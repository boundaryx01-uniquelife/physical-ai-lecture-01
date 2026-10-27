from lib import *
S={}
# 1 cover (on navy)
def cover(wave=False):
    b=circ(380,310,285,"#1E3160")+circ(700,330,20,ORANGE)+circ(120,500,22,SKY)
    b+=gear(120,130,34,YEL,"#1E3160")+bulb(650,230,0.9)+spark(80,300,18)+spark(690,420,14)+spark(300,60,12,PEACH)
    b+=kid(215,540,2.5,ORANGE,"#0E1730","wave" if wave else "up")
    b+=robot(535,540,2.5,SKY,WHITE,"wave" if wave else "up","down")
    if not wave: b+=waves(425,330,28,PEACH,7,-1,3)
    return svg(760,600,b)
S['cover']=cover(); S['closing']=cover(True)
# 2 agenda
def agenda():
    pts=[(70,420),(210,395),(300,330),(190,270),(150,200),(270,150),(380,170),(440,90)]
    b=circ(260,250,215,PALE)
    b+=smooth(pts,WHITE,44)+smooth(pts,GRAY,30)+smooth(pts,WHITE,4,"2 18")
    nums=[(95,410),(250,375),(285,320),(185,265),(160,205),(270,155),(380,170)]
    for i,(x,y) in enumerate(nums):
        b+=circ(x,y,25,BLUE if i<6 else ORANGE)+text(x,y+10,str(i+1),28,WHITE)
    b+=flag(440,96,90)+robot(28,492,0.5,BLUE)+spark(430,300,13)+spark(60,220,12,ORANGE)
    return svg(520,500,b)
S['agenda']=agenda()
# 3 curriculum stairs
def curriculum():
    b=circ(280,70,40,YEL)+cloud(110,80,1.1)+cloud(370,140,0.8)
    cols=[PALE,"#B9D0FF",SKY,BLUE,NAVY]
    for i in range(5):
        x=40+i*98;h=60+i*54
        b+=rect(x,440-h,100,h,cols[i],8)+text(x+50,440-h+52,str(i+1),40,WHITE if i>=2 else BLUE)
    b+=flag(466,440-60-4*54,84)
    b+=kid(100,380,0.9,ORANGE,NAVY,"up")
    b+=robot(468,440-60-4*54,0.62,SKY)+spark(280,120,13,ORANGE)
    b+=rect(20,440,520,12,GRAY,6)
    return svg(560,470,b)
S['curriculum']=curriculum()
# 4 policy schools
def policy():
    b=rect(10,290,620,12,GRAY,6)
    xs=[90,230,380,540];ss=[0.55,0.75,0.95,1.2];cl=[PALE,"#B9D0FF",SKY,BLUE]
    for x,s,c in zip(xs,ss,cl): b+=school(x,290,s,c)
    pts=[(70,120),(220,95),(370,60),(540,24)]
    b+=smooth(pts,ORANGE,7,"1 16")+arrow(500,34,560,18,ORANGE,7,20)
    b+=spark(40,60,14)+spark(600,100,12,ORANGE)
    return svg(640,320,b)
S['policy']=policy()
# 5 literacy
def literacy():
    b=circ(280,230,205,PALE)
    b+=robot(150,400,1.5,BLUE)
    b+=path("M215 70 H455 Q485 70 485 100 V170 Q485 200 455 200 H340 L300 245 L305 200 H215 Q185 200 185 170 V100 Q185 70 215 70 Z",WHITE,NAVY,5)
    b+=text(335,160,"?!",64,ORANGE)
    b+=mag(380,250,1.0)
    b+=shield(455,370,1.0,GREEN)+spark(95,95,16)+spark(500,60,13,ORANGE)
    return svg(560,470,b)
S['literacy']=literacy()
# 6 physical loop (on navy band) -> white badges
def physical():
    b=""
    xs=[90,280,470]
    for x in xs: b+=circ(x,110,64,WHITE)
    b+=eyeico(90,110,1.0)+chip(280,110,1.0)+gear(470,110,34,ORANGE,WHITE)
    b+=arrow(158,110,208,110,PEACH,8,18)+arrow(348,110,398,110,PEACH,8,18)
    b+=path("M470 188 Q470 250 280 250 Q90 250 90 190","none",PEACH,7,extra='stroke-dasharray="2 14"')
    b+=arrow(96,214,90,192,PEACH,7,16)
    return svg(560,270,b)
S['physical']=physical()
# 7 why
def why():
    b=circ(260,220,200,PALE)
    b+=rect(120,310,280,18,ORANGE,6)+rect(150,328,12,70,NAVY,3)+rect(358,328,12,70,NAVY,3)
    b+=robot(260,310,0.85,SKY)
    b+=kid(90,400,1.6,ORANGE,NAVY,"fwd")+kid(430,400,1.6,BLUE,ORANGE,"fwd")
    b+=bulb(260,60,0.8)+spark(60,150,14)+spark(470,160,13,ORANGE)
    return svg(520,430,b)
