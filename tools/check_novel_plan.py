"""Check the current edition's structure and prerequisite schedule, not literary quality."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    plan = (ROOT/'docs/manga/SEVEN_VOLUME_NOVEL_PLAN.md').read_text(encoding='utf-8-sig')
    volumes = re.findall(r'(?ms)^## Volume (\d+) — (.*?)\n(.*?)(?=^## |\Z)', plan)
    errors=[]
    if len(volumes)!=7: errors.append('Expected seven volumes')
    numbers=[]
    for index, (number,title,body) in enumerate(volumes,1):
        chapters=re.findall(r'(?m)^(\d+)\. \*\*(.+?)\*\* — (.+)$',body)
        expected=list(range((index-1)*7+1,index*7+1))
        actual=[int(c[0]) for c in chapters]
        if int(number)!=index or actual!=expected: errors.append(f'Volume {index}: nonsequential/missing chapters')
        numbers+=actual
    seals=re.findall(r'\bSeal (\d)\b', '\n'.join(v[2] for v in volumes))
    if seals!=['1','9','8','0','2','7']: errors.append(f'Incomplete or reordered office Seals: {seals}')
    if len(set(numbers))!=49: errors.append('Expected49 unique chapters')
    bible=(ROOT/'docs/novel/RESOLVED_SERIES_BIBLE.md').read_text(encoding='utf-8-sig')
    for phrase in ['chapters 25–26','chapter 45','125,000','6–8 hours','8–12 hours']:
        if phrase not in bible: errors.append('Missing adopted gate/target: '+phrase)
    report=dict(status='FAIL' if errors else 'PASS',volumes=len(volumes),chapters=len(numbers),story_pages=49*22,story_pages_per_volume=7*22,office_seals=seals,errors=errors,limits='Structural planning only; not scene coverage, prose completeness, literary quality,1078 generated pages,or measured playtime.')
    print(json.dumps(report,indent=2))
    raise SystemExit(bool(errors))

if __name__=='__main__': main()
