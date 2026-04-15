# Real-Spinning Lunch Roulette: Decision-Making & Analytics Platform
🍱 우리 뭐 먹지? 진짜 도는 런치룰렛
- 본 프로젝트는 룰렛 돌리기와 실시간 유저 행동 데이터 분석 시스템을 결합한 통합 솔루션입니다.
    - 유저들에게는 쉽고 재밌는 선택 경험을 제공, 관리자에겐 수집된 데이터로 또 다른 가치를 제공하는 지능형 대시보드.

🛠️ Logic & Tech Stack
- Core Logic
    - Physics-Mimic Animation: CSS @keyframes와 cubic-bezier를 활용하여 실제 룰렛의 감속 및 정지 메커니즘을 완벽하게 구현.
    - Stealth Admin Access: URL 파라미터(?view='manage')를 통한 은닉형 진입점 설계 및 st.secrets 기반의 이중 인증(MFA) 보안 체계 구축.
    - Geographic Analysis Engine: 접속 IP를 실시간 트래킹하여 위도·경도 데이터로 변환, 사용자 지역 분포를 지도(Map) 인터페이스에 시각화.
    - User Retention Intelligence: IP 기반 코호트 분석(Cohort Analysis) 로직을 통해 일별 재방문율(Retention)을 산출하고 사용자 고착도를 데이터로 증명.

🛰 Tech Stack
- Languages: Python, CSS3, HTML5, JavaScript
- Frontend: Streamlit (Dynamic Dashboard UI), Plotly, Seaborn
- Data Engine: Pandas (Time-series Analysis), GeoPy/Requests (IP Geolocation)
- Cloud Infrastructure: Google Sheets API, Streamlit Cloud, GitHub Actions (Server Poking)

✨ Key Features
1. Interactive Decision Support
    - Base64 Roulette UI: 무중단 이미지 스트리밍으로 실제 룰렛과 동일한 물리적 회전 경험 제공.
    - Map Integration: 당첨 메뉴 확정 후 네이버/카카오 지도 API를 통한 실시간 주변 식당 큐레이션.

2. Advanced Admin Dashboard (Admin Only)
    - Real-time Log Monitoring: Google Sheets와 연동된 실시간 접속 로그 트래킹 및 검색/필터링 기능.
    - Activity Heatmap: 요일/시간대별 IP접속 패턴을 히트맵으로 시각화하여 사용자가 가장 배고픈 골든 타임(Golden Time) 분석.
    - Retention Dashboard: * Daily Cohort: 신규 방문자 대비 재방문자의 비율을 히트맵 형식으로 산출.
    - Popularity Analytics: 당첨 빈도 상위 메뉴 데이터 시각화로 점심 트렌드 파악.

# Dev Log: High-Level Engineering
🔒 Stealth & Security
- 일반 사용자에게 노출되지 않는 관리자 모드를 구현하기 위해 URL Query Parameter 제어 로직을 적용했습니다. 이는 불필요한 리소스 노출을 막고, 관리자 전용 대시보드가 실제 서비스 성능에 영향을 주지 않도록 설계되었습니다.

📊 Data Transformation
- 비정형 로그 데이터를 시계열(Time-series) 데이터로 가공하는 파이프라인을 구축했습니다. 특히 Pandas의 pivot_table과 resample 기능을 활용하여 원본 로그로부터 코호트 매트릭스를 실시간으로 생성하는 로직을 최적화했습니다.

🌍 Geolocation Mapping
- IP 기반 위치 정보 수집 시 발생할 수 있는 Latency를 최소화하기 위해 비동기 처리 및 예외 처리 로직을 강화하여, 분석 페이지 로딩 속도를 유지하면서도 정확한 지리적 분포도를 구현했습니다.

👨‍💻 Developer: Dave
- Focus: 재미기반 유저의 효율적인 의사결정 프로세스 및 유저 데이터 실시간 대쉬보드 구현.
- Philosophy: "이용 할 수록 데이터가 쌓이고 이는 더 많은 가치 창출에 기여한다."

# Quick Start
1. 저장소 복제 및 라이브러리 설치
 - git clone https://github.com/YourName/Lunch-Roulette.git
 - pip install -r requirements.txt

2. 접근 방법
 - streamlit run app6.py
