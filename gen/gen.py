import os,re
OUT='./lecture/project/slides/'
IMG=dict(cover='8dd4de3a0c5d45a068f066a3d1dfe68f',closing='cfa02a67051547ac80ffc913fcc403d2',agenda='f74a71b204cf05f62298feb6527af0ac',
curriculum='b621aba6164c62e4665d62f632b2c9a1',policy='3b8ec40a9ae9d5ba49334b042aa0332d',literacy='dfb76f583e6160d66816a709970d61ba',
physical='9e00f2ed3870ff848a24e0f9a1afbabc',why='9ab7a3a4ad1bf04bdb41eeaafcddd279',vsA='12f6c1f2539f186689ede3df1d44c50d',
vsB='9397950ca994b82be05b75aa2c83a611',vsC='64dec31b4f28ec84e7f9bf13bd811fae',limits='964c7c382bc66b1918beb1be04b5dd1a',
overseas='02414096ab505d9c070e99f1a21b78cf',overseas2='f32a24bb47b2f3eacd8e16ac40f50ae7',naesung='72af0bd642d688a7bc714073e229a890',
center='f672fc505d270bd9bb77d043265fcf3f',impl='1e57bcdf8a7b9e75288df89fc981af66',start='44785f7a21138e00d1f60cb5dacc7b66',
safety='be41ab395c5d854984bcdad249859af1',senseq='20deecf9b1e06713e3355aa9657a5266')
FONT="font-family:'Noto Sans KR', Arial, sans-serif"
def img(k,w,h,alt,extra=""):
    return f'<img src="/_blob/{IMG[k]}" alt="{alt}" style="width:{w}px;height:{h}px;object-fit:contain;{extra}">'
def head(label,title,size=60):
    return f'<div style="display:flex;flex-direction:column;gap:12px"><p style="font-size:26px;font-weight:700;color:#0B4FB3">{label}</p><h2 style="font-size:{size}px;font-weight:900;line-height:1.15">{title}</h2></div>'
def foot(src,page,dark=False):
    c="#B9C6E4" if dark else "#5B6779"
    return f'<p style="position:absolute;left:128px;bottom:64px;width:1500px;font-size:24px;line-height:1.4;color:{c}">{src}</p><p style="position:absolute;right:128px;bottom:64px;width:120px;text-align:right;font-size:24px;color:{c}">{page}</p>'
def sec(id,inner,notes,dark=False,gap=32,pad="128px 128px 160px",extra=""):
    bg="#14213D" if dark else "#F2F5FB"; fg="#EEF2FA" if dark else "#14213D"
    return f'<section id="{id}" data-transition="fade" style="background:{bg};color:{fg};{FONT};padding:{pad};display:flex;flex-direction:column;gap:{gap}px;{extra}">\n{inner}\n<aside>{notes}</aside>\n</section>\n'
CARD='background:#FCFDFF;border:1px solid #D3DBEA;border-radius:16px'
BAND='background:#14213D;border-radius:16px'
def write(id,html): open(OUT+id+'.html','w').write(html)

# 1 cover
write('cover',sec('cover',f'''<p style="font-size:32px;font-weight:500;color:#B9C6E4">피지컬 AI 교육 교원 워크숍 · 2부 학교급별 사례 나눔</p>
<div style="display:flex;flex-direction:column;gap:32px">
<h1 style="font-size:92px;font-weight:900;line-height:1.15;color:#FFFFFF">초등 피지컬 AI 교육의<br>방향과 우수사례</h1>
<p style="font-size:44px;font-weight:500;color:#F6B48A">2022 개정 교육과정과 AI for All 기조 아래서</p>
</div>
<div style="display:flex;flex-direction:column;gap:8px">
<p style="font-size:32px;font-weight:700;color:#FFFFFF">박재현 선생님 · 내성초등학교</p>
<p style="font-size:26px;color:#B9C6E4">2026. 11. 02 · 부산광역시교육청 디지털미래교육과</p>
</div>
<div style="position:absolute;left:1200px;top:270px">{img('cover',640,480,'학생과 로봇이 함께 손을 드는 일러스트')}</div>''',
'[0:00–0:30] 안녕하세요, 내성초등학교 박재현입니다. 오늘 20분은 교육과정에서 시작해 교실까지 갑니다. 초등 AI 성취기준, 교육부 방침과 AI 리터러시, 피지컬 AI의 개념과 한계, 해외 사례, 그리고 저희 현장 사례와 내일 시작하는 방법입니다.',dark=True,gap=48,pad='128px'))

# 2 agenda
rows=[("22개정 초등 AI 성취기준","약 1분"),("교육부 방침과 AI 리터러시","약 3분"),("피지컬 AI의 개념과 기대","약 1분"),("초등 AI 교육의 한계","약 1분"),("피지컬 컴퓨팅과의 차이, 수업 속 리터러시","약 2분"),("해외 사례와 적용 방향","약 2분"),("현장 사례 · 시사점 · 내일 시작","약 9분")]
rh="".join(f'<div style="display:flex;flex-direction:row;align-items:center;gap:20px;{CARD};padding:10px 24px"><div style="width:48px;height:48px;border-radius:24px;background:{"#E8742A" if i==1 else "#0B4FB3"};color:#FFFFFF;font-size:28px;font-weight:900;text-align:center;line-height:48px">{i+1}</div><p style="flex:1;font-size:32px;font-weight:700">{t}</p><p style="font-size:26px;color:#5B6779">{m}</p></div>' for i,(t,m) in enumerate(rows))
write('agenda',sec('agenda',f'''{head("오늘의 순서 · 20분","교육과정에서 교실까지, 일곱 걸음")}
<div style="display:flex;flex-direction:row;align-items:center;gap:40px">
<div style="flex:1;display:flex;flex-direction:column;gap:12px">{rh}</div>
{img('agenda',440,423,'굽이진 길과 일곱 개의 이정표')}
</div>
{foot("주황색 2번은 오늘 가장 힘주어 말씀드릴 AI 리터러시 부분입니다.",2)}''',
'[0:30–1:00] 순서입니다. 제가 정리한 일곱 걸음입니다. 성취기준, 교육부 방침과 AI 리터러시, 피지컬 AI의 개념, 한계, 피지컬 컴퓨팅과의 차이, 해외 사례, 그리고 현장 사례에서 내일 시작하는 방법까지입니다. 가장 힘주어 말씀드릴 곳은 2번, 지침 속의 AI 리터러시입니다.'))

