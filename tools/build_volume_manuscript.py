"""Compile a continuous reading copy and verifiable source manifest; not literary approval."""
from pathlib import Path
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Reject stale or missing compiled artifacts')
    parser.add_argument('--volume', type=int, choices=range(1, 8), default=1)
    args = parser.parse_args()
    ledger = json.loads((ROOT/'docs/novel/scene_ledger.json').read_text(encoding='utf-8'))
    plan = (ROOT/'docs/manga/SEVEN_VOLUME_NOVEL_PLAN.md').read_text(encoding='utf-8-sig')
    titles = {int(n): title for n, title in re.findall(r'^## Volume (\d+) — ([^:\n]+):', plan, re.M)}
    volume_title = titles[args.volume]
    volume_word = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven'][args.volume-1]
    rows = [row for row in ledger['chapters'] if row['volume'] == args.volume]
    expected = list(range((args.volume-1)*7+1, args.volume*7+1))
    if [row['chapter'] for row in rows] != expected:
        raise ValueError('Incomplete or reordered volume ledger')
    chapters = []
    parts = ['# ZERO-SUM: OMEN', '', '# The Remainder', '', f'## Volume {volume_word}: {volume_title}', '']
    for row in rows:
        n = row['chapter']
        paths = list((ROOT/f'docs/novel/volume_{args.volume:02d}').glob(f'chapter_{n:02d}_*.md'))
        if len(paths) != 1:
            raise ValueError(f'Chapter {n}: expected exactly one source, found {len(paths)}')
        path = paths[0]
        raw = path.read_bytes()
        text = raw.decode('utf-8-sig')
        heading = f'## Chapter {n}: {row["title"]}'
        if text.count(heading) != 1:
            raise ValueError(f'Chapter {n}: title differs from ledger')
        body = text.split(heading, 1)[1].strip()
        words = len(re.findall(r"\b[\w’'-]+\b", body))
        if not body or re.search(r'(?im)^\s*(TODO|TBD|PLACEHOLDER)\b', body):
            raise ValueError(f'Chapter {n}: missing prose or explicit placeholder')
        parts += [heading, '', body, '']
        chapters.append(dict(chapter=n, title=row['title'], source=path.relative_to(ROOT).as_posix(),
                             sha256=sha(raw), body_words=words,
                             planned_scene_ids=[s['id'] for s in row['scenes']]))
    manuscript = ('\n'.join(parts).rstrip()+'\n').encode('utf-8')
    out = ROOT/'output/novel'
    slug = re.sub(r'[^a-z0-9]+', '_', volume_title.lower()).strip('_')
    md = out/f'volume_{args.volume:02d}_{slug}.md'
    report = dict(schema_version=1, evidence_scope='Compilation, source identity and body word counts; not independent reader acceptance',
                  volume=args.volume, chapters=chapters, body_words=sum(c['body_words'] for c in chapters),
                  manuscript_sha256=sha(manuscript), whole_series_editorially_accepted=False,
                  authored_manga_pages=0)
    manifest = (json.dumps(report, indent=2, ensure_ascii=False)+'\n').encode('utf-8')
    outputs = [(md, manuscript), (out/f'volume_{args.volume:02d}_manifest.json', manifest)]
    for path, data in outputs:
        if args.check:
            if not path.is_file() or path.read_bytes() != data:
                raise ValueError('Missing or stale artifact: '+str(path))
        else:
            out.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print(json.dumps(dict(status='PASS', mode='check' if args.check else 'build',
                          chapters=len(chapters), body_words=report['body_words'],
                          manuscript=md.relative_to(ROOT).as_posix()), indent=2))

if __name__ == '__main__':
    main()
