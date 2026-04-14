from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

try:
    print("🚀 데이브 엔진 2.0(룰렛 전용) 기상 시도...")
    # 룰렛 앱 URL로 변경하세요!
    driver.get("https://our-lunch.streamlit.app/") 
    
    # 1. 초기 로딩 대기 (스트림릿 서버가 깨어나는 시간 고려)
    time.sleep(40) 
    
    # 2. iframe 진입 (Streamlit 메인 컨텐츠는 보통 첫 번째 iframe에 있음)
    try:
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        if len(iframes) > 0:
            driver.switch_to.frame(0)
            print("🌐 iframe 진입 성공")
    except:
        print("⚠️ iframe 진입 건너뜀 (메인 프레임 시도)")

    # 3. 버튼 탐색 전략 (최대 10회 시도)
    target_button = None
    for i in range(10):
        # 스트림릿 버튼은 내부에 <p> 태그로 텍스트가 들어가는 경우가 많음
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"🔄 [{i+1}차 시도] 발견된 버튼 개수: {len(buttons)}")
        
        for btn in buttons:
            btn_text = btn.text
            print(f"   - 발견된 버튼 텍스트: '{btn_text}'")
            # "룰렛 돌리기" 키워드가 포함된 버튼 찾기
            if "룰렛" in btn_text or "시작" in btn_text:
                target_button = btn
                break
        
        if target_button:
            print(f"🎯 타겟 버튼 발견! ({target_button.text})")
            break
            
        print("😴 로딩 중... 10초 더 대기합니다.")
        time.sleep(10)

    # 4. 동작 수행
    if target_button:
        # 일반 클릭이 안 먹힐 때를 대비해 JavaScript 강제 클릭 실행
        driver.execute_script("arguments[0].click();", target_button)
        print("✅ 성공: 룰렛 엔진이 완전히 깨어났습니다!")
        
        # 로그 수집 스레드가 작동할 수 있도록 클릭 후 잠시 대기
        time.sleep(5) 
    else:
        print("❌ 실패: 버튼 요소를 찾지 못했습니다.")

except Exception as e:
    print(f"❌ 에러 발생: {e}")

finally:
    driver.quit()
    print("💤 엔진 종료.")