# 3 curriculum
std=[("6실05-01","생활 문제를 알고리즘으로 표현"),("6실05-02","컴퓨터에게 명령하는 프로그램 작성"),("6실05-03","협력해 프로그램을 만들고 공유"),("6실05-04","AI에 쓰는 데이터의 유형 탐색"),("6실05-05","AI가 만들어지는 과정 체험, 사회적 영향 탐색")]
sh="".join(f'<div style="display:flex;flex-direction:row;align-items:center;gap:20px;{"background:#FFF1E4;border:2px solid #E8742A;border-radius:16px" if i==4 else CARD};padding:12px 24px"><div style="width:48px;height:48px;border-radius:24px;background:{"#E8742A" if i==4 else "#0B4FB3"};color:#FFFFFF;font-size:28px;font-weight:900;text-align:center;line-height:48px">{i+1}</div><div style="display:flex;flex-direction:column;gap:2px"><p style="font-size:22px;font-weight:700;color:#5B6779">[{c}]</p><p style="font-size:30px;font-weight:700;line-height:1.25">{t}</p></div></div>' for i,(c,t) in enumerate(std))
write('curriculum',sec('curriculum',f'''{head("1 · 교육과정","22개정이 정한 초등 AI 성취기준")}
<div style="display:flex;flex-direction:row;align-items:center;gap:40px">
<div style="flex:1;display:flex;flex-direction:column;gap:10px">{sh}</div>
{img('curriculum',480,402,'다섯 계단을 오르는 학생과 로봇')}
</div>
<div style="{BAND};padding:24px 40px"><p style="font-size:32px;font-weight:700;line-height:1.4;color:#FFFFFF">실과 5~6학년 ‘디지털 사회와 인공지능’ · 초등 정보교육 34시간 이상 · 디지털 소양은 <span style="color:#FFD2B3">언어·수리와 같은 기초소양</span></p></div>
{foot("출처: 교육부 고시 제2022-33호 초등학교 교육과정(2차 자료로 확인), 교육부 2026년 업무계획. AI 윤리는 여러 교과에 나뉘어 있어 교과별 성취기준은 국가교육과정정보센터에서 확인하세요.",3)}''',
'[1:00–2:15] 먼저 교육과정입니다. 2022 개정은 디지털 소양을 언어, 수리와 같은 기초소양으로 올렸고, 초등 정보교육은 34시간 이상입니다. 5~6학년 실과에 디지털 사회와 인공지능 영역이 생겼고 성취기준은 다섯 개입니다. 알고리즘, 프로그램, 협력과 공유, 데이터, 그리고 마지막 6실05-05, 인공지능이 만들어지는 과정을 체험하고 사회에 미치는 영향을 탐색한다. 이 마지막 문장에 이미 AI 리터러시가 들어 있습니다. 뒤에서 다시 말씀드리겠습니다.'))

# 4 policy
pc=[("2025. 11. 10","AI for All","초중등부터 평생교육까지 전 생애 AI 교육 체계. AI 윤리를 교육과정에 포함"),
("2026. 3","1,141개교","AI 중점학교 운영 시작(초등 530교). 초등 AI·정보교육을 34시간에서 68시간 이상으로"),
("2027 · 2028","2,000개교","1,500개교(2027)를 거쳐 2,000개교(2028)까지 단계적으로 확대 계획"),
("2029~","교육과정 개정","2026 연구, 2027 상반기 개정 요청, 2029년 이후 현장 적용 전망")]
ph="".join(f'<div style="flex:1;display:flex;flex-direction:column;gap:10px;{CARD};padding:24px 28px"><p style="font-size:24px;font-weight:700;color:#0B4FB3">{a}</p><p style="font-size:40px;font-weight:900;line-height:1.2">{b}</p><p style="font-size:24px;line-height:1.4;color:#4A5568">{c}</p></div>' for a,b,c in pc)
write('policy',sec('policy',f'''{head("2 · 교육부 방침","정책은 ‘모두를 위한 AI’로 단계 확대 중입니다")}
<div style="display:flex;flex-direction:row;align-items:center;gap:32px">
{img('policy',560,280,'점점 커지는 학교 건물과 상승 화살표')}
<div style="flex:1;{BAND};padding:32px 40px"><p style="font-size:40px;font-weight:700;line-height:1.4;color:#FFFFFF">초등의 열쇠는 하나입니다. 일부가 아니라 <span style="color:#FFD2B3">모든 학생이 AI를 경험</span>하는 것, 그리고 AI 윤리와 리터러시가 함께 가는 것.</p></div>
</div>
<div style="display:flex;flex-direction:row;gap:20px">{ph}</div>
{foot("출처: 교육부 AI 인재양성 방안(2025.11.10), AI 중점학교 운영 보도(2026.3), 이투데이(2025.11). 수치는 발표 전 교육부 공지로 재확인하세요.",4)}''',
'[2:15–3:30] 교육부 방침입니다. 2025년 11월 모두를 위한 AI, AI for All이 발표됐습니다. 초중등부터 평생교육까지 이어지는 체계이고 AI 윤리를 교육과정에 넣겠다는 내용이 들어 있습니다. 2026년 3월에는 AI 중점학교 1,141개교가 시작했고 초등은 530개교입니다. 초등 AI·정보교육을 34시간에서 68시간 이상으로 늘립니다. 2027년 1,500개교, 2028년 2,000개교로 확대하고, 교육과정 개정은 2029년 이후 적용 전망입니다. 숫자는 보도를 인용한 것이라 공식 공지로 한 번 더 확인해 주세요.'))