S['why']=why()
# 8 vs A B C
def vsA():
    b=rect(10,200,340,12,GRAY,6)
    b+=rect(40,140,90,64,GRAY,14,NAVY,4)+circ(85,138,32,RED,NAVY,4)+circ(75,128,8,"#FF9A9A")
    b+=arrow(150,150,215,150,ORANGE,8,18)+bulb(285,128,1.0,True)
    b+=spark(300,40,10)
    return svg(360,230,b)
def vsB():
    b=rect(10,190,340,14,"#E8ECF5",7)
    b+=path("M20 175 Q110 120 190 170 T340 140","none",NAVY,16)
    b+=rect(120,125,86,36,BLUE,10)+circ(138,168,13,NAVY)+circ(190,168,13,NAVY)+circ(138,168,5,PALE)+circ(190,168,5,PALE)
    b+=f'<polygon points="163,161 150,186 176,186" fill="{YEL}"/>'
    b+=loop(163,95,50,ORANGE,7,200,340)+circ(163,126,7,YEL)
    return svg(360,230,b)
def vsC():
    b=rect(10,200,340,12,GRAY,6)
    b+=rect(14,70,70,52,NAVY,10)+circ(49,96,16,SKY)+circ(49,96,7,WHITE)+rect(28,60,22,12,NAVY,3)
    cols=[[(135,70),(135,110),(135,150)],[(190,60),(190,100),(190,140),(190,180)],[(245,90),(245,130)]]
    for a,bb in zip(cols,cols[1:]):
        for p in a:
            for q in bb: b+=line(p[0],p[1],q[0],q[1],"#B9C6E4",2.5)
    for c in cols:
        for p in c: b+=circ(p[0],p[1],11,BLUE if c!=cols[2] else ORANGE)
    b+=line(84,96,120,100,NAVY,5)+line(258,110,290,150,NAVY,12)+line(290,150,330,140,NAVY,12)+circ(290,150,10,YEL)+circ(332,140,8,ORANGE)
    b+=rect(274,185,60,15,BLUE,5)
    b+=loop(190,205,95,ORANGE,6,205,335)
    return svg(360,230,b)
S['vsA']=vsA();S['vsB']=vsB();S['vsC']=vsC()
# 9 limits
def limits():
    b=circ(260,220,200,PALE)
    rows=6
    for r in range(rows):
        y=330-r*38
        off=0 if r%2==0 else 30
        for c in range(-1,4):
            x=130+c*60+off
            if x<115 or x+58>395: continue
            b+=rect(x,y,56,34,ORANGE if (r+c)%3 else "#F29A5E",5)
    b+=line(398,380,330,120,NAVY,10)+line(430,380,362,120,NAVY,10)
    for i in range(6):
        t=i/5.0
        b+=line(398+(330-398)*(0.15+t*0.8)+0,380+(120-380)*(0.15+t*0.8),430+(362-430)*(0.15+t*0.8),380+(120-380)*(0.15+t*0.8),NAVY,7)
    b+=flag(150,100,76,GREEN)
    b+=kid(70,400,1.35,GREEN,NAVY,"up")
    b+=spark(470,90,14)+spark(60,150,12,ORANGE)
    return svg(520,430,b)
S['limits']=limits()
# 10 overseas globe
def overseas():
    b=circ(280,215,168,BLUE)
    b+=path("M150 160 Q190 110 240 140 Q270 170 230 200 Q190 220 150 200 Z",GREEN)
    b+=path("M300 120 Q360 100 400 150 Q410 200 360 210 Q320 190 300 150 Z",GREEN)
    b+=path("M230 270 Q290 250 330 290 Q320 340 270 350 Q230 320 230 270 Z",GREEN)
    b+=path("M120 215 Q280 160 440 215","none","#FFFFFF55",4)+path("M120 215 Q280 270 440 215","none","#FFFFFF55",4)
    b+=ell(280,215,230,60,"none",ORANGE,5,extra='transform="rotate(-18 280 215)"')
    # book on orbit
    b+=rect(444,128,58,42,WHITE,6,NAVY,4)+line(473,128,473,170,NAVY,3)+rect(444,170,58,6,NAVY,2)
    b+=pin(190,120,0.9,ORANGE)+pin(350,270,0.9,YEL)+pin(400,180,0.9,RED)
    b+=spark(60,80,15)+spark(500,320,13,ORANGE)
    return svg(560,430,b)
S['overseas']=overseas()
# 11 overseas2: generic board
def board():
    b=rect(20,90,260,200,"#222B3F",24,NAVY,4)
    for i in range(10): b+=rect(40+i*22,284,14,20,YEL,3)
    for r in range(5):
        for c in range(5):
            on=(r,c) in [(0,1),(0,3),(2,0),(3,1),(3,2),(3,3),(2,4)]
            b+=circ(100+c*30,130+r*28,9,ORANGE if on else "#3C486A")
    b+=circ(60,240,16,"#5B6B91")+circ(240,240,16,"#5B6B91")
    # waveform card
    b+=rect(320,60,260,130,WHITE,16,GRAY,3)
    b+=path("M338 140 Q360 80 382 140 T426 140 T470 140 T514 130 T560 140","none",BLUE,6)
    b+=rect(320,210,260,110,WHITE,16,GRAY,3)
    for i,(c,h) in enumerate([(SKY,50),(SKY,72),(ORANGE,86)]): b+=rect(350+i*70,300-h,50,h,c,6)
    b+=arrow(282,190,318,150,NAVY,6,14)+arrow(282,220,318,250,NAVY,6,14)
    b+=shield(60,70,0.5,GREEN)+spark(600,360,12)
    return svg(620,380,b)
