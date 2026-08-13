from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os
import re


def _resolve_google_scholar_id() -> str:
    sid = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if sid:
        return sid
    config_path = os.path.join(os.path.dirname(__file__), "..", "_config.yml")
    if os.path.isfile(config_path):
        with open(config_path, encoding="utf-8") as f:
            text = f.read()
        m = re.search(
            r"googlescholar\s*:\s*\"[^\"]*[?&]user=([^&\"]+)",
            text,
        )
        if m:
            return m.group(1)
    raise SystemExit(
        "缺少 Google Scholar 用户 ID：请设置环境变量 GOOGLE_SCHOLAR_ID，"
        "或在仓库根目录 _config.yml 的 author.googlescholar 中填写含 user= 的链接。"
    )


author: dict = scholarly.search_author_id(_resolve_google_scholar_id())
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