# 5 literacy
lg=[("22개정 교육과정","디지털 소양은 기초소양. [6실05-05]에서 AI의 사회적 영향까지 탐색"),
("교육부 AI 인재양성 방안(2025.11)","초중등 AI 리터러시 강화, AI 윤리를 교육과정에 포함, 과몰입·의존 방지"),
("UNESCO 학생 AI 역량 틀(2024)","인간 중심 사고·AI 윤리·AI 기술과 활용·AI 시스템 설계, 이해→적용→창작 3수준"),
("EC·OECD AI 리터러시 틀(2026.6)","Engage·Create·Manage·Shape 4영역, 19개 역량. 초등 기초: 일상 속 AI 찾기"),
("KICE 교사 지침(2026.10)","교사의 생성형 AI 활용 윤리 5원칙: 투명·안전·공정·책임·협력")]
lh="".join(f'<div style="display:flex;flex-direction:row;align-items:center;gap:24px;{CARD};padding:10px 24px"><div style="width:330px;font-size:24px;font-weight:700;line-height:1.3;color:#0B4FB3">{a}</div><p style="flex:1;font-size:25px;line-height:1.35;color:#2A3550">{b}</p></div>' for a,b in lg)
write('literacy',sec('literacy',f'''{head("2 · 교육부 방침 속 AI 리터러시","지침은 한목소리로 ‘AI 리터러시’를 말합니다")}
<div style="display:flex;flex-direction:row;align-items:center;gap:32px">
<div style="flex:1;display:flex;flex-direction:column;gap:10px">{lh}</div>
{img('literacy',440,330,'AI 답변을 돋보기로 확인하는 로봇')}
</div>
<div style="background:#E8742A;border-radius:16px;padding:20px 40px"><p style="font-size:36px;font-weight:900;color:#FFFFFF">공통 요구: 원리 이해 · 결과 검증 · 책임 있는 사용</p></div>
{foot("출처: 교육부(2025.11), 이투데이, UNESCO(2024), EC·OECD(2026.6, EdTech Innovation Hub 해설), KICE 연구리포트 제13호(2026.10.7). ‘공통 요구’는 발표자가 묶어 정리했습니다.",5)}''',
'[3:30–5:00] 오늘 가장 힘주어 말씀드릴 부분입니다. 교육과정, 교육부 방침, 유네스코, 유럽연합과 OECD, 그리고 지난달 KICE 교사 지침까지, 서로 다른 문서가 같은 말을 합니다. AI를 쓸 줄 아는 것으로 끝나지 않고, 원리를 이해하고, 결과를 따져 보고, 책임 있게 쓰라는 것입니다. 교육부 방안은 AI 윤리를 교육과정에 넣고 과몰입과 의존을 막는 리터러시를 강조합니다. 유네스코는 인간 중심 사고와 윤리를 기술 이해와 같은 급의 차원으로 둡니다. KICE의 5원칙은 학생이 아니라 교사가 AI를 쓸 때의 원칙이지만, 교사가 먼저 보여주는 본보기가 됩니다. 공통 요구라는 세 단어는 제가 묶어 정리한 표현입니다. 유럽연합과 OECD 틀은 보도 기준으로 2026년 6월 발표로 확인했습니다.'))

# 6 physical
card3=lambda t,d,ic:f'<div style="flex:1;display:flex;flex-direction:column;gap:12px;{CARD};padding:28px"><p style="font-size:44px;font-weight:900;color:#0B4FB3">{t}</p><p style="font-size:26px;line-height:1.4;color:#4A5568">{d}</p></div>'
write('physical',sec('physical',f'''{head("3 · 피지컬 AI의 개념","화면 밖으로 나온 AI")}
<div style="display:flex;flex-direction:row;align-items:stretch;gap:24px">
{card3("감지","센서·카메라·마이크로 상황을 읽는다","")}{card3("판단","규칙이나 모델로 무엇을 할지 정한다","")}{card3("실행","모터·LED·로봇 팔로 몸을 움직인다","")}
</div>
<div style="display:flex;flex-direction:row;align-items:center;gap:32px;{BAND};padding:24px 40px">
<p style="flex:1;font-size:38px;font-weight:700;line-height:1.45;color:#FFFFFF">챗봇은 답을 말하지만, 피지컬 AI는 <span style="color:#FFD2B3">행동하고 그 결과를 다시 감지</span>합니다.</p>
{img('physical',480,231,'감지, 판단, 실행이 되돌아오는 고리')}
</div>
{foot("수업에서 쓰는 풀이입니다. 학계의 엄밀한 정의와는 다를 수 있습니다.",6)}''',
'[5:00–5:45] 피지컬 AI를 어렵게 말하지 않겠습니다. 감지, 판단, 실행입니다. 센서로 읽고, 규칙이나 모델로 정하고, 모터나 LED로 움직입니다. 그리고 그 결과를 다시 읽는 고리가 있습니다. 챗봇은 답을 말하지만 피지컬 AI는 행동하고 결과를 다시 봅니다. 수업을 위한 풀이이니 학계의 엄밀한 정의와는 다를 수 있습니다.'))

# 7 why
wy=[("보입니다","움직임으로 나타나니 감지·판단·실행이 눈에 보입니다."),("만집니다","오류도 실제 동작으로 드러나, 직접 고치며 배웁니다."),("함께합니다","한 로봇을 두고 결과를 같이 보고 이야기합니다.")]
wh="".join(f'<div style="{CARD};padding:20px 32px"><p style="font-size:40px;font-weight:900;color:#0B4FB3">{a}</p><p style="font-size:28px;line-height:1.4;color:#4A5568">{b}</p></div>' for a,b in wy)
write('why',sec('why',f'''{head("3 · 피지컬 AI의 기대 방향","보이고, 만져지고, 함께하는 AI 수업",56)}
<div style="display:flex;flex-direction:row;align-items:center;gap:40px">
<div style="flex:1;display:flex;flex-direction:column;gap:16px">{wh}</div>
{img('why',440,364,'로봇을 둘러싸고 함께 보는 학생들')}
</div>
<div style="background:#FFF4E5;border:2px solid #F6B48A;border-radius:16px;padding:20px 40px"><p style="font-size:30px;font-weight:700;line-height:1.4">주의: ‘공간지각력·집중력 향상’ 같은 효과 주장은 근거가 충분하지 않아 오늘은 말하지 않습니다.</p></div>
{foot("수업 경험에 바탕한 기대입니다. 체화된 인지 이론은 배경 이론일 뿐 효과의 증거는 아닙니다.",7)}''',
'[5:45–6:15] 기대하는 방향은 세 가지입니다. 보이고, 만져지고, 함께하는 수업입니다. 코드가 틀리면 로봇이 엉뚱하게 움직여 오류가 눈에 보이고, 친구와 함께 이야기하게 됩니다. 다만 공간지각이나 집중력이 좋아진다는 식의 주장은 근거가 충분하지 않아 오늘은 하지 않겠습니다. 수업 경험에 바탕한 기대입니다.'))

