"""Filesystem-backed prompt store."""
from pathlib import Path
from datetime import datetime
import json
import yaml


def vault_dir(base: str = None) -> Path:
    root = Path(base) if base else Path.home() / '.promptvault'
    root.mkdir(parents=True, exist_ok=True)
    return root


def create_prompt(title: str, content: str, tags: list, base: str = None) -> Path:
    root = vault_dir(base)
    slug = ''.join(c.lower() if c.isalnum() else '-' for c in title).strip('-')
    path = root / f'{slug}.yaml'
    data = {
        'title': title,
        'tags': tags,
        'content': content,
        'created_at': datetime.utcnow().isoformat() + 'Z',
        'updated_at': datetime.utcnow().isoformat() + 'Z',
    }
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding='utf-8')
    return path


def list_prompts(base: str = None) -> list:
    root = vault_dir(base)
    prompts = []
    for f in sorted(root.glob('*.yaml')):
        data = yaml.safe_load(f.read_text(encoding='utf-8'))
        prompts.append({'path': str(f), **data})
    return prompts


def search_prompts(query: str, base: str = None) -> list:
    q = query.lower()
    results = []
    for p in list_prompts(base):
        hay = ' '.join([p.get('title',''), p.get('content',''), ' '.join(p.get('tags',[]))]).lower()
        if q in hay:
            results.append(p)
    return results


def export_json(base: str = None) -> str:
    return json.dumps(list_prompts(base), ensure_ascii=False, indent=2)
