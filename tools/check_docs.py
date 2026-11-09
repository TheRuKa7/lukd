"""Validate repository documentation contracts; no engine/build success is inferred.

Run: python tools/check_docs.py [--json] [--self-test]
Uses only the Python standard library. Historical reports retain their semantics,
but their live Markdown links are checked just like current documents.
"""
from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.git', 'node_modules', '.venv', 'venv', 'Library', 'Temp', 'build'}
VIEWS = {'front', 'left', 'right', 'back'}


def without_code(text):
    """Keep line count; ignore fenced and inline literal examples."""
    lines, fence = [], None
    for line in text.splitlines():
        m = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if m:
            mark = m[1]
            if fence is None:
                fence = mark[0]
            elif mark[0] == fence:
                fence = None
            lines.append('')
        else:
            lines.append('' if fence else re.sub(r'(`+).*?\1', '', line))
    return '\n'.join(lines)


def slug(text):
    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r'!?\[([^\]]+)\]\([^)]*\)', r'\1', text)
    text = text.replace('`', '').lower().strip()
    # GitHub-style heading IDs retain Unicode letters/numbers and underscores.
    return re.sub(r'[^\w\- ]', '', text).replace(' ', '-')


def anchors(text):
    result, seen = set(), {}
    fence = None
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if m:
            fence = None if fence == m[1][0] else m[1][0]
            continue
        if fence:
            continue
        h = re.match(r'^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$', line)
        title = h[1] if h else None
        if title is None and i + 1 < len(lines) and re.match(r'^\s{0,3}(=+|-+)\s*$', lines[i+1]) and line.strip():
            title = line.strip()
        if title is not None:
            base = slug(title)
            n = seen.get(base, 0)
            seen[base] = n + 1
            result.add(base + (f'-{n}' if n else ''))
        result.update(re.findall(r'<a\s+(?:[^>]*?\s)?(?:id|name)=["\']([^"\']+)', line, re.I))
    return result


def markdown_links(text):
    """Yield (line,destination), including references and balanced parentheses."""
    text = without_code(text)
    definitions = {}
    for m in re.finditer(r'^\s{0,3}\[([^\]]+)\]:\s*(?:<([^>]+)>|(\S+))', text, re.M):
        definitions[m[1].strip().casefold()] = m[2] or m[3]
        yield text.count('\n', 0, m.start()) + 1, m[2] or m[3]
    pattern = re.compile(r'!?\[([^\]\n]*(?:\n[^\]\n]*)?)\]')
    consumed = 0
    for m in pattern.finditer(text):
        if m.start() < consumed:
            continue
        pos = m.end()
        if pos < len(text) and text[pos] == ':':
            continue
        while pos < len(text) and text[pos].isspace():
            pos += 1
        dest = None
        if pos < len(text) and text[pos] == '(':
            pos += 1
            start, depth, angle = pos, 1, False
            while pos < len(text):
                ch = text[pos]
                if ch == '\\':
                    pos += 2
                    continue
                if ch == '<' and pos == start:
                    angle = True
                elif ch == '>' and angle:
                    angle = False
                elif not angle:
                    if ch == '(':
                        depth += 1
                    elif ch == ')':
                        depth -= 1
                        if depth == 0:
                            raw = text[start:pos].strip()
                            if raw.startswith('<') and '>' in raw:
                                dest = raw[1:raw.index('>')]
                            else:
                                dest = re.split(r'\s+["\']', raw, maxsplit=1)[0]
                            break
                pos += 1
        elif pos < len(text) and text[pos] == '[':
            end = text.find(']', pos + 1)
            if end >= 0:
                dest = definitions.get((text[pos+1:end] or m[1]).strip().casefold())
                consumed = end + 1
        else:
            dest = definitions.get(m[1].strip().casefold())
        if dest:
            yield text.count('\n', 0, m.start()) + 1, dest