# 8 limits
lm=[("교사 연수·전문성","연수 참여 교원의 61.0%가 ‘유용하지 않았다’고 응답(교총, 교원 3,485명)"),
("업무·행정 부담","AI 디지털교과서 활용 교사의 79.7%가 업무 증가 응답(교총). 중점학교도 준비 시간·인력 부족 우려"),
("신뢰·안전","교사 63%가 생성형 AI 활용. 우려는 부정확한 정보·개인정보 유출·사고력 저하(KICE, 2026.10)"),
("제도의 변동","AI 디지털교과서를 ‘교과서’에서 ‘교육자료’로 바꾸는 법 개정 추진(2025.8)")]
lmh=[f'<div style="flex:1;{CARD};padding:20px 28px;display:flex;flex-direction:column;gap:8px"><p style="font-size:32px;font-weight:900;color:#0B4FB3">{a}</p><p style="font-size:24px;line-height:1.4;color:#4A5568">{b}</p></div>' for a,b in lm]
write('limits',sec('limits',f'''{head("4 · 초등 AI 교육의 한계","현장이 말하는 네 가지 벽")}
<div style="display:flex;flex-direction:row;align-items:center;gap:32px">
<div style="flex:1;display:flex;flex-direction:column;gap:20px"><div style="display:flex;flex-direction:row;gap:20px">{lmh[0]}{lmh[1]}</div><div style="display:flex;flex-direction:row;gap:20px">{lmh[2]}{lmh[3]}</div></div>
{img('limits',440,330,'벽 앞에서 사다리를 바라보는 교사')}
</div>
<div style="{BAND};padding:20px 40px"><p style="font-size:32px;font-weight:700;line-height:1.4;color:#FFFFFF">피지컬 AI에는 <span style="color:#FFD2B3">교구 예산·보관·안전 관리</span>가 더해집니다. <span style="font-size:24px;font-weight:500;color:#B9C6E4">(발표자 정리)</span></p></div>
{foot("출처: 교총 설문(2025.7.28, 풀뉴스), KICE 연구리포트 제13호(2026.10.7), 한국교육신문(2026.7), 이투데이(2025.8.4). 법 개정 이후의 현재 지위는 공식 공지로 확인하세요.",8)}''',
'[6:15–7:30] 한계도 숨기지 않겠습니다. 연수는 기기 조작 안내에 치우쳤다는 평가가 많았고, 교총 조사에서 연수에 참여한 교원의 61.0%가 유용하지 않았다고 했습니다. AI 디지털교과서를 쓰는 교사의 79.7%는 업무가 늘었다고 했고, AI 중점학교 현장에서도 준비 시간과 인력 부족 우려가 나옵니다. KICE 조사에서는 교사 63%가 생성형 AI를 쓰고 있고, 부정확한 정보와 개인정보 유출, 사고력 저하를 걱정합니다. 제도도 움직이고 있어서, AI 디지털교과서의 지위가 교과서에서 교육자료로 바뀌는 법 개정이 2025년 8월 처리 단계에 올랐습니다. 현재 지위는 공식 공지로 확인하셔야 합니다. 피지컬 AI에는 교구 예산과 보관, 안전 관리가 더해진다는 점은 제 정리입니다. 교총 수치는 해당 연수 참여자, 해당 교과서 활용 교사를 모집단으로 한 값입니다.'))

# 9 vs sw
cols=[("A · 규칙, 한 방향","vsA","버튼을 누르면 LED가 켜진다",[("예","버튼 → LED 켜기"),("판단","사람이 정한 규칙"),("학생","연결·제어 코딩")],"#0B4FB3"),
("B · 규칙, 되먹임","vsB","라인트레이서",[("예","라인트레이서"),("판단","규칙 + 센서 되먹임"),("학생","조건·반복 조정")],"#0B4FB3"),
("C · 학습, 되먹임","vsC","카메라로 학습한 분류 로봇",[("예","물체·동작 분류 로봇"),("판단","데이터로 만든 모델"),("학생","데이터·평가·편향")],"#E8742A")]
def col(t,k,alt,rs,c):
    r="".join(f'<div style="display:flex;flex-direction:row;gap:12px"><p style="width:64px;font-size:22px;font-weight:700;color:{c}">{a}</p><p style="flex:1;font-size:26px;font-weight:500">{b}</p></div>' for a,b in rs)
    return f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:10px;{CARD};padding:20px 24px;{"border:2px solid #E8742A;" if k=="vsC" else ""}">{img(k,300,192,alt)}<p style="font-size:34px;font-weight:900;color:{c}">{t}</p><div style="width:100%;display:flex;flex-direction:column;gap:6px">{r}</div></div>'
write('vssw',sec('vssw',f'''{head("5 · 기존 SW교육과의 차이","피지컬 컴퓨팅 위에 ‘학습하는 판단’을 얹습니다",56)}
<div style="display:flex;flex-direction:row;gap:24px">{"".join(col(*c) for c in cols)}</div>
<div style="{BAND};padding:20px 40px"><p style="font-size:34px;font-weight:700;line-height:1.4;color:#FFFFFF">A·B는 기존 피지컬 컴퓨팅, <span style="color:#FFD2B3">C에서 ‘AI의 판단’</span>이 시작됩니다. 버리지 않고 위에 얹습니다.</p></div>
{foot("‘규칙 기반=열린 고리’로 단정하지 않았습니다. 라인트레이서처럼 규칙 기반이면서 센서로 다시 확인하는 사례가 많습니다. 발표자 정리.",9)}''',
'[7:30–8:45] 기존 SW교육과 무엇이 다른가. 마이크로비트, 아두이노 같은 피지컬 컴퓨팅은 이미 해 왔습니다. 세 단계로 보면 쉽습니다. A는 규칙이고 한 방향입니다. 버튼을 누르면 LED가 켜집니다. B는 규칙이지만 센서로 다시 확인합니다. 라인트레이서입니다. 흔히 규칙 기반은 열린 고리라고 하는데, 이렇게 규칙 기반이면서 되먹임이 있는 사례가 많아서 저는 단정하지 않습니다. C는 데이터로 만든 모델이 판단하고 결과를 다시 봅니다. 카메라로 사물이나 동작을 학습시킨 분류 로봇입니다. 학생이 하는 일도 달라집니다. 연결과 제어에서 데이터를 모으고, 평가하고, 편향을 점검하는 일로 넓어집니다. 그래서 버리지 않고 위에 얹습니다. 제미나이 보고서의 학습 기반 모델을 초등생이 설계한다는 서술은 현실과 맞지 않아 쓰지 않았습니다.'))

