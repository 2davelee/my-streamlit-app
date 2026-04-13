#진짜 도는 런치룰렛 (Real-Spinning Lunch Roulette)
🍱 "오늘 뭐 먹지?" 고민을 한 방에 해결해주는 인터랙티브 점심 메뉴 추천 서비스입니다.

단순히 텍스트만 바뀌는 룰렛이 아니라, CSS Animation과 Streamlit을 결합하여 실제 회전하는 몰입감을 제공합니다.

✨ 핵심 기능 (Key Features)
진짜 돌아가는 룰렛 UI: st.markdown과 Base64 이미지 인코딩을 활용하여 브라우저에서 실제로 회전하는 애니메이션 구현.

동적 메뉴 관리: 사용자가 실시간으로 메뉴를 추가하거나 삭제하며 룰렛 판을 구성 가능.

당첨 결과 즉시 검색: 당첨된 메뉴를 바탕으로 네이버 지도 및 카카오 맵과 연동하여 주변 맛집 바로가기 버튼 제공.

데이터 로깅 (Optional): Google Sheets API를 통해 어떤 메뉴가 얼마나 당첨되었는지 데이터 히스토리 관리.

🛠️ 기술 스택 (Tech Stack)
Language:

Framework:

Design:  (Bezier-Curve Animation)

Environment:  /

🚀 시작하기 (Installation)
저장소 복제

git clone https://github.com/사용자명/레포이름.git
cd 레포이름
필수 라이브러리 설치

pip install -r requirements.txt
앱 실행

streamlit run app6.py
📂 프로젝트 구조 (Project Structure)
Plaintext
├── .streamlit/          # Streamlit 설정 및 테마
├── app6.py              # 메인 애플리케이션 파일 (최적화 버전)
├── requirements.txt      # 의존성 라이브러리 목록
└── README.md            # 프로젝트 문서
💡 개발 노트 (Dev Log)
1. 룰렛 회전 애니메이션 최적화
Streamlit의 리렌더링 특성 때문에 CSS 애니메이션이 끊기는 현상을 방지하기 위해, st.session_state로 회전 각도를 관리하고 placeholder.empty()를 통해 UI 깨짐을 방지했습니다.

2. 레이아웃 사수하기
CSS 스타일 블록을 상단에 고정하고 !important 태그를 활용하여, 메뉴가 늘어나거나 줄어들어도 결과 박스와 룰렛 이미지가 화면 중앙을 유지하도록 설계했습니다.

👤 Author
Dave AI Project Manager & Data Analytics Engineer 새벽의 사투 끝에 떡볶이와 부대찌개를 룰렛 위에 올리는 데 성공했습니다. 🎡