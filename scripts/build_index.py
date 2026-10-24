"""Build a portable course index from catalog.json. Python standard library only."""
from pathlib import Path
import json,html,re

ROOT=Path(__file__).resolve().parents[1]

def safe_path(value):
    if not re.fullmatch(r'[A-Za-z0-9_./-]+',value) or '..' in Path(value).parts or value.startswith('/'):
        raise ValueError('Catalog links must be safe relative paths: '+value)
    if not (ROOT/value).is_file():raise ValueError('Missing course resource: '+value)
    return value

def e(value):return html.escape(str(value),quote=True)

def build():
    catalog=json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'));cards=[];track_names={t['id']:t['title'] for t in catalog['tracks']}
    ids=set()
    for c in catalog['courses']:
        assert re.fullmatch('[a-z0-9-]+',c['id']) and c['id'] not in ids
        ids.add(c['id']);assert all(t in track_names for t in c.get('trackIds',[]))
        lab=safe_path(c['lab']);notes=[];downloads=[]
        for n in c['notes']:
            actions=''.join(f'<a href="{e(safe_path(n[k]))}">{label}</a>' for k,label in [('html','Read HTML'),('pdf','View PDF'),('text','Text')])
            recommend='<span class="recommended">Start here</span>' if n.get('recommended') else ''
            notes.append(f'<article class="note-card"><div class="note-meta"><span>{e(n["pages"])} A4 pages</span>{recommend}</div><h4>{e(n["title"])}</h4><p>{e(n["description"])}</p><div class="note-actions">{actions}</div></article>')
        for d in c['downloads']:
            attribute=f' download="{e(d["filename"])}"' if d.get('filename') else ' download'
            downloads.append(f'<a class="download-row" href="{e(safe_path(d["path"]))}"{attribute}><span><strong>{e(d["title"])}</strong><small>{e(d["description"])}</small></span><span aria-hidden="true">↓</span></a>')
        read_notes=f'<a class="secondary-route" href="{e(safe_path(c["notes"][0]["html"]))}">Read notes</a>' if c['notes'] else ''
        chips=''.join('<li>'+e(t)+'</li>' for t in c['topics'])
        tracks=' '.join(c.get('trackIds',[]));track_labels=' · '.join(track_names[t] for t in c.get('trackIds',[]))
        search=' '.join([c['title'],c['shortTitle'],c['language'],track_labels,*c['topics']])
        cards.append(f'''<section class="course" id="{e(c['id'])}" data-search="{e(search.lower())}" data-tracks="{e(tracks)}" aria-labelledby="{e(c['id'])}-title">
          <div class="course-main"><div class="course-copy"><div class="eyebrow">INTERACTIVE COURSE <span>· {e(c['language'])}</span></div><h2 id="{e(c['id'])}-title">{e(c['title'])}</h2><p class="course-hook">{e(c['description'])}</p><ul class="chips" aria-label="Topics">{chips}</ul><div class="course-stats"><span><b>{e(c['lessonCount'])}</b> visual lessons</span><span><b>{e(c['questionCount'])}</b> practice MCQs</span></div><div class="course-routes"><a class="primary" href="{e(lab)}#practice">Practice MCQs <span aria-hidden="true">&rarr;</span></a><a class="secondary-route" href="{e(lab)}#course">Explore lessons</a>{read_notes}</div></div><div class="course-art" aria-hidden="true">{MEMORY}</div></div>
          <div class="resources"><div class="resource-heading"><div><div class="eyebrow">KEEP IT HANDY</div><h3>Notes for the way you study</h3></div><p>Read on screen or take an A4 copy.</p></div><div class="note-grid">{''.join(notes)}</div><details class="downloads"><summary>Offline copies & downloads <span aria-hidden="true">+</span></summary><div>{''.join(downloads)}</div></details></div></section>''')
    options='<option value="">All tracks</option>'+''.join(f'<option value="{e(t["id"])}">{e(t["title"])}</option>' for t in catalog['tracks'])
    track_control=f'<label class="track-control">Track<select id="track">{options}</select></label>' if catalog['tracks'] else ''
    template=(ROOT/'site/hub.template.html').read_text(encoding='utf-8')
    values={'TITLE':e(catalog['title']),'DESCRIPTION':e(catalog['description']),'CARDS':'\n'.join(cards),'TRACKS':track_control,'COUNT':str(len(cards)),'COUNT_LABEL':'course' if len(cards)==1 else 'courses','APPEARANCE_CSS':(ROOT/'site/appearance.css').read_text(encoding='utf-8'),'APPEARANCE_JS':(ROOT/'site/appearance.js').read_text(encoding='utf-8')}
    for key,value in values.items():template=template.replace('{{'+key+'}}',value)
    assert '{{' not in template
    (ROOT/'index.html').write_text(template,encoding='utf-8')
    print(f'Built {len(cards)} course card(s); all catalog links exist.')

MEMORY='''<svg viewBox="0 0 290 310" role="presentation"><rect x="22" y="12" width="250" height="286" rx="20" fill="#eef7f4"/><text x="48" y="46" fill="#16685f" font-size="12" font-family="sans-serif" font-weight="700" letter-spacing="1">FOLLOW THE MEMORY</text><text x="44" y="108" fill="#778b8a" font-size="13" font-family="monospace">S0</text><rect x="75" y="70" width="145" height="67" rx="5" fill="white" stroke="#aacdc4"/><text x="89" y="93" fill="#53676b" font-size="13" font-family="monospace">x : int</text><text x="147" y="123" text-anchor="middle" fill="#123c3a" font-size="28" font-family="sans-serif" font-weight="700">7</text><text x="44" y="208" fill="#778b8a" font-size="13" font-family="monospace">S1</text><rect x="75" y="170" width="145" height="67" rx="5" fill="#fff2dd" stroke="#dec4a0"/><text x="89" y="193" fill="#7d6649" font-size="13" font-family="monospace">p : int*</text><text x="147" y="223" text-anchor="middle" fill="#a65c1e" font-size="25" font-family="sans-serif" font-weight="700">S0</text><path d="M220 204 H244 V104 H226" fill="none" stroke="#168678" stroke-width="2.5"/><polygon points="220,104 229,99 229,109" fill="#168678"/><text x="147" y="271" text-anchor="middle" fill="#16685f" font-size="14" font-family="sans-serif">An address. A route. A value.</text></svg>'''

if __name__=='__main__':build()