# 10 literacy2
q=[("무엇으로 감지했지? 가리거나 어두우면?","AI의 한계"),("규칙으로 정했나, 데이터로 배웠나?","데이터·편향"),("틀렸을 때 누가 멈추고 누가 책임지지?","책임·안전"),("AI가 꼭 필요했나? 규칙으로 충분하지 않나?","비판적 판단"),("카메라·마이크의 정보는 어디로 가지?","개인정보")]
qh="".join(f'<div style="display:flex;flex-direction:row;align-items:center;gap:20px;{CARD};padding:10px 24px"><div style="width:44px;height:44px;border-radius:22px;background:#0B4FB3;color:#FFFFFF;font-size:26px;font-weight:900;text-align:center;line-height:44px">{i+1}</div><p style="flex:1;font-size:30px;font-weight:700">{a}</p><p style="font-size:24px;font-weight:700;color:#B84A12;background:#FFF1E4;border-radius:12px;padding:6px 16px">{b}</p></div>' for i,(a,b) in enumerate(q))
write('literacy2',sec('literacy2',f'''{head("5 · 수업 속 AI 리터러시","피지컬 AI 수업은 AI 리터러시를 몸으로 배웁니다",58)}
<div style="display:flex;flex-direction:row;align-items:center;gap:32px">
<div style="flex:1;display:flex;flex-direction:column;gap:10px">{qh}</div>
{img('senseq',440,330,'카드로 센서를 가리자 당황하는 로봇')}
</div>
<div style="{BAND};padding:20px 40px"><p style="font-size:34px;font-weight:700;line-height:1.4;color:#FFFFFF">구조대 부스라면: <span style="color:#FFD2B3">팔을 가리면 인식될까? 틀린 명령이 나오면 누가 멈출까?</span></p></div>
{foot("다섯 질문은 UNESCO·EC/OECD 틀과 micro:bit 재단의 AI 수업 질문을 참고해 발표자가 수업용으로 정리했습니다.",10)}''',
'[8:45–9:45] 그래서 피지컬 AI 수업에서 무엇을 묻는가. 로봇은 틀리면 눈에 보입니다. 이것이 리터러시 수업의 재료가 됩니다. 하나, 무엇으로 감지했는가, 가리거나 어두우면 어떻게 되는가. 둘, 규칙으로 정했는가 데이터로 배웠는가. 셋, 틀렸을 때 누가 멈추고 누가 책임지는가. 넷, AI가 꼭 필요했는가, 규칙으로 충분하지 않은가. 다섯, 카메라와 마이크의 정보는 어디로 가는가. 뒤에서 보여 드릴 구조대 부스에 이 질문을 그대로 붙일 수 있습니다. 다섯 질문은 해외 틀을 참고해 제가 수업용으로 정리한 것입니다.'))

# 11 overseas
ov=[("미국 · AI4K12","5 Big Ideas: 인식·표현과 추론·학습·자연스러운 상호작용·사회적 영향. K-2, 3-5, 6-8, 9-12로 심화","큰 개념(인식)을 센서와 이으면 피지컬 AI 수업의 뼈대가 됩니다."),
("UNESCO · 학생 AI 역량 틀(2024)","인간 중심 사고·AI 윤리·기술과 활용·시스템 설계의 4차원, 이해→적용→창작 3수준","만들기 전에 ‘이해’와 ‘윤리’를 거치는 순서를 둡니다."),
("EC·OECD · AI 리터러시 틀(2026.6)","Engage·Create·Manage·Shape 4영역, 19역량. 초등 예: AI의 답과 교사 풀이 비교","AI 결과를 사람의 방법과 견주는 활동이 초등의 출발점입니다.")]
ovh="".join(f'<div style="{CARD};padding:16px 28px;display:flex;flex-direction:column;gap:4px"><p style="font-size:30px;font-weight:900;color:#0B4FB3">{a}</p><p style="font-size:24px;line-height:1.35;color:#2A3550">{b}</p><p style="font-size:24px;line-height:1.35;font-weight:700;color:#B84A12">적용 → {c}</p></div>' for a,b,c in ov)
write('overseas',sec('overseas',f'''{head("6 · 해외 사례 ① 틀","해외는 ‘틀’을 먼저 세웠습니다")}
<div style="display:flex;flex-direction:row;align-items:center;gap:32px">
<div style="flex:1;display:flex;flex-direction:column;gap:14px">{ovh}</div>
{img('overseas',440,338,'궤도를 도는 책과 지구본')}
</div>
{foot("출처: AI4K12(AAAI·CSTA), UNESCO AI competency framework for students(2024), EC·OECD AI Literacy Framework(EdTech Innovation Hub 해설). 틀의 이름과 영역 수는 확인한 범위만 적었습니다.",11)}''',
'[9:45–11:00] 해외는 틀을 먼저 세웠습니다. 미국의 AI4K12는 인식, 표현과 추론, 학습, 자연스러운 상호작용, 사회적 영향이라는 다섯 개의 큰 개념을 학년군마다 깊게 가르칩니다. 유네스코의 학생 AI 역량 틀은 인간 중심 사고, 윤리, 기술, 시스템 설계의 네 차원에 이해, 적용, 창작의 세 수준입니다. 유럽연합과 OECD의 틀은 네 영역 열아홉 역량이고, 초등 기초 예시로 AI의 답과 교사의 풀이를 비교하는 활동이 소개됩니다. 우리 수업에 적용하면, 인식은 센서와 잇고, 만들기 전에 이해와 윤리를 거치고, AI 결과를 사람의 방법과 견주는 것입니다. 제미나이 보고서의 싱가포르 의무 10시간 등은 출처를 찾지 못해 뺐습니다.'))

# 12 overseas2
oc=[("영국 micro:bit CreateAI(2024)","자기 움직임으로 데이터를 모으고 모델을 훈련·테스트합니다. 편향·프라이버시, ‘AI가 꼭 필요한가’까지 묻습니다."),
("중국(2025.9~)","베이징은 초·중 AI 교육을 연 8시간 이상 의무화. 초등 목표에 ‘AI가 만든 허위정보 위험 평가’가 들어갑니다."),
("핀란드 Elements of AI","누구나 무료로 듣는 온라인 AI 입문 과정. 접근 장벽을 낮춘 사례로 소개됩니다(칼럼).")]
och="".join(f'<div style="flex:1;{CARD};padding:20px 28px;display:flex;flex-direction:column;gap:8px"><p style="font-size:30px;font-weight:900;color:#0B4FB3">{a}</p><p style="font-size:24px;line-height:1.4;color:#4A5568">{b}</p></div>' for a,b in oc)
write('overseas2',sec('overseas2',f'''{head("6 · 해외 사례 ② 실천","해외에서 가져올 세 가지 실천")}
<div style="display:flex;flex-direction:row;align-items:center;gap:32px">
{img('overseas2',520,319,'마이크로비트형 보드와 데이터 그래프')}
<div style="flex:1;{BAND};padding:32px 40px"><p style="font-size:36px;font-weight:700;line-height:1.45;color:#FFFFFF">시수를 정하고, 도구에 <span style="color:#FFD2B3">데이터·편향 질문</span>을 담고, 접근을 열어 <span style="color:#FFD2B3">모든 학생</span>에게 닿게 합니다.</p></div>
</div>
<div style="display:flex;flex-direction:row;gap:20px">{och}</div>
{foot("출처: micro:bit 재단(2024.11.20), 호주 교육부 자료 ‘China’s approach to AI education’(2025), 한국교육신문 칼럼(2025.11.5).",12)}''',
'[11:00–12:00] 해외에서 가져올 실천 세 가지입니다. 영국 micro:bit 재단의 CreateAI는 학생이 자기 움직임으로 데이터를 모으고 모델을 훈련하고 테스트해서 독립형 제품까지 만듭니다. 그 과정에서 데이터 프라이버시, 편향, AI가 정말 필요한가를 묻는 것이 핵심입니다. 마이크로비트를 쓰는 학교에는 좋은 참고가 됩니다. 중국은 2025년 9월부터 베이징 초중학교에서 AI 교육을 연 8시간 이상 하고, 초등 목표에 AI가 만든 허위정보의 위험 평가가 들어 있습니다. 핀란드는 누구나 무료로 듣는 입문 과정으로 접근 장벽을 낮췄다고 칼럼에서 소개합니다. 시수를 정하고, 도구에 데이터와 편향 질문을 담고, 접근을 여는 것, 이 세 가지를 가져오면 됩니다.'))