def validate_series_plan(readme, opening, treatment, ledger, story):
    """Validate authored plan shape only; never infer native Mangaka output."""
    errors, counts = [], {}
    match = re.search(r'<!-- series-plan-contract -->\s*```json\s*(\{.*?\})\s*```', readme, re.S)
    contract = {}
    if match:
        try:
            contract = json.loads(match[1])
        except ValueError as exc:
            errors.append(f'series plan: invalid JSON contract: {exc}')
    else:
        errors.append('series plan: missing README planning contract')
    expected = {'evidence_scope': 'plan_only', 'production_tool': 'Mangaka', 'story_art': 'black_and_white', 'reading_direction': 'ltr', 'chapter_count': 22, 'story_pages_per_chapter': 30, 'story_page_target': 660, 'ordinary_image_generation_for_story_pages': False}
    for key, value in expected.items():
        if contract.get(key) != value:
            errors.append(f'series plan: {key} must be {value!r}, not {contract.get(key)!r}')

    def sections(text, pattern):
        matches = list(re.finditer(pattern, text, re.M))
        return [(int(m[1]), m[2].strip(), text[m.end():matches[i+1].start() if i+1 < len(matches) else len(text)]) for i, m in enumerate(matches)]

    first = sections(opening, r'^## Chapter(\d{2}) - (.+)$')
    later = sections(treatment, r'^## (\d{2}) — (.+)$')
    if [n for n, _, _ in first] != [1, 2, 3]:
        errors.append('series plan: opening must contain unique ordered chapters01–03')
    if [n for n, _, _ in later] != list(range(4, 23)):
        errors.append('series plan: treatment must contain unique ordered chapters04–22')
    numbered_pages, blocks = 0, 0
    for chapter, _, body in first:
        pages = [int(x) for x in re.findall(r'^\*\*Page(\d{2})\.\*\*', body, re.M)]
        if pages != list(range(1, 31)):
            errors.append(f'series plan chapter{chapter:02}: expected ordered unique Page01–Page30 instructions')
        numbered_pages += len(pages)
    expected_blocks = ['1–5', '6–10', '11–15', '16–20', '21–25', '26–30']
    for chapter, _, body in later:
        found = re.findall(r'^\|(1–5|6–10|11–15|16–20|21–25|26–30)\|', body, re.M)
        if found != expected_blocks:
            errors.append(f'series plan chapter{chapter:02}: expected six ordered five-page blocks through26–30')
        blocks += len(found)
    titles = [(int(n), title.strip()) for n, title in re.findall(r'^\|(\d{2}) — \*\*(.+?)\*\*', ledger, re.M)]
    if [n for n, _ in titles] != list(range(1, 23)):
        errors.append('series plan: reveal ledger must contain22 unique ordered chapter titles')
    title_map = dict(titles)
    for chapter, title, _ in first + later:
        if title_map.get(chapter) != title:
            errors.append(f'series plan chapter{chapter:02}: script/treatment title differs from reveal ledger')
    proofs = set(re.findall(r'`(piece\.[a-z_]+)`', ledger))
    canonical = set(re.findall(r'piece\.[a-z_]+', story))
    if len(proofs) != 8 or not proofs <= canonical:
        errors.append('series plan: expected exactly eight canonical protected proof IDs')
    companions = ['Vesper', 'Maeve', 'Hina', 'Jinling', 'Bai Si', 'Shunya', 'Prima', 'Fibi']
    stages = {}
    for line in ledger.splitlines():
        cells = [x.strip() for x in line.split('|')[1:-1]] if line.startswith('|') else []
        if cells and cells[0] in companions:
            if cells[0] in stages:
                errors.append(f'series plan: duplicate core arc {cells[0]}')
            stages[cells[0]] = cells[1:]
    if set(stages) != set(companions) or any(len(values) != 4 or not all(values) for values in stages.values()):
        errors.append('series plan: expected eight core arc rows with four nonempty stages each')
    planned = numbered_pages + blocks * 5
    if planned != 660:
        errors.append(f'series plan: authored instructions account for {planned} planned pages, expected660')
    counts.update(series_planned_chapters=len(first)+len(later), series_story_page_target=contract.get('story_page_target'), series_opening_numbered_page_instructions=numbered_pages, series_later_five_page_blocks=blocks, series_planned_pages_accounted=planned, series_canonical_proof_ids=len(proofs), series_core_relationship_stage_cells=sum(len(values) for values in stages.values()))
    return {'errors': errors, 'counts': counts, 'evidence_scope': 'Authored plan structure only; no native Mangaka chapter/page exports verified.'}


