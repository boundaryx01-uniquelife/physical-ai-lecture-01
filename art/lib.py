import math
NAVY="#14213D";BLUE="#0B4FB3";SKY="#5B8DEF";PALE="#DCE8FF";ORANGE="#E8742A";PEACH="#FFD2B3"
YEL="#FFC857";GREEN="#2FA36B";GRAY="#D3DBEA";WHITE="#FFFFFF";SKIN="#F5C9A6";RED="#D64545";INK="#14213D"
def n(v): return f"{v:.1f}".rstrip('0').rstrip('.')
def svg(w,h,body): return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'
def rect(x,y,w,h,fill,rx=0,stroke=None,sw=0,extra=""):
    st=f' stroke="{stroke}" stroke-width="{n(sw)}"' if stroke else ''
    return f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="{n(rx)}" fill="{fill}"{st} {extra}/>'
def circ(cx,cy,r,fill,stroke=None,sw=0):
    st=f' stroke="{stroke}" stroke-width="{n(sw)}"' if stroke else ''
    return f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}" fill="{fill}"{st}/>'
def line(x1,y1,x2,y2,color,w,cap="round",dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{n(x1)}" y1="{n(y1)}" x2="{n(x2)}" y2="{n(y2)}" stroke="{color}" stroke-width="{n(w)}" stroke-linecap="{cap}"{d}/>'
def path(d,fill="none",stroke=None,sw=0,cap="round",extra=""):
    st=f' stroke="{stroke}" stroke-width="{n(sw)}" stroke-linecap="{cap}" stroke-linejoin="round"' if stroke else ''
    return f'<path d="{d}" fill="{fill}"{st} {extra}/>'
def ell(cx,cy,rx,ry,fill,stroke=None,sw=0,extra=""):
    st=f' stroke="{stroke}" stroke-width="{n(sw)}"' if stroke else ''
    return f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(rx)}" ry="{n(ry)}" fill="{fill}"{st} {extra}/>'
def text(x,y,t,size,fill,weight=900,anchor="middle"):
    return f'<text x="{n(x)}" y="{n(y)}" font-family="Noto Sans KR, Arial, sans-serif" font-size="{n(size)}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{t}</text>'
def arrow(x1,y1,x2,y2,color,w=8,head=18):
    a=math.atan2(y2-y1,x2-x1)
    bx,by=x2-head*math.cos(a),y2-head*math.sin(a)
    p1=(x2,y2);p2=(bx+head*0.6*math.sin(a),by-head*0.6*math.cos(a));p3=(bx-head*0.6*math.sin(a),by+head*0.6*math.cos(a))
    return line(x1,y1,bx,by,color,w)+f'<polygon points="{n(p1[0])},{n(p1[1])} {n(p2[0])},{n(p2[1])} {n(p3[0])},{n(p3[1])}" fill="{color}" stroke="{color}" stroke-width="2" stroke-linejoin="round"/>'
def smooth(points,stroke,sw,dash=None):
    d=f"M{n(points[0][0])} {n(points[0][1])}"
    for i in range(1,len(points)-1):
        mx=(points[i][0]+points[i+1][0])/2;my=(points[i][1]+points[i+1][1])/2
        d+=f" Q{n(points[i][0])} {n(points[i][1])} {n(mx)} {n(my)}"
    d+=f" L{n(points[-1][0])} {n(points[-1][1])}"
    ex=f'stroke-dasharray="{dash}"' if dash else ''
    return path(d,"none",stroke,sw,extra=ex)
