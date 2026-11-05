"""Merge the Nov 5 2026 studio manifests into schedule/posts.json (adds new ids, replaces 2 fixed entries in place)."""
import json, os
R = '/home/claude/steadfold-autopost'
KEYS = ['id','account','publish_at','video','cover','images','caption','first_comment','alt_text','trial']
Q = json.load(open(f'{R}/schedule/posts.json'))
posts = Q['posts']; idx = {p['id']: i for i, p in enumerate(posts)}
pub = open(f'{R}/state/published.json').read()
held = ''.join(open(f'{R}/schedule/{f}').read() for f in os.listdir(f'{R}/schedule') if f.startswith('held-'))
add = rep = 0
for f in ['littlefold','lockedhour','fullyfunded','hourback','fullyfunded_fix','littlefold_fix']:
    d = json.load(open(f'{R}/studio/editorial/nov05/{f}.json')); d = d if isinstance(d, list) else [d]
    for e in d:
        x = {k: e[k] for k in KEYS if k in e and e[k] not in (None, '')}
        for m in [x.get('video'), x.get('cover')] + (x.get('images') or []):
            if m: assert os.path.exists(f'{R}/media/{m}'), m
        if e.get('replaces_existing'):
            i = idx[e['id']]; assert posts[i]['publish_at'] == x['publish_at']
            posts[i] = x; rep += 1
        else:
            assert e['id'] not in idx and f'"{e["id"]}"' not in pub and f'"{e["id"]}"' not in held, e['id']
            posts.append(x); add += 1

json.dump(Q, open(f'{R}/schedule/posts.json', 'w'), indent=2, ensure_ascii=False); open(f'{R}/schedule/posts.json','a').write('\n')
print('added', add, 'replaced', rep)
