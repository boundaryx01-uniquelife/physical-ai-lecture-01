from lib import *
DEFS='''<defs>
<linearGradient id="gW" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#D6E4FF"/></linearGradient>
<linearGradient id="gO" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF9A4D"/><stop offset="1" stop-color="#E8742A"/></linearGradient>
<linearGradient id="gB" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3D7BEA"/><stop offset="1" stop-color="#0B4FB3"/></linearGradient>
<linearGradient id="gG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4CC48B"/><stop offset="1" stop-color="#2FA36B"/></linearGradient>
<linearGradient id="gBg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E8F0FF"/><stop offset="1" stop-color="#FFF1E4"/></linearGradient>
</defs>'''
def kid2(cx,by,s=1,shirt="url(#gO)",pants="#1F3A6E",hair="#1B2440",arms="down",bag=True,flip=1):
    g=ell(cx,by+2*s,40*s,8*s,"#14213D1F")
    if bag: g+=rect(cx-40*s*flip if flip==1 else cx+24*s,by-106*s,16*s,46*s,"#C85A1E",9*s)
    g+=rect(cx-18*s,by-52*s,16*s,48*s,pants,8*s)+rect(cx+2*s,by-52*s,16*s,48*s,pants,8*s)
    g+=ell(cx-10*s,by-3*s,14*s,7*s,"#FFFFFF")+ell(cx+10*s,by-3*s,14*s,7*s,"#FFFFFF")+rect(cx-24*s,by-1*s,28*s,4*s,"#E8742A",2*s)+rect(cx-4*s,by-1*s,28*s,4*s,"#E8742A",2*s)
    def arm(side,mode):
        x0=cx+side*25*s;y0=by-98*s
        pts={"up":(cx+side*52*s,by-140*s),"wave":(cx+side*56*s,by-128*s),"fwd":(cx+side*54*s,by-92*s),"down":(cx+side*36*s,by-58*s),"hold":(cx+side*46*s,by-120*s),"cover":(cx+side*60*s,by-104*s)}
        x1,y1=pts[mode]
        return line(x0,y0,x1,y1,"#F29A5E" if shirt.startswith("url(#gO") else "#2F6FE0",14*s)+circ(x1,y1,8.5*s,SKIN)
    g+=rect(cx-28*s,by-112*s,56*s,68*s,shirt,22*s)
    if isinstance(arms,tuple): al,ar=arms
    else: al,ar=("down" if arms in("wave","hold","cover") else arms),arms
    g+=arm(-1,al)+arm(1,ar)
    hy=by-144*s
    g+=circ(cx-28*s,hy+2*s,6*s,SKIN)+circ(cx+28*s,hy+2*s,6*s,SKIN)+circ(cx,hy,28*s,SKIN)
    g+=path(f"M{n(cx-30*s)} {n(hy-2*s)} A{n(30*s)} {n(30*s)} 0 0 1 {n(cx+30*s)} {n(hy-2*s)} Q{n(cx+16*s)} {n(hy-16*s)} {n(cx+2*s)} {n(hy-8*s)} Q{n(cx-14*s)} {n(hy-18*s)} {n(cx-30*s)} {n(hy-2*s)} Z",hair)
    g+=circ(cx+4*s,hy-30*s,6*s,hair)
    g+=ell(cx-10*s,hy+4*s,3.8*s,5*s,"#14213D")+ell(cx+10*s,hy+4*s,3.8*s,5*s,"#14213D")+circ(cx-9*s,hy+2*s,1.4*s,WHITE)+circ(cx+11*s,hy+2*s,1.4*s,WHITE)
    g+=circ(cx-19*s,hy+13*s,5*s,"#FF9E8A88")+circ(cx+19*s,hy+13*s,5*s,"#FF9E8A88")
    g+=path(f"M{n(cx-7*s)} {n(hy+14*s)} Q{n(cx)} {n(hy+21*s)} {n(cx+7*s)} {n(hy+14*s)}","none","#14213D",2.8*s)
    return g
def robot2(cx,by,s=1,arms="down",eyes="#5BE1FF",confused=False):
    g=ell(cx,by+2*s,46*s,8*s,"#14213D1F")
    def arm(side,mode):
        x0=cx+side*32*s;y0=by-76*s
        pts={"up":(cx+side*62*s,by-122*s),"wave":(cx+side*64*s,by-110*s),"fwd":(cx+side*62*s,by-72*s),"down":(cx+side*50*s,by-48*s)}
        x1,y1=pts[mode]
        return line(x0,y0,x1,y1,"#C9D9F7",13*s)+circ(x1,y1,8*s,"#3D7BEA")
    if isinstance(arms,tuple): al,ar=arms
    else: al,ar=("down" if arms=="wave" else arms),arms
    g+=arm(-1,al)+arm(1,ar)
    g+=circ(cx,by-17*s,17*s,"#14213D")+circ(cx,by-17*s,6*s,"#DCE8FF")
    g+=rect(cx-34*s,by-98*s,68*s,68*s,"url(#gW)",24*s)
    g+=circ(cx,by-64*s,10*s,"url(#gO)")+circ(cx,by-64*s,4*s,WHITE)
    g+=rect(cx-10*s,by-106*s,20*s,12*s,"#9DB5E8",5*s)
    g+=rect(cx-44*s,by-176*s,88*s,72*s,"url(#gW)",30*s)
    g+=circ(cx-46*s,by-140*s,9*s,"url(#gO)")+circ(cx+46*s,by-140*s,9*s,"url(#gO)")
    g+=rect(cx-35*s,by-166*s,70*s,52*s,"#14213D",22*s)
    if confused:
        g+=ell(cx-15*s,by-143*s,6*s,8*s,eyes)+ell(cx+15*s,by-143*s,4*s,4*s,eyes)+path(f"M{n(cx-8*s)} {n(by-126*s)} L{n(cx+8*s)} {n(by-126*s)}","none",eyes,3.5*s)
    else:
        g+=ell(cx-15*s,by-143*s,6*s,8*s,eyes)+ell(cx+15*s,by-143*s,6*s,8*s,eyes)+path(f"M{n(cx-9*s)} {n(by-127*s)} Q{n(cx)} {n(by-120*s)} {n(cx+9*s)} {n(by-127*s)}","none",eyes,3.5*s)
    g+=line(cx,by-176*s,cx,by-194*s,"#9DB5E8",4*s)+circ(cx,by-198*s,7*s,"url(#gO)")
    return g
def bg(w,h,cx,cy,r): return circ(cx,cy,r,"url(#gBg)")
def sp(x,y,s,c=YEL): return spark(x,y,s,c)