def robot(cx,by,s=1,body=BLUE,face=WHITE,right="down",left="down",eye=NAVY):
    g=""
    g+=ell(cx,by+2*s,46*s,8*s,"#00000018")
    # arms
    def arm(side,mode):
        x0=cx+side*38*s;y0=by-88*s
        if mode=="up": x1,y1=cx+side*66*s,by-128*s
        elif mode=="wave": x1,y1=cx+side*70*s,by-112*s
        elif mode=="fwd": x1,y1=cx+side*72*s,by-78*s
        else: x1,y1=cx+side*60*s,by-56*s
        return line(x0,y0,x1,y1,body,13*s)+circ(x1,y1,8*s,YEL)
    g+=arm(-1,left)+arm(1,right)
    g+=rect(cx-38*s,by-100*s,76*s,64*s,body,12*s)
    g+=circ(cx,by-68*s,10*s,YEL)+circ(cx,by-68*s,4*s,WHITE)
    g+=rect(cx-10*s,by-110*s,20*s,14*s,NAVY,4*s)
    g+=rect(cx-35*s,by-170*s,70*s,58*s,face,18*s,NAVY,4*s)
    g+=circ(cx-14*s,by-143*s,8*s,eye)+circ(cx+14*s,by-143*s,8*s,eye)
    g+=circ(cx-12*s,by-146*s,2.6*s,WHITE)+circ(cx+16*s,by-146*s,2.6*s,WHITE)
    g+=path(f"M{n(cx-9*s)} {n(by-126*s)} Q{n(cx)} {n(by-118*s)} {n(cx+9*s)} {n(by-126*s)}","none",NAVY,3.5*s)
    g+=line(cx,by-170*s,cx,by-188*s,NAVY,4*s)+circ(cx,by-192*s,7*s,ORANGE)
    g+=circ(cx-22*s,by-20*s,15*s,NAVY)+circ(cx+22*s,by-20*s,15*s,NAVY)+circ(cx-22*s,by-20*s,5*s,PALE)+circ(cx+22*s,by-20*s,5*s,PALE)
    return g
def kid(cx,by,s=1,shirt=ORANGE,hair=NAVY,arms="up"):
    g=ell(cx,by+2*s,36*s,7*s,"#00000018")
    g+=rect(cx-17*s,by-42*s,14*s,42*s,NAVY,5*s)+rect(cx+3*s,by-42*s,14*s,42*s,NAVY,5*s)
    g+=rect(cx-20*s,by+-6*s,18*s,8*s,"#2B3A5E",4*s)+rect(cx+2*s,by-6*s,18*s,8*s,"#2B3A5E",4*s)
    def arm(side,mode):
        x0=cx+side*24*s;y0=by-92*s
        if mode=="up": x1,y1=cx+side*52*s,by-128*s
        elif mode=="wave": x1,y1=cx+side*56*s,by-118*s
        elif mode=="fwd": x1,y1=cx+side*50*s,by-80*s
        else: x1,y1=cx+side*34*s,by-52*s
        return line(x0,y0,x1,y1,shirt,12*s)+circ(x1,y1,7*s,SKIN)
    g+=arm(-1,arms if arms!="wave" else "down")+arm(1,arms)
    g+=rect(cx-25*s,by-102*s,50*s,66*s,shirt,16*s)
    g+=circ(cx,by-126*s,23*s,SKIN)
    g+=path(f"M{n(cx-23*s)} {n(by-128*s)} A{n(23*s)} {n(23*s)} 0 0 1 {n(cx+23*s)} {n(by-128*s)} Q{n(cx)} {n(by-142*s)} {n(cx-23*s)} {n(by-128*s)} Z",hair)
    g+=circ(cx-8*s,by-122*s,2.8*s,NAVY)+circ(cx+8*s,by-122*s,2.8*s,NAVY)
    g+=path(f"M{n(cx-6*s)} {n(by-113*s)} Q{n(cx)} {n(by-107*s)} {n(cx+6*s)} {n(by-113*s)}","none",NAVY,2.6*s)
    return g
def waves(x,y,r,color,sw=6,direction=1,k=3):
    g=""
    for i in range(1,k+1):
        ri=r*i
        g+=path(f"M{n(x+direction*ri*0.5)} {n(y-ri*0.85)} A{n(ri)} {n(ri)} 0 0 {1 if direction==1 else 0} {n(x+direction*ri*0.5)} {n(y+ri*0.85)}","none",color,sw)
    return g
