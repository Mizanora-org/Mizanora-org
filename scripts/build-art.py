"""Generate dependency-free, GitHub-friendly animated brand artwork."""
from pathlib import Path
from html import escape
ROOT = Path(__file__).resolve().parents[1]

def text(x,y,s,size=18,color='#a9c7bf',extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" {extra}>{escape(s)}</text>'

def svg(name,height,body,label):
    data=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(label)}</title><desc id="desc">Mizanora. Balance in purpose. Light in progress. Decorative motion respects reduced-motion settings.</desc>
<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#061b19"/><stop offset="1" stop-color="#103c32"/></linearGradient><linearGradient id="line"><stop stop-color="#46dfaa"/><stop offset="1" stop-color="#e6c77d"/></linearGradient><pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse"><path d="M48 0H0V48" fill="none" stroke="#84d3b6" stroke-opacity=".055"/></pattern></defs>
<style>
text{{font-family:Segoe UI,Arial,sans-serif}}.orbit{{transform-origin:1000px 205px;animation:rotate 40s linear infinite}}.pulse{{animation:pulse 4s ease-in-out infinite}}.flow{{stroke-dasharray:8 14;animation:flow 8s linear infinite}}.rise{{animation:rise 6s ease-in-out infinite}}@keyframes rotate{{to{{transform:rotate(360deg)}}}}@keyframes pulse{{50%{{opacity:.4}}}}@keyframes flow{{to{{stroke-dashoffset:-220}}}}@keyframes rise{{50%{{transform:translateY(-8px)}}}}@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>
<rect width="1200" height="{height}" rx="24" fill="url(#bg)"/><rect width="1200" height="{height}" rx="24" fill="url(#grid)"/><rect x="1" y="1" width="1198" height="{height-2}" rx="23" fill="none" stroke="#81c7ac" stroke-opacity=".2"/>
{body}</svg>'''
    for directory in ('assets', 'profile/assets'):
        (ROOT/directory).mkdir(parents=True, exist_ok=True)
        (ROOT/directory/name).write_text(data+'\n')

hero=text(60,60,'M I Z A N O R A   /   P A K I S T A N',14,'#e6c77d')
hero+=text(60,153,'Purpose-led.',68,'#f1fbf7','font-weight="700"')+text(60,228,'Possibility-built.',68,'#f1fbf7','font-weight="700"')
hero+=text(63,285,'Digital infrastructure. Ethical commerce. Thoughtful AI.',22)
hero+=text(63,330,'Rooted in Mizan. Inspired by Noor.',20,'#e6c77d')
hero+='<path d="M64 369H750" stroke="url(#line)" class="flow"/>'
hero+=text(63,405,'BALANCE IN PURPOSE  /  LIGHT IN PROGRESS',13,'#89b7a8','letter-spacing="2"')
hero+='''<circle cx="1000" cy="205" r="134" fill="#0a2a24" stroke="#366b54"/><g class="orbit" fill="none" stroke="#e6c77d"><circle cx="1000" cy="205" r="116" stroke-dasharray="2 18"/><path d="M1000 67V89M1000 321V343M862 205H884M1116 205H1138"/></g><g class="rise"><path d="M1034 130a84 84 0 1 0 30 129 71 71 0 1 1-30-129" fill="#e6c77d"/><path d="m1039 168 8 20 21 2-16 14 5 21-18-11-18 11 5-21-16-14 21-2Z" fill="#62dfaf"/></g><circle class="pulse" cx="1110" cy="106" r="5" fill="#62dfaf"/>'''
svg('hero.svg',445,hero,'Mizanora — purpose-led, possibility-built')

body=text(48,49,'THE MIZANORA ECOSYSTEM',15,'#e6c77d','letter-spacing="3"')+text(48,87,'One platform. Connected possibilities.',30,'#f1fbf7','font-weight="600"')
for i,(n,title,sub,detail) in enumerate([('01','Commerce','Shop Smart. Shop Halal.','Products / COD / customer support'),('02','Noor AI','Assistance that feels closer.','Shopping help / Urdu & English voice'),('03','Community','Useful beyond the checkout.','Live channel / tools / worker program')]):
    x=48+i*374
    body+=f'<rect x="{x}" y="120" width="356" height="176" rx="16" fill="#0b2a24" stroke="#32604e"/>'
    body+=text(x+22,153,n,14,'#e6c77d')+text(x+22,192,title,28,'#f1fbf7','font-weight="600"')+text(x+22,231,sub,17)+text(x+22,266,detail,14)
    body+=f'<path class="flow" d="M{x+22} 283H{x+332}" stroke="#62dfaf" opacity=".5"/>'
svg('ecosystem.svg',326,body,'Mizanora ecosystem: commerce, Noor AI and community')
body=text(48,49,'THE PRINCIPLES BEHIND THE PLATFORM',14,'#e6c77d','letter-spacing="2"')
for i,(title,sub) in enumerate([('MIZAN','Balance, fairness & responsibility'),('NOOR','Clarity, knowledge & illumination'),('IMPACT','Useful technology for real people')]):
    x=48+374*i
    body+=f'<circle cx="{x+8}" cy="88" r="5" fill="#62dfaf" class="pulse" style="animation-delay:{i}s"/>'
    body+=text(x,132,title,27,'#f1fbf7','font-weight="600"')+text(x,171,sub,17)
svg('principles.svg',210,body,'Mizanora principles: balance, illumination and impact')
body=text(600,58,'BUILD WITH PURPOSE. GROW WITH MIZANORA.',27,'#f1fbf7','text-anchor="middle" font-weight="600"')+text(600,96,'From Pakistan, with a vision for meaningful digital progress.',18,'#a9c7bf','text-anchor="middle"')+'<path class="flow" d="M225 124H975" stroke="url(#line)"/>'
svg('footer.svg',155,body,'Build with purpose. Grow with Mizanora.')
print('Generated 4 animated SVG assets.')