# 13 naesung
def nc(t,b): return f'<div style="{CARD};padding:16px 32px"><p style="font-size:30px;font-weight:700;color:#0B4FB3">{t}</p><p style="font-size:24px;line-height:1.4;color:#4A5568">{b}</p></div>'
write('case-naesung',sec('case-naesung',f'''{head("7 · 현장 사례 ① 내성초","행사·수업·방과후가 한 줄로 이어집니다")}
<div style="display:flex;flex-direction:row;align-items:center;gap:32px">
<div style="flex:1;display:flex;flex-direction:column;gap:14px">
{nc("학교 행사 · 2026. 5. 11 「내성 AI 디지털 페스타」","8개 체험 부스를 고학년이 운영(멘토-멘티). 그중 「AI 커맨딩 로봇 구조대」는 몸동작으로 포니봇을 조작하는 부스.")}
{nc("수업 · 10월 「AI메이커교육 with 로보틱스」","1~2학년 포즈 인식 AI 게임·휴머노이드 키링, 3~4학년 이족보행로봇, 5~6학년 AI 포니봇 팀 챌린지.")}
{nc("방과후·방학 · 포니봇 동아리, 여름 로봇 코딩 캠프","캠프 8.24~28, 20차시, 4~6학년 24명. 마이크로비트 기반 포니봇·카미봇으로 센서 기반 자율주행 미션.")}
</div>
{img('naesung',400,278,'학교 건물 앞에서 손을 흔드는 로봇')}
</div>
<p style="font-size:32px;font-weight:700;line-height:1.4">핵심: 같은 교구를 <span style="color:#B84A12">행사 → 수업 → 방과후·방학</span>으로 이어 쓰고, 학년이 오를수록 미션이 커집니다.</p>
{foot("출처: 내성초 보도자료(2026.5.11), 2026 내성초 AI메이커교육 운영 계획, 여름 캠프 운영 계획(계획서 기준)",13)}''',
'[12:00–12:30] 여기서부터는 저희 현장 사례입니다. 내성초는 같은 교구를 5월 페스타, 10월 AI메이커교육, 방과후와 여름방학 캠프로 이어 씁니다. 페스타에서는 체험 부스 여덟 개를 고학년이 운영자가 되어 후배에게 안내했습니다. 10월에는 학년별로 저학년 포즈 인식 AI 게임, 3~4학년 이족보행로봇, 5~6학년 AI 포니봇 팀 챌린지를 했습니다. 캠프는 4~6학년 24명이 5일 20차시로 했습니다. 캠프·수업 내용은 운영 계획서 기준입니다.'))

# 14 rescue patch
r=open(OUT+'case-rescue.html').read()
r=r.replace('4 · 우수사례 ④ 내성초','7 · 현장 사례 ② 내성초').replace('>13</p>','>14</p>').replace('[11:30–13:00]','[12:30–13:30]')
r=r.replace('감지, 실행이 그대로 보입니다.','감지, 판단, 실행이 그대로 보입니다.')
if '리터러시' not in r:
    r=r.replace('(사진 속 학생 얼굴은 흐림 처리했습니다.)','앞에서 드린 질문을 붙여 보면, 팔을 가리면 인식될까, 틀린 명령이 나오면 누가 멈출까입니다. (사진 속 학생 얼굴은 흐림 처리했습니다.)')
write('case-rescue',r)

# 15 center
write('case-center',sec('case-center',f'''{head("7 · 현장 사례 ③ 동래발명교육센터","기능 익히기에서 문제 해결 데모로",60)}
<div style="display:flex;flex-direction:row;gap:24px">
<div style="width:520px;display:flex;flex-direction:column;gap:14px;justify-content:center;{BAND};padding:32px 40px">
<p style="font-size:26px;font-weight:700;color:#F6B48A">수업 설계의 전환 · 교구는 목업(시제품)</p>
<p style="font-size:52px;font-weight:900;line-height:1.2;color:#FFFFFF">기능 익히기</p>
<p style="font-size:52px;font-weight:900;line-height:1.2;color:#F6B48A">→ 문제 해결 데모</p>
<div style="background:#FFFFFF;border-radius:12px;padding:10px;display:flex;justify-content:center">{img('center',400,200,'아이디어에서 설계도, 시제품으로 이어지는 그림')}</div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px">
<div style="{CARD};padding:18px 32px"><p style="font-size:30px;font-weight:700;color:#0B4FB3">4일·12시간 파일럿 (2026.12 운영 예정)</p><p style="font-size:24px;line-height:1.4;color:#4A5568">「피지컬 AI 챌린지」 5~6학년: 바이브 코딩과 마이크로비트 기반 포니봇으로 학교·마을 문제를 해결합니다.</p></div>
<div style="{CARD};padding:18px 32px"><p style="font-size:30px;font-weight:700;color:#0B4FB3">AI를 쓰는 두 가지 방법</p><p style="font-size:24px;line-height:1.4;color:#4A5568">교사가 바이브 코딩으로 만든 AI 흉내 데모 앱, 그리고 자연어를 코드로 바꿔 주는 코딩 도우미 AI.</p></div>
<div style="{CARD};padding:18px 32px"><p style="font-size:30px;font-weight:700;color:#0B4FB3">그 밖의 프로젝트</p><p style="font-size:24px;line-height:1.4;color:#4A5568">포니봇 미션레이스(센서 레이싱), 카미봇pi와 티처블머신, 로보독 팀 프로젝트.</p></div>
</div>
</div>
<p style="font-size:32px;font-weight:700;line-height:1.4">핵심: 코딩이 목표가 아니라, <span style="color:#B84A12">문제를 푸는 아이디어</span>를 보여 주는 도구로 교구를 씁니다.</p>
{foot("출처: 동래교육지원청 발명교육센터 2026 교육과정 안내. 12월 과정은 파일럿으로 운영할 계획입니다.",15)}''',
'[13:30–14:45] 마지막 현장 사례는 제가 담당하는 동래발명교육센터입니다. 예전 수업은 교구의 기능을 익히고 코딩해서 작동을 확인하는 데서 끝나기 쉬웠습니다. 지금은 순서를 바꿉니다. 먼저 해결할 문제가 있고, 그 해결 아이디어를 보여 주는 데모, 즉 목업을 만들기 위해 피지컬 교구를 씁니다. 12월에는 4일, 12시간짜리 피지컬 AI 챌린지를 파일럿 프로그램으로 운영할 계획입니다. AI를 쓰는 방법은 두 가지입니다. 교사가 바이브 코딩으로 AI처럼 작동하는 데모 앱을 만들어 주는 것, 그리고 자연어를 코드로 바꿔 주는 코딩 도우미 AI로 복잡한 판단까지 교구에 구현하는 것입니다. AI 흉내 데모는 학생에게 따로 밝히지 않고 쓰며, 오늘은 선생님들께 이런 방식으로 응답하는 시스템의 구조를 알려 드리는 것입니다. 앞서 말씀드린 리터러시 관점에서는 수업 뒤에 구조를 밝히는 단계를 둘지 고민할 지점입니다.'))