class Audit:
    def __init__(self, root=ROOT):
        self.root = Path(root).resolve()
        self.errors, self.warnings, self.counts = [], [], {}

    def error(self, message):
        self.errors.append(message)

    def path(self, value, context, required=True):
        if not value:
            if required:
                self.error(f'{context}: missing path')
            return None
        p = (self.root / value.replace('\\', '/')).resolve()
        if not p.is_relative_to(self.root):
            self.error(f'{context}: path leaves repository: {value}')
            return None
        if not p.is_file():
            self.error(f'{context}: missing file: {value}')
            return None
        return p

    def read_json(self, name):
        p = self.path(name, name)
        if p:
            try:
                return json.loads(p.read_text(encoding='utf-8-sig'))
            except (ValueError, OSError) as exc:
                self.error(f'{name}: {exc}')
        return None

    def links(self):
        documents = [p for p in self.root.rglob('*.md') if not any(x in EXCLUDED for x in p.relative_to(self.root).parts)]
        count = 0
        for p in documents:
            content = p.read_text(encoding='utf-8-sig')
            for line, target in markdown_links(content):
                # Protocol URLs are not local links; external liveness is a separate research job.
                if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', target) or target.startswith('//'):
                    continue
                parts = urlsplit(target)
                raw = unquote(parts.path).replace('\\', '/')
                local = (self.root / raw.lstrip('/') if raw.startswith('/') else p.parent / raw).resolve() if raw else p
                ctx = f'{p.relative_to(self.root)}:{line}'
                count += 1
                if not local.is_relative_to(self.root):
                    self.error(f'{ctx}: local link leaves repository: {target}')
                elif not local.exists():
                    self.error(f'{ctx}: broken local link: {target}')
                elif parts.fragment and local.suffix.lower() == '.md':
                    if unquote(parts.fragment) not in anchors(local.read_text(encoding='utf-8-sig')):
                        self.error(f'{ctx}: missing heading anchor: {target}')
        self.counts.update(markdown_files=len(documents), local_links=count)

    def catalogue(self):
        data = self.read_json('art/catalog/characters.json')
        if not data:
            return
        rows, seen, complete = data.get('entries', []), set(), 0
        unique_sets, contextual, shared = set(), 0, 0
        for row in rows:
            ident = row.get('id')
            if not ident or ident in seen:
                self.error(f'catalog: missing/duplicate ID {ident}')
            seen.add(ident)
            context = f'catalog {ident}'
            for field in ['name', 'group', 'role', 'region', 'appearance', 'power', 'provenance', 'coverage_policy']:
                if not row.get(field):
                    self.error(f'{context}: missing {field}')
            for side in VIEWS:
                if not row.get('appearance', {}).get(side):
                    self.error(f'{context}: no written {side} specification')
            paths = row.get('view_paths', {})
            if set(paths) != VIEWS:
                self.error(f'{context}: expected exactly four view keys')
            present = all(bool(v) and (self.root / v).is_file() for v in paths.values()) and len(paths) == 4
            claimed = row.get('provenance', {}).get('four_view_files_present')
            if claimed is True and not present:
                self.error(f'{context}: claimed four views absent')
            if any(paths.values()) and not all(paths.values()):
                self.error(f'{context}: partial turnaround must be explicitly withheld or completed')
            for side, value in paths.items():
                if value:
                    self.path(value, f'{context} {side}')
            if row.get('source3d_path'):
                self.path(row['source3d_path'], context + ' source3d')
            elif present:
                self.error(f'{context}: rendered views have no source3d')
            for source in row.get('source_documents', []):
                self.path(source, context + ' source document')
            for palette in row.get('palette', []):
                if not re.fullmatch(r'#[0-9A-Fa-f]{6}', palette.get('hex', '')):
                    self.error(f'{context}: invalid palette hex')
            if not present:
                self.warnings.append(f'{context}: no complete existing four-view set; not final coverage')
            complete += present
            if present:
                unique_sets.add(tuple(paths.get(side) for side in sorted(VIEWS)))
            contextual += row.get('coverage_policy', {}).get('requires_character_turnaround') is False
            shared += bool(row.get('provenance', {}).get('proxy_id')) or str(row.get('provenance', {}).get('render_scope', '')).startswith('compound group')
        # Every authored upstream cast ID must remain represented, including outfits.
        tree = ast.parse((self.root / 'tools/cast.py').read_text(encoding='utf-8-sig'))
        cast_ids = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'dict':
                for keyword in node.keywords:
                    if keyword.arg == 'key' and isinstance(keyword.value, ast.Constant) and isinstance(keyword.value.value, str):
                        cast_ids.add(keyword.value.value)
            if isinstance(node, ast.Dict):
                for key, value in zip(node.keys, node.values):
                    if isinstance(key, ast.Constant) and key.value in {'id', 'key'} and isinstance(value, ast.Constant) and isinstance(value.value, str):
                        cast_ids.add(value.value)
        for ident in sorted(cast_ids - seen):
            self.error(f'catalog: missing source cast ID {ident}')
        if not cast_ids:
            self.error('catalog: no upstream cast IDs extracted; coverage check is invalid')
        aliases = {
            'Ao and Aka, the Kitsune twins': ['ao', 'aka'],
            'Basilica surveyors in a Noise storm': ['basilica_surveyor'],
            'The Headless Horseman': ['headless_horseman'],
            'The Ghost Train': ['ghost_train'],
        }
        names = {row.get('name', '').casefold() for row in rows}
        bestiary = (self.root / 'docs/BESTIARY.md').read_text(encoding='utf-8-sig')
        opponent_names = []
        for line in bestiary.splitlines():
            if line.startswith('|'):
                match = re.search(r'\*\*([^*]+)\*\*', line)
                if match:
                    opponent_names.append(match[1])
        for name in opponent_names:
            if name.casefold() in names:
                continue
            if name in aliases and all(x in seen for x in aliases[name]):
                continue
            self.error(f'catalog: bestiary opponent lacks indexed coverage: {name}')
        self.counts.update(catalog_records=len(rows), complete_four_view_records=complete, upstream_cast_ids=len(cast_ids))
        self.counts['bestiary_table_opponents'] = len(opponent_names)
        self.counts.update(unique_four_view_sets=len(unique_sets), contextual_not_anatomical_records=contextual, shared_group_or_uniform_records=shared)

    def backlog(self):
        name = 'docs/refinement/BACKLOG.csv'
        with (self.root / name).open(encoding='utf-8-sig', newline='') as f:
            rows = list(csv.DictReader(f))
        ids = [r['id'] for r in rows]
        if len(ids) != len(set(ids)):
            self.error('backlog: duplicate IDs')
        graph = {r['id']: [x.strip() for x in r['depends_on'].split(';') if x.strip()] for r in rows}
        active, done = set(), set()
        def visit(node):
            if node not in graph:
                self.error(f'backlog: unknown dependency {node}')
                return
            if node in active:
                self.error(f'backlog: dependency cycle at {node}')
                return
            if node in done:
                return
            active.add(node)
            for dep in graph[node]:
                visit(dep)
            active.remove(node)
            done.add(node)
        for node in graph:
            visit(node)
        self.counts['backlog_items'] = len(rows)

    def tuning(self):
        name = 'tuning/jam_tuning.csv'
        with (self.root / name).open(encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != ['section', 'key', 'value', 'unit', 'note']:
                self.error('tuning: unexpected schema')
            rows = list(reader)
        seen = set()
        integer_units = {'balance', 'level', 'fixed_base', 'logical_px', 'logical_px_per_s', 'count', 'rounds', 'seconds', 'minutes', 'fps', 'decimal_mb', 'mib', 'mult'}
        for row in rows:
            ident = (row['section'], row['key'])
            if ident in seen:
                self.error(f'tuning: duplicate {ident}')
            seen.add(ident)
            try:
                value = float(row['value'])
                if not math.isfinite(value) or value <= 0:
                    raise ValueError('must be positive finite scalar')
                if row['unit'] in integer_units and not value.is_integer():
                    raise ValueError('integer unit needs integer scalar')
                if row['unit'] not in integer_units | {'ratio'}:
                    raise ValueError('unknown unit')
            except (TypeError, ValueError) as exc:
                self.error(f'tuning {ident}: {exc}: {row.get("value")}')
        required = {
            'party': 'start_balance balance_per_level start_level base_per_level level_cap_jam',
            'hero': 'nil_speed vesper_speed cell_height lucky_width assist_speed_mult first_demo_speed_mult',
            'pattern': 'bust pair zero_sum cascade jackpot_min reaper reaper_current_balance_share overwrite',
            'passive': 'vesper_bonus_per_actual_seven',
            'favour': 'warm_after_busts warm_speed_mult warm_match_width haps_hand_after_busts',
            'charm': 'horseshoe_chosen_width black_cat_uses_per_fight ofuda_uses_per_fight',
            'enemy': 'debt_hound_balance debt_hound_base varro_balance varro_base_phase1 varro_base_phase2 varro_phase2_share varro_jar_affected_rounds varro_jar_defences',
            'build': 'total_download_mb initial_download_mb peak_memory_mib desktop_fps start_to_first_action_seconds lucky_choice_seconds',
        }
        for section, keys in required.items():
            for key in keys.split():
                if (section, key) not in seen:
                    self.error(f'tuning: missing required scalar {(section, key)}')
        self.counts['tuning_scalars'] = len(rows)

    def architecture(self):
        data = self.read_json('docs/architecture/tr-registry.json')
        if not data:
            return
        seen = set()
        for row in data.get('requirements', []):
            ident = row.get('id')
            if not ident or ident in seen:
                self.error(f'traceability: duplicate/missing ID {ident}')
            seen.add(ident)
            if row.get('status') != 'specified' or row.get('unity_implementation') != 'not_started':
                self.error(f'{ident}: Unity implementation claim needs a revised evidence baseline')
            for source in row.get('sources', []):
                path = self.path(source['path'], ident + ' requirement source')
                if path and slug(source['heading']) not in anchors(path.read_text(encoding='utf-8-sig')):
                    self.error(f'{ident}: source heading missing: {source["heading"]}')
            adr = self.path(row.get('adr'), ident + ' ADR')
            if adr and ident not in adr.read_text(encoding='utf-8-sig'):
                self.error(f'{ident}: ADR does not explicitly trace requirement')
            for artifact in row.get('existing_verification', []):
                self.path(artifact, ident + ' existing verification')
            # Future proof is a named gate/description, never an invented file.
            if not row.get('required_verification') or not row.get('gate'):
                self.error(f'{ident}: absent future verification gate')
        self.counts['technical_requirements'] = len(seen)

    def story_ids(self):
        script = (self.root / 'docs/JAM_SCRIPT.md').read_text(encoding='utf-8-sig')
        jam_ids = re.findall(r'^\|\s*`(jam_[a-z0-9_]+)`\s*\|', script, re.M)
        if not jam_ids or len(jam_ids) != len(set(jam_ids)):
            self.error('jam script: absent or duplicate table IDs')
        pages = self.read_json('art/manga/chapter_01/pages.json')
        dialogue = self.read_json('art/manga/chapter_01/dialogue.json')
        if not pages or not dialogue:
            return
        page_ids, panel_ids, text_ids = set(), set(), set()
        panel_page, panel_text = {}, {}
        missing_outputs = []
        for page in pages.get('pages', []):
            ident = page.get('id')
            if not ident or ident in page_ids:
                self.error(f'legacy manga study: duplicate/missing page ID {ident}')
            page_ids.add(ident)
            for asset in page.get('reference_assets', []):
                self.path(asset, f'legacy manga study {ident} reference')
            for key in ['clean_art', 'lettered_art']:
                path = page.get(key)
                if not path or not (self.root / path).is_file():
                    missing_outputs.append(f'{ident}:{key}')
            for panel in page.get('panels', []):
                panel_id = panel.get('id')
                if not panel_id or panel_id in panel_ids:
                    self.error(f'legacy manga study: duplicate/missing panel ID {panel_id}')
                panel_ids.add(panel_id)
                panel_page[panel_id] = ident
                panel_text[panel_id] = panel.get('dialogue_ids', [])
        for entry in dialogue.get('entries', []):
            ident = entry.get('id')
            if not ident or ident in text_ids:
                self.error(f'legacy manga study: duplicate/missing dialogue ID {ident}')
            text_ids.add(ident)
            panel_id = entry.get('panel_id')
            if panel_id not in panel_ids or panel_page.get(panel_id) != entry.get('page_id'):
                self.error(f'legacy manga study {ident}: page/panel reference mismatch')
            if ident not in panel_text.get(panel_id, []):
                self.error(f'legacy manga study {ident}: panel lacks dialogue back-reference')
        for panel_id, refs in panel_text.items():
            for ident in refs:
                if ident not in text_ids:
                    self.error(f'legacy manga study {panel_id}: missing dialogue {ident}')
        if pages.get('page_count') != len(page_ids):
            self.error('legacy manga study: declared page count differs from unique pages')
        if missing_outputs:
            # Script manifests may name planned exports without claiming they exist.
            # A verified/final claim must instead have every declared artifact.
            message = 'legacy manga study: declared exports absent: ' + ', '.join(missing_outputs)
            if re.search(r'\b(final|verified|complete)\b', str(pages.get('status', '')), re.I):
                self.error(message)
            else:
                self.warnings.append(message + '; manifest is not a completed-export claim')
        self.counts.update(jam_script_ids=len(jam_ids), legacy_manga_study_pages=len(page_ids), legacy_manga_study_panels=len(panel_ids), legacy_manga_study_dialogue_ids=len(text_ids), legacy_manga_study_missing_declared_exports=len(missing_outputs))

    def series_plan(self):
        names = ['README.md', 'OPENING_SCRIPT_01_03.md', 'CHAPTER_TREATMENT_04_22.md', 'SERIES_REVEAL_LEDGER.md']
        contents = [(self.root / 'docs/manga' / name).read_text(encoding='utf-8-sig') for name in names]
        for name in ['MANGAKA_WORKFLOW.md', 'SERIES_PRODUCTION_BRIEF.md', 'OPENING_EDITORIAL_REVIEW.md']:
            self.path('docs/manga/' + name, 'series plan source hierarchy')
        report = validate_series_plan(*contents, (self.root / 'docs/STORY.md').read_text(encoding='utf-8-sig'))
        self.errors.extend(report['errors'])
        self.counts.update(report['counts'])

    def provenance(self):
        manifests = ['art/renders/lookdev/lookdev_v5.json', 'art/source/encounter_drafts.json']
        hashes = 0
        for name in manifests:
            if not (self.root / name).exists():
                self.warnings.append(f'provenance: {name} not yet generated')
                continue
            data = self.read_json(name)
            def walk(value, ctx):
                nonlocal hashes
                if isinstance(value, dict):
                    filename = value.get('path') or value.get('file')
                    digest = value.get('sha256')
                    if filename and digest:
                        p = self.path(filename, ctx)
                        if p and hashlib.sha256(p.read_bytes()).hexdigest() != digest:
                            self.error(f'{ctx}: hash differs from recorded source {filename}')
                        hashes += 1
                    for key, child in value.items():
                        walk(child, f'{ctx}/{key}')
                elif isinstance(value, list):
                    for i, child in enumerate(value):
                        walk(child, f'{ctx}/{i}')
            if data:
                walk(data, name)
                for key in ['source_script', 'source']:
                    if data.get(key):
                        p = self.path(data[key], name + '/' + key)
                        if p and data.get('script_sha256') and key == 'source_script':
                            hashes += 1
                            if hashlib.sha256(p.read_bytes()).hexdigest() != data['script_sha256']:
                                self.error(f'{name}: recorded script hash is stale')
        self.counts['provenance_hashes'] = hashes

    def run(self):
        for check in [self.links, self.catalogue, self.backlog, self.tuning, self.architecture, self.story_ids, self.series_plan, self.provenance]:
            try:
                check()
            except (KeyError, TypeError, OSError, ValueError) as exc:
                self.error(f'{check.__name__}: malformed/missing input: {exc}')
        return {'status': 'PASS' if not self.errors else 'FAIL', 'counts': self.counts, 'errors': self.errors, 'warnings': self.warnings, 'limits': 'Local documentation/data integrity only. The 22x30 manga counters validate a superseded historical draft; the new 49x22 outline and full novel are not validated by these counters. Neither proves native Mangaka chapters or a finished comic. No visual, legal, accessibility, playtest or Unity acceptance.'}


def self_test():
    import unittest
    import tempfile
    class ParserTests(unittest.TestCase):
        def test_balanced_and_angle_paths(self):
            self.assertEqual([x[1] for x in markdown_links('[a](a(b).md#x) [b](<folder name/a.md> "title")')], ['a(b).md#x', 'folder name/a.md'])
        def test_literals_and_references(self):
            text = '`[fake](missing.md)`\n```md\n[x](bad.md)\n```\n[a][ref]\n[ref]: okay.md\n'
            self.assertEqual([x[1] for x in markdown_links(text)], ['okay.md', 'okay.md'])
        def test_duplicate_unicode_anchor(self):
            self.assertEqual(anchors('# Śūnya: Zero\n## Again\n## Again'), {'śūnya-zero', 'again', 'again-1'})
        def test_existing_file_with_missing_anchor_fails(self):
            with tempfile.TemporaryDirectory() as name:
                root = Path(name)
                (root/'a.md').write_text('# Present\n[x](b.md#absent)', encoding='utf-8')
                (root/'b.md').write_text('# Present', encoding='utf-8')
                audit = Audit(root)
                audit.links()
                self.assertEqual(len(audit.errors), 1)
                self.assertIn('missing heading anchor', audit.errors[0])
        def test_backlog_cycle_and_unknown_dependency_fail(self):
            with tempfile.TemporaryDirectory() as name:
                root = Path(name)
                (root/'docs/refinement').mkdir(parents=True)
                (root/'docs/refinement/BACKLOG.csv').write_text('id,depends_on\nA,B\nB,A;MISSING\n', encoding='utf-8')
                audit = Audit(root)
                audit.backlog()
                self.assertTrue(any('cycle' in error for error in audit.errors))
                self.assertTrue(any('unknown dependency' in error for error in audit.errors))
        def test_expression_and_duplicate_scalar_fail(self):
            with tempfile.TemporaryDirectory() as name:
                root = Path(name)
                (root/'tuning').mkdir()
                (root/'tuning/jam_tuning.csv').write_text('section,key,value,unit,note\npattern,pair,2 x 3,mult,\npattern,pair,2,mult,\n', encoding='utf-8')
                audit = Audit(root)
                audit.tuning()
                self.assertTrue(any('duplicate' in error for error in audit.errors))
                self.assertTrue(any('2 x 3' in error for error in audit.errors))
                self.assertTrue(any('missing required scalar' in error for error in audit.errors))
        def test_source_hash_change_is_detected(self):
            with tempfile.TemporaryDirectory() as name:
                root = Path(name)
                (root/'art/source').mkdir(parents=True)
                (root/'asset.png').write_bytes(b'changed bytes')
                (root/'art/source/encounter_drafts.json').write_text(json.dumps({'records': [{'path': 'asset.png', 'sha256': hashlib.sha256(b'original').hexdigest()}]}), encoding='utf-8')
                audit = Audit(root)
                audit.provenance()
                self.assertTrue(any('hash differs' in error for error in audit.errors))
        def series_inputs(self):
            names = ['README.md', 'OPENING_SCRIPT_01_03.md', 'CHAPTER_TREATMENT_04_22.md', 'SERIES_REVEAL_LEDGER.md']
            return [(ROOT/'docs/manga'/name).read_text(encoding='utf-8-sig') for name in names] + [(ROOT/'docs/STORY.md').read_text(encoding='utf-8-sig')]
        def test_current_series_is_a_plan_not_a_native_export_count(self):
            report = validate_series_plan(*self.series_inputs())
            self.assertEqual(report['errors'], [])
            self.assertEqual(report['counts']['series_planned_pages_accounted'], 660)
            self.assertEqual(report['counts']['series_core_relationship_stage_cells'], 32)
            self.assertNotIn('native_pages_produced', report['counts'])
        def test_duplicate_numbered_page_cannot_pass_as_thirty_pages(self):
            values = self.series_inputs()
            values[1] = values[1].replace('**Page30.**', '**Page29.**', 1)
            errors = validate_series_plan(*values)['errors']
            self.assertTrue(any('chapter01' in error and 'Page01–Page30' in error for error in errors))
        def test_short_later_chapter_and_wrong_title_fail(self):
            values = self.series_inputs()
            values[2] = values[2].replace('|26–30|', '|26–29|', 1).replace('A Hundred Wishes', 'A Different Title', 1)
            errors = validate_series_plan(*values)['errors']
            self.assertTrue(any('six ordered five-page blocks' in error for error in errors))
            self.assertTrue(any('title differs' in error for error in errors))
        def test_ordinary_image_policy_and_invented_proof_fail(self):
            values = self.series_inputs()
            values[0] = values[0].replace('"ordinary_image_generation_for_story_pages": false', '"ordinary_image_generation_for_story_pages": true')
            values[3] = values[3].replace('piece.enma_page', 'piece.invented_proof')
            errors = validate_series_plan(*values)['errors']
            self.assertTrue(any('ordinary_image_generation_for_story_pages' in error for error in errors))
            self.assertTrue(any('eight canonical protected proof IDs' in error for error in errors))
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ParserTests))
    return result.wasSuccessful()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        sys.exit(0 if self_test() else 1)
    report = Audit().run()
    if args.json:
        print(json.dumps(report, ensure_ascii=True, indent=2))
    else:
        print(f'Document contracts: {report["status"]}')
        print(', '.join(f'{k}={v}' for k, v in report['counts'].items()))
        for message in report['errors']:
            print('ERROR:', message)
        for message in report['warnings']:
            print('PENDING:', message)
        print(report['limits'])
    sys.exit(0 if not report['errors'] else 1)
