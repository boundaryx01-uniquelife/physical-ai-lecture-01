# 초등 피지컬 AI 교육 강연 (2026.11.02, 부산시교육청 디지털미래교육과 교원 워크숍)

발표자: 박재현(내성초, 동래발명교육센터) · 20분 · 20장

- 덱: Slides 아티팩트 https://claude.ai/artifact/QGWSdBURGa8jQ4YR4bNeQi (v11, 비공개)
- `lecture/project/` : deck.json + slides/*.html (아티팩트 원본 파일)
- `gen/gen.py` : 슬라이드 HTML 생성기 (이미지 id는 아티팩트 `/_blob/<id>`)
- `art/` : SVG 삽화 (lib.py, lib2.py, scenes*.py, render*.py → png/ png2/). 최신 5종(cover/closing/literacy/limits/senseq)은 png2
- `ref/` : 제미나이·딥리서치 보고서와 오류 점검
- `cases/` : 내성초 사례 텍스트, `photos/` : 구조대 사진(얼굴 흐림본만; 원본 pose_raw 제외)

## 이어가기 메모
- 슬라이드 검증용 렌더링은 하지 않음(요청 시에만). 밀집 슬라이드 5·8·9·10·20 오버플로 육안 확인 필요
- gen.py 재실행 시 case-rescue.html에 문장 중복이 생김 → lecture/ 쪽 파일 기준 유지
- 이미지 교체: 제미나이/GPT 이미지를 받아 아티팩트에 asset 업로드 후 gen.py의 IMG id 교체
- 발표 전 확인: AI 디지털교과서 법적 지위, AI 중점학교 수치(1,141교 등)를 공식 공지로 재확인
- 슬라이드 15 발표자 노트의 'AI 모방 시연 고지' 문장 유지 여부 결정