# 16 implications
im=[("리터러시를 활동 안에 넣기","만들기 전에 묻고(데이터·한계·책임), 만든 뒤 따져 봅니다."),
("규칙에서 학습으로, 한 칸씩","A→B→C 순서로 얹어 교사와 학생의 부담을 줄입니다."),
("연수는 수업 설계 중심으로","기기 가입·조작 안내가 아니라 내용·교수법·AI 지식을 함께 다루는 실무 밀착형 연수."),
("안전한 도구와 환경부터","개인정보·안전 필터, 정지 방법을 갖춘 교구와 도구를 학교와 교육청이 함께 마련.")]
imh="".join(f'<div style="display:flex;flex-direction:row;align-items:center;gap:20px;{CARD};padding:12px 28px"><div style="width:52px;height:52px;border-radius:26px;background:{["#0B4FB3","#E8742A","#2FA36B","#5B8DEF"][i]};color:#FFFFFF;font-size:30px;font-weight:900;text-align:center;line-height:52px">{i+1}</div><div style="flex:1"><p style="font-size:32px;font-weight:900">{a}</p><p style="font-size:24px;line-height:1.4;color:#4A5568">{b}</p></div></div>' for i,(a,b) in enumerate(im))
write('impl',sec('impl',f'''{head("7 · 시사점과 제안","네 가지를 먼저 합시다")}
<div style="display:flex;flex-direction:row;align-items:center;gap:32px">
{img('impl',440,369,'네 방향을 가리키는 이정표와 로봇')}
<div style="flex:1;display:flex;flex-direction:column;gap:14px">{imh}</div>
</div>
{foot("시사점은 자료 조사와 현장 경험을 바탕으로 한 발표자의 제안입니다. 3번은 제미나이 보고서의 ‘AI-TPACK 중심 연수’ 제안과 같은 방향입니다.",16)}''',
'[14:45–16:15] 시사점과 제안입니다. 하나, 리터러시를 따로 가르치지 말고 활동 안에 넣습니다. 만들기 전에 묻고 만든 뒤 따져 봅니다. 둘, 규칙에서 학습으로 한 칸씩 올라갑니다. 셋, 교사 연수는 기기 가입과 조작 안내가 아니라 내용, 교수법, AI 지식을 함께 다루는 수업 설계 중심이어야 합니다. 넷, 개인정보와 안전을 갖춘 도구와 환경을 학교와 교육청이 함께 마련해야 합니다. 이 네 가지는 자료와 현장 경험을 바탕으로 한 제 제안입니다.'))

# 17 start
sc=[("1단계","말로 해 보기","자동문·신호등·에어컨에서 감지·판단·실행을 찾고 ‘규칙일까, AI일까?’ 묻습니다."),
("2단계","화면에서 규칙 만들기","블록 코딩으로 ‘조건이 맞으면 움직이는’ 규칙을 만들고, 규칙이 틀리는 경우를 찾아봅니다."),
("3단계","작은 로봇 + 학습 한 가지","학년에 맞는 교구 하나로 시작하고, 익숙해지면 티처블머신처럼 학습하는 판단을 하나 더합니다.")]
sch="".join(f'<div style="flex:1;{CARD};padding:22px 28px;display:flex;flex-direction:column;gap:8px"><p style="font-size:24px;font-weight:700;color:#B84A12">{a}</p><p style="font-size:34px;font-weight:900">{b}</p><p style="font-size:25px;line-height:1.4;color:#4A5568">{c}</p></div>' for a,b,c in sc)
write('start',sec('start',f'''{head("8 · 내일 시작하기","내일 시작하는 3단계")}
<div style="display:flex;flex-direction:row;align-items:center;gap:32px">
{img('start',560,244,'세 개의 디딤돌을 오르는 학생과 로봇')}
<div style="flex:1;{BAND};padding:28px 40px;display:flex;flex-direction:column;gap:10px"><p style="font-size:26px;font-weight:700;color:#F6B48A">옆 선생님과 30초</p><p style="font-size:38px;font-weight:900;line-height:1.35;color:#FFFFFF">우리 학교에서 ‘감지·판단·실행’이 보이는 물건 한 가지는?</p></div>
</div>
<div style="display:flex;flex-direction:row;gap:20px">{sch}</div>
{foot("발표자의 수업 제안입니다. 학교 여건에 맞게 조정하세요.",17)}''',
'[16:15–18:15] 내일 무엇을 하면 될까요. 먼저 30초만 옆 선생님과 이야기해 보시죠. 우리 학교에서 감지, 판단, 실행이 보이는 물건 한 가지, 자동문이든 에어컨이든 좋습니다. (30초 뒤) 이것이 1단계입니다. 2단계는 화면에서 조건이 맞으면 움직이는 규칙을 만들고 규칙이 틀리는 경우를 찾아보는 것, 3단계는 학년에 맞는 교구 한 가지로 시작해서 익숙해지면 학습하는 판단을 하나 더하는 것입니다. 한 번에 다 갖추려 하지 않으셔도 됩니다. 한 단계씩, 교구 한 가지씩입니다.'))