S['overseas2']=board()
# 12 naesung
def naesung():
    b=circ(230,160,140,PALE)
    b+=school(180,290,1.4,SKY)
    b+=robot(350,290,0.8,BLUE,WHITE,"wave")
    b+=rect(10,290,440,12,GRAY,6)+circ(60,215,32,GREEN)+rect(56,232,8,58,"#8A5A3A",2)
    b+=spark(400,60,13,ORANGE)
    return svg(460,320,b)
S['naesung']=naesung()
# 13 center: idea -> blueprint -> prototype
def center():
    b=bulb(70,100,1.2)
    b+=arrow(140,110,190,110,NAVY,7,16)
    b+=rect(200,40,150,150,"#1D5BD6",10,NAVY,4)
    for i in range(1,4): b+=line(212,40+i*37,338,40+i*37,"#5B8DEF",2)+line(200+i*37,52,200+i*37,178,"#5B8DEF",2)
    b+=rect(240,80,70,40,"none",4,WHITE,4)+circ(250,130,9,"none",WHITE,4)+circ(300,130,9,"none",WHITE,4)
    b+=arrow(360,110,410,110,NAVY,7,16)
    b+=rect(420,80,86,40,ORANGE,10)+circ(442,128,14,NAVY)+circ(486,128,14,NAVY)+circ(442,128,5,PALE)+circ(486,128,5,PALE)+rect(478,64,26,18,YEL,4)
    b+=rect(10,230,500,12,GRAY,6)
    
    return svg(520,260,b)
S['center']=center()
# 14 implications: signpost
def impl():
    b=circ(280,230,200,PALE)
    b+=rect(268,60,24,380,NAVY,6)
    cols=[BLUE,ORANGE,GREEN,SKY]
    for i,c in enumerate(cols):
        y=80+i*84
        if i%2==0: b+=f'<polygon points="292,{y} 440,{y} 480,{y+30} 440,{y+60} 292,{y+60}" fill="{c}"/>'+circ(330,y+30,12,WHITE)
        else: b+=f'<polygon points="268,{y} 120,{y} 80,{y+30} 120,{y+60} 268,{y+60}" fill="{c}"/>'+circ(230,y+30,12,WHITE)
    b+=ell(280,440,90,12,"#00000018")+robot(430,440,0.7,BLUE,WHITE,"up")+spark(70,60,14)+spark(500,360,12,ORANGE)
    return svg(560,470,b)
S['impl']=impl()
# 15 start: 3 steps
def start():
    b=circ(300,150,140,PALE)
    st=[(110,230),(300,190),(490,140)]
    for i,(x,y) in enumerate(st):
        b+=ell(x,y+8,80,20,"#00000018")+ell(x,y,76,24,GRAY,NAVY,4)+ell(x,y-6,76,22,WHITE if i<2 else PEACH,NAVY,4)
        b+=text(x,y+8,str(i+1),34,BLUE if i<2 else ORANGE)
    b+=arrow(180,205,230,190,ORANGE,6,14)+arrow(372,170,422,152,ORANGE,6,14)
    b+=kid(110,215,0.75,ORANGE,NAVY,"fwd")
    b+=flag(560,150,80)+robot(520,108,0.5,BLUE,WHITE,"wave")
    b+=spark(300,40,13)
    return svg(620,270,b)
S['start']=start()
# 16 safety
def safety():
    b=circ(230,190,165,PALE)
    b+=shield(120,170,1.6,GREEN)
    oct_=[(0.38,0),(0.62,0),(1,0.38),(1,0.62),(0.62,1),(0.38,1),(0,0.62),(0,0.38)]
    X,Y,W=240,130,150
    pts=" ".join(f"{n(X+a*W)},{n(Y+b_*W)}" for a,b_ in oct_)
    b+=f'<polygon points="{pts}" fill="{RED}" stroke="{WHITE}" stroke-width="8"/>'
    b+=rect(X+34,Y+W/2-12,W-68,24,WHITE,6)
    b+=spark(380,70,13,ORANGE)+spark(70,60,12)
    return svg(460,370,b)
S['safety']=safety()
def senseq():
    b=circ(260,215,200,PALE)
    b+=robot(120,400,1.7,BLUE,WHITE,"down","down")
    b+=waves(215,255,34,ORANGE,7,1,3)
    b+=rect(300,170,70,100,WHITE,10,NAVY,5)+text(335,242,"?",62,ORANGE)
    b+=kid(430,400,1.6,GREEN,NAVY,"fwd")
    b+=spark(70,90,15)+spark(480,90,13,ORANGE)
    return svg(540,430,b)
S['senseq']=senseq()
