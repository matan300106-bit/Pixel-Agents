import numpy as np, json, soundfile as sf
SR=48000; DUR=18.8; N=int(SR*DUR); t=np.arange(N)/SR
mus=np.zeros(N); sfx=np.zeros(N)
def env(n,a=.005,r=.3):
    x=np.arange(n)/SR; return np.minimum(1,x/a)*np.exp(-x/r)
def add(buf,s,sig,g=1):
    i=int(s*SR); j=min(N,i+len(sig)); buf[i:j]+=g*sig[:j-i]
def tone(f,d,r=.4,a=.005,harm=(1,.5,.25)):
    x=np.arange(int(d*SR))/SR; s=sum(h*np.sin(2*np.pi*f*(k+1)*x) for k,h in enumerate(harm)); return s*env(len(x),a,r)
def mid(n): return 440*2**((n-69)/12)
bpm=100; beat=60/bpm
# chords (I vi IV V) C Am F G, pluck arps
prog=[[60,64,67,72],[57,60,64,69],[53,57,60,65],[55,59,62,67]]
b=0; T=0.0
while T<DUR:
    ch=prog[(b//4)%4]; n=ch[b%4] + (12 if b%8>=4 else 0)
    quiet = 6.6<=T<7.4 or 14.65<=T<15.3
    if not quiet: add(mus,T,tone(mid(n),1.2,.35),.16)
    if b%4==0 and not quiet: add(mus,T,tone(mid(ch[0]-24),2.4,.9,.02,(1,.3)),.22)
    b+=1; T=b*beat/2
# sad single note in the dip
add(mus,6.65,tone(mid(57),1.2,.6,.02,(1,.2)),.25)
# swell on goal: pad chord
for n in [60,64,67,72,76]:
    x=np.arange(int(1.85*SR))/SR; s=np.sin(2*np.pi*mid(n)*x)*np.minimum(1,x/.4)*np.minimum(1,(1.85-x)/.1); add(mus,12.8,s,.09)
# resolve note at end into loop
add(mus,18.1,tone(mid(72),1.0,.5),.18)
def pop(f0=500,f1=1400,d=.12):
    x=np.arange(int(d*SR))/SR; f=f0+(f1-f0)*x/d; return np.sin(2*np.pi*np.cumsum(f)/SR)*env(len(x),.002,.05)
def noise(d,lp=.2):
    n=np.random.randn(int(d*SR)); y=np.zeros_like(n); a=lp
    for i in range(1,len(n)): y[i]=y[i-1]+a*(n[i]-y[i-1])
    return y
rng=np.random.default_rng(1)
add(sfx,0.25,pop(),.5)
w=noise(.9,.08); x=np.arange(len(w))/SR; add(sfx,0.95,w*np.sin(np.pi*x/.9)**2,1.4)        # whoosh reveal
w=noise(.6,.1); x=np.arange(len(w))/SR; add(sfx,7.35,w*np.sin(np.pi*x/.6)**2,1.4)         # dive whoosh
add(sfx,4.6,np.concatenate([tone(1200+300*rng.random(),.08,.03,.001,(1,)) for _ in range(10)]),.12)  # water drips
for k in range(6): add(sfx,5.85+k*.11,noise(.05,.6)*env(int(.05*SR),.001,.015),.5)        # crunch
for s,f in [(9.75,600),(10.65,700),(11.55,800)]:
    add(sfx,s,pop(f,f*2.4,.14),1.1); add(sfx,s+.08,tone(f*2,.6,.25,.003,(1,.3)),.3)          # pop + chime
for k,n in enumerate([84,88,91,96]): add(sfx,12.82+k*.06,tone(mid(n),.8,.3,.002,(1,)),.12)  # sparkle
add(sfx,14.65,tone(110,.5,.15,.002,(1,.6,.3)),.35)                                          # thud back to reality
add(sfx,16.6,pop(700,1600,.12),.5)
# voice
L=json.load(open('/tmp/tts/timeline.json')); voc=np.zeros(N)
for l in L:
    a,sr=sf.read(f"/tmp/tts/t_l{l['i']:02d}.wav"); add(voc,l['s'],a,1.0)
# duck music under voice
vm=np.convolve(np.abs(voc),np.ones(2400)/2400,'same'); duck=1-0.7*np.clip(vm*12,0,1)
duck=np.convolve(duck,np.ones(4800)/4800,'same')
mix=voc*1.0+0.6*mus*duck+sfx*.8
mix*=0.89/np.max(np.abs(mix))
fade=np.ones(N); fade[:int(.02*SR)]=np.linspace(0,1,int(.02*SR)); fade[-int(.05*SR):]=np.linspace(1,0,int(.05*SR))
sf.write('/tmp/ct/v/mix.wav',mix*fade,SR)
print('peak ok', np.max(np.abs(mix)))