def gear(cx,cy,r,color,hole=PALE):
    g=""
    for i in range(8):
        a=i*45
        g+=f'<rect x="{n(cx-r*0.2)}" y="{n(cy-r*1.2)}" width="{n(r*0.4)}" height="{n(r*0.5)}" rx="{n(r*0.08)}" fill="{color}" transform="rotate({a} {n(cx)} {n(cy)})"/>'
    g+=circ(cx,cy,r,color)+circ(cx,cy,r*0.42,hole)
    return g
def bulb(cx,cy,s=1,on=True):
    c=YEL if on else GRAY
    g=""
    if on:
        for i in range(8):
            a=math.radians(i*45-90)
            g+=line(cx+math.cos(a)*40*s,cy+math.sin(a)*40*s,cx+math.cos(a)*52*s,cy+math.sin(a)*52*s,YEL,5*s)
    g+=circ(cx,cy,28*s,c)+rect(cx-14*s,cy+22*s,28*s,22*s,GRAY,6*s,NAVY,3*s)+line(cx-9*s,cy+32*s,cx+9*s,cy+32*s,NAVY,3*s)
    g+=path(f"M{n(cx-9*s)} {n(cy+4*s)} Q{n(cx)} {n(cy-10*s)} {n(cx+9*s)} {n(cy+4*s)}","none",WHITE,4*s)
    return g
def eyeico(cx,cy,s=1,col=BLUE):
    return ell(cx,cy,34*s,22*s,WHITE,col,5*s)+circ(cx,cy,13*s,col)+circ(cx,cy,5.5*s,NAVY)+circ(cx+4*s,cy-4*s,3*s,WHITE)
def chip(cx,cy,s=1,col=BLUE):
    g=""
    for i in range(4):
        o=(-18+i*12)*s
        g+=line(cx+o,cy-36*s,cx+o,cy-26*s,col,4*s)+line(cx+o,cy+26*s,cx+o,cy+36*s,col,4*s)+line(cx-36*s,cy+o,cx-26*s,cy+o,col,4*s)+line(cx+26*s,cy+o,cx+36*s,cy+o,col,4*s)
    g+=rect(cx-26*s,cy-26*s,52*s,52*s,col,8*s)+rect(cx-14*s,cy-14*s,28*s,28*s,WHITE,5*s)+circ(cx,cy,5*s,ORANGE)
    return g
def hand(cx,cy,s=1,col=ORANGE):
    g=line(cx-24*s,cy+28*s,cx-4*s,cy-4*s,col,12*s)+line(cx+24*s,cy+28*s,cx+4*s,cy-4*s,col,12*s)
    g+=path(f"M{n(cx-18*s)} {n(cy-26*s)} L{n(cx-4*s)} {n(cy-4*s)} L{n(cx+18*s)} {n(cy-26*s)}","none",col,12*s)
    g+=circ(cx-4*s,cy-4*s,10*s,NAVY)+circ(cx-4*s,cy-4*s,3.5*s,WHITE)
    return g
def loop(cx,cy,r,color,sw=7,a0=200,a1=340):
    x0=cx+r*math.cos(math.radians(a0));y0=cy+r*math.sin(math.radians(a0))
    x1=cx+r*math.cos(math.radians(a1));y1=cy+r*math.sin(math.radians(a1))
    d=f"M{n(x0)} {n(y0)} A{n(r)} {n(r)} 0 0 1 {n(x1)} {n(y1)}"
    ang=math.radians(a1+90)
    hx,hy=x1,y1
    p=[(hx+16*math.cos(ang),hy+16*math.sin(ang)),(hx+11*math.cos(ang+2.4),hy+11*math.sin(ang+2.4)),(hx+11*math.cos(ang-2.4),hy+11*math.sin(ang-2.4))]
    return path(d,"none",color,sw)+f'<polygon points="{" ".join(n(a)+","+n(b) for a,b in p)}" fill="{color}"/>'
