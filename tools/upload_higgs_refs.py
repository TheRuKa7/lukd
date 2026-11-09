"""PUT local reference bytes to provider-issued upload URLs. Never logs signed URLs."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

def upload(item):
    path=Path(item['local_path'])
    if not path.is_file(): raise FileNotFoundError(path)
    try:
        result=subprocess.run(['curl.exe','-f','-sS','--max-time','90','-X','PUT',
            '-H','Content-Type: '+item['content_type'],'--data-binary','@'+str(path),
            item['upload_url'],'--write-out','%{http_code}'],capture_output=True,text=True)
        status=int(result.stdout[-3:]) if result.stdout[-3:].isdigit() else 0
    except Exception as exc:
        # Do not echo exception strings: some clients include signed request URLs.
        return dict(index=item['index'],media_id=item['media_id'],status='upload_failed',error_type=type(exc).__name__)
    return dict(index=item['index'],media_id=item['media_id'],http_status=status,
                status='uploaded' if status==200 else 'upload_failed')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');args=ap.parse_args()
    jobs=json.loads(Path(args.input).read_text(encoding='utf-8-sig'))
    results=list(ThreadPoolExecutor(max_workers=5).map(upload,jobs))
    Path(args.output).write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(results))
    if any(x['status']!='uploaded' for x in results):raise SystemExit(1)

if __name__=='__main__':main()