# 18 safety
sf=[("멈춤","정지 버튼이나 전원 차단 방법을 먼저 정합니다."),("구역","움직이는 범위를 정하고 안전 구역을 둡니다."),("데이터","카메라·마이크로 얻은 정보는 개인정보일 수 있어 범위를 정합니다."),("확인","결과는 교사가 확인하고, 실행 허락은 사람이 합니다. AI의 답도 한 번 의심합니다.")]
sfh=[f'<div style="flex:1;{CARD};padding:20px 28px;display:flex;flex-direction:column;gap:8px"><p style="font-size:36px;font-weight:900;color:#0B4FB3">{a}</p><p style="font-size:25px;line-height:1.4;color:#4A5568">{b}</p></div>' for a,b in sf]
write('safety',sec('safety',f'''{head("8 · 안전과 책임","움직이는 AI는 멈추는 법을 먼저 정합니다")}
<div style="display:flex;flex-direction:row;align-items:center;gap:32px">
<div style="flex:1;display:flex;flex-direction:column;gap:20px"><div style="display:flex;flex-direction:row;gap:20px">{sfh[0]}{sfh[1]}</div><div style="display:flex;flex-direction:row;gap:20px">{sfh[2]}{sfh[3]}</div></div>
{img('safety',400,322,'방패와 정지 표지')}
</div>
{foot("수업 안전 점검은 발표자의 정리입니다. 학교와 교육청의 안전 지침이 우선합니다.",18)}''',
'[18:15–19:00] 마지막으로 안전입니다. 움직이는 AI는 멈추는 법을 먼저 정합니다. 정지 버튼이나 전원 차단, 움직이는 범위, 카메라와 마이크가 모으는 정보의 범위, 그리고 결과를 교사가 확인하고 실행은 사람이 허락하는 것입니다. 안전은 리터러시와 같은 말입니다. 학생이 AI의 결과를 한 번 의심해 보는 습관이 가장 오래 가는 안전장치입니다. 이 점검은 제 정리이니 학교와 교육청의 안전 지침을 우선해 주세요.'))

# 19 closing
write('closing',sec('closing',f'''<p style="font-size:32px;font-weight:700;color:#F6B48A">감지 · 판단 · 실행, 그리고 질문하기</p>
<h1 style="font-size:96px;font-weight:900;line-height:1.2;color:#FFFFFF">우리 교실에서,<br>한 가지부터 시작합니다</h1>
<p style="max-width:1000px;font-size:44px;font-weight:500;line-height:1.4;color:#B9C6E4">모든 학생이 AI를 경험하는 일은 교사의 작은 시작에서 출발합니다.</p>
<div style="position:absolute;left:1220px;top:250px">{img('closing',560,420,'손을 흔드는 학생과 로봇')}</div>
{foot("감사합니다 · 박재현 · 내성초등학교",19,True)}''',
'[19:00–20:00] 정리합니다. 감지, 판단, 실행, 그리고 질문하기. 이 네 가지로 시작하면 어떤 교구로도 수업을 설계할 수 있습니다. 교육과정과 교육부 방침이 말하는 AI 리터러시는 결국 로봇이 틀렸을 때 왜 틀렸는지 묻는 일에서 시작합니다. 모든 학생이 AI를 경험하는 일은 우리 교실의 작은 시작에서 출발합니다. 감사합니다. (질문이 있으면 해당 슬라이드로 돌아가 답합니다.)',dark=True,gap=40,pad='128px 128px 160px',extra='justify-content:center;'))

# 20 sources
L=[("https://www.etoday.co.kr/news/view/2523982","교육부, 모두를 위한 인공지능(AI) 인재양성 방안(2025.11.10) · 이투데이 보도"),
("https://www.etoday.co.kr/news/view/2523891","이투데이, AI 중점학교 2000곳으로 늘린다, 교육과정도 전면 개편(2025.11.10)"),
("https://www.moe.go.kr/upload/filedown/2026_business_plan_press_release.pdf","교육부, 2026년 업무계획 보도자료(2025.12.12)"),
("https://www.heraldk.com/article/2026030819000030069","헤럴드경제, AI 중점학교 1141개 운영 시작(2026.3.8)"),
("https://www.hangyo.com/mobile/article.html?no=106819","한국교육신문, AI중점학교 속도 내는데 학교 준비는 아직(2026.7.8)"),
("https://hangyo.com/mobile/article.html?no=105730","한국교육신문 칼럼, 초등 AI 교육이 시기상조라고?(2025.11.5)"),
("https://www.hangyo.com/mobile/article.html?no=109594","한국교육신문, 교사 63% 수업·평가에 AI 활용(KICE 연구리포트 제13호, 2026.10.7)"),
("https://www.etoday.co.kr/news/view/2493911","이투데이, AI 교과서 교육자료 격하 앞두고(2025.8.4) · 풀뉴스, 교총 설문 3,485명(2025.7.28)"),
("https://gcedclearinghouse.org/en/node/146445","UNESCO, AI competency framework for students(2024)"),
("https://edtechinnovationhub.com/news/european-commission-and-oecd-set-19-ai-literacy-competences-for-schools","EC·OECD, AI Literacy Framework(2026.6, EdTech Innovation Hub 해설)"),
("https://microbit.org/news/2024-11-20/teaching-and-learning-about-ai-with-the-microbit/","micro:bit Educational Foundation, Teaching and learning about AI with the micro:bit(2024.11.20)"),
("https://www.education.gov.au/download/19495/chinas-approach-ai-education-primary-and-secondary-schools/41945/document/pdf","호주 교육부, China’s approach to AI education in primary and secondary schools(2025)")]
sl="".join(f'<li><a href="{u}">{t}</a></li>' for u,t in L)
sl+='<li>AI4K12 Initiative(AAAI·CSTA) 5 Big Ideas · 교육부 고시 제2022-33호 초등학교 교육과정(2차 자료로 성취기준 확인)</li><li>내성초 보도자료·운영 계획, 동래교육지원청 발명교육센터 교육과정 안내(2026)</li><li>제미나이 딥리서치 보고서는 오류 점검 후 참고만 했고, 위 출처로 확인한 내용만 사용했습니다.</li>'
write('sources',sec('sources',f'''{head("부록","출처")}
<ul style="font-size:24px;line-height:1.5;color:#14213D">{sl}</ul>
{foot("정책 수치는 발표 전에 교육부·교육청 공식 공지로 한 번 더 확인하세요.",20)}''',
'발표하지 않는 부록 슬라이드입니다. 질문이 나오면 출처로 돌아와 확인합니다.',gap=24))