def shield(cx,cy,s=1,col=GREEN):
    d=f"M{n(cx)} {n(cy-54*s)} L{n(cx+44*s)} {n(cy-38*s)} L{n(cx+44*s)} {n(cy+4*s)} Q{n(cx+44*s)} {n(cy+38*s)} {n(cx)} {n(cy+58*s)} Q{n(cx-44*s)} {n(cy+38*s)} {n(cx-44*s)} {n(cy+4*s)} L{n(cx-44*s)} {n(cy-38*s)} Z"
    return path(d,col)+path(f"M{n(cx-20*s)} {n(cy+2*s)} L{n(cx-6*s)} {n(cy+18*s)} L{n(cx+22*s)} {n(cy-14*s)}","none",WHITE,10*s)
def mag(cx,cy,s=1,col=NAVY):
    return line(cx+38*s,cy+38*s,cx+78*s,cy+78*s,col,16*s)+circ(cx,cy,48*s,"#FFFFFF66",col,10*s)+path(f"M{n(cx-28*s)} {n(cy-22*s)} Q{n(cx-14*s)} {n(cy-36*s)} {n(cx+4*s)} {n(cy-34*s)}","none",WHITE,6*s)
def spark(cx,cy,s,col=YEL):
    return path(f"M{n(cx)} {n(cy-s)} Q{n(cx)} {n(cy)} {n(cx+s)} {n(cy)} Q{n(cx)} {n(cy)} {n(cx)} {n(cy+s)} Q{n(cx)} {n(cy)} {n(cx-s)} {n(cy)} Q{n(cx)} {n(cy)} {n(cx)} {n(cy-s)} Z",col)
def cloud(cx,cy,s,col=WHITE):
    return circ(cx-22*s,cy,16*s,col)+circ(cx,cy-10*s,22*s,col)+circ(cx+24*s,cy,17*s,col)+rect(cx-24*s,cy,50*s,17*s,col,0)
def school(cx,by,s=1,body=SKY,roof=NAVY):
    g=rect(cx-60*s,by-70*s,120*s,70*s,body,6*s)
    g+=f'<polygon points="{n(cx-70*s)},{n(by-70*s)} {n(cx)},{n(by-112*s)} {n(cx+70*s)},{n(by-70*s)}" fill="{roof}"/>'
    g+=rect(cx-12*s,by-34*s,24*s,34*s,WHITE,4*s)
    for dx in(-44,28): g+=rect(cx+dx*s,by-54*s,16*s,18*s,WHITE,3*s)
    g+=circ(cx,by-84*s,8*s,WHITE)
    g+=line(cx+76*s,by,cx+76*s,by-86*s,NAVY,3*s)+f'<polygon points="{n(cx+76*s)},{n(by-86*s)} {n(cx+98*s)},{n(by-78*s)} {n(cx+76*s)},{n(by-70*s)}" fill="{ORANGE}"/>'
    return g
def flag(x,by,h,col=ORANGE):
    return line(x,by,x,by-h,NAVY,4)+f'<polygon points="{n(x)},{n(by-h)} {n(x+h*0.55)},{n(by-h*0.8)} {n(x)},{n(by-h*0.6)}" fill="{col}"/>'
def pin(cx,cy,s=1,col=ORANGE):
    return path(f"M{n(cx)} {n(cy+30*s)} Q{n(cx-22*s)} {n(cy+4*s)} {n(cx-22*s)} {n(cy-8*s)} A{n(22*s)} {n(22*s)} 0 1 1 {n(cx+22*s)} {n(cy-8*s)} Q{n(cx+22*s)} {n(cy+4*s)} {n(cx)} {n(cy+30*s)} Z",col)+circ(cx,cy-8*s,8*s,WHITE)
