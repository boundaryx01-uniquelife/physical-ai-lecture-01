from lib2 import *
S2={}
def wrap(w,h,b): return svg(w,h,DEFS+b)
# cover
b=bg(640,480,320,250,215)+circ(560,90,16,"#FFC857")+bulb(330,70,0.9)+sp(70,120,16)+sp(590,250,14,ORANGE)+sp(120,330,12,"#5B8DEF")
b+=kid2(205,440,2.1,arms="up")+robot2(445,440,2.1,arms="up")
b+=waves(335,300,24,"#E8742A",6,1,3)
S2['cover']=wrap(640,480,b)
# closing
b=bg(640,480,320,250,215)+circ(80,90,16,"#FFC857")+flag(560,360,150)+sp(520,90,15,ORANGE)+sp(100,250,13)+sp(310,70,12,"#5B8DEF")
b+=kid2(200,440,2.1,arms="wave")+robot2(400,440,2.1,arms="wave")
S2['closing']=wrap(640,480,b)
# literacy: kid with magnifier at bubble
b=bg(640,480,330,250,215)+sp(70,90,15)+sp(580,130,13,ORANGE)
b+=path("M270 70 H560 Q590 70 590 100 V190 Q590 220 560 220 H440 L400 262 L408 220 H270 Q240 220 240 190 V100 Q240 70 270 70 Z","#FFFFFF","#14213D",5)
b+=rect(275,100,140,12,"#DCE8FF",6)+rect(275,128,230,12,"#DCE8FF",6)+rect(275,156,190,12,"#DCE8FF",6)+path("M500 160 L520 180 L560 128","none","#2FA36B",9)
b+=robot2(520,445,1.45,arms="wave")
b+=kid2(150,445,2.0,arms=("down","hold"))
b+=line(215,300,290,235,"#14213D",10)+circ(310,215,42,"#FFFFFF88","#14213D",9)+shield(90,160,0.6,GREEN)
S2['literacy']=wrap(640,480,b)
# limits
b=bg(640,480,330,250,215)+sp(70,90,15)+sp(590,100,13,ORANGE)
rows=7
for r in range(rows):
    y=400-r*40; off=0 if r%2==0 else 32
    for c in range(0,6):
        x=250+c*64-off
        if x<246 or x+60>570: continue
        b+=rect(x,y,60,36,"#E8742A" if (r+c)%3 else "#F29A5E",6)
b+=line(520,420,452,110,"#14213D",10)+line(552,420,484,110,"#14213D",10)
for i in range(6):
    t=0.12+i*0.15; xa=520+(452-520)*t; ya=420+(110-420)*t; xb=552+(484-552)*t
    b+=line(xa,ya,xb,ya,"#14213D",7)
b+=flag(300,150,0)+rect(298,70,5,0,"#14213D")
b+=f'<polygon points="470,60 470,100 520,80" fill="#2FA36B"/>'+line(470,60,470,130,"#14213D",5)
b+=kid2(110,445,2.0,"url(#gG)","#14213D",arms=("down","fwd"),bag=False)+robot2(205,445,0.9,arms="up")
S2['limits']=wrap(640,480,b)
# senseq
b=bg(640,480,330,250,215)+sp(80,100,15)+sp(580,100,13,ORANGE)
b+=robot2(180,450,2.0,arms="down",confused=True)
b+=text(110,110,"?",60,"#E8742A")+text(250,80,"?",44,"#E8742A")
b+=waves(262,300,26,"#E8742A",6,1,2)
b+=rect(330,225,64,96,"#3D7BEA",10,"#14213D",5)
b+=kid2(480,450,2.0,"url(#gG)","#14213D",arms=("down","cover"),bag=False)
S2['senseq']=wrap(640,480,b)
