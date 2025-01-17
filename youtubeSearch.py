# 유튜브 검색어 창에 입력하는 프로그램입니다.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # By 모듈 임포트
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver 경로 설정 (수동으로 경로를 설정하거나 webdriver-manager를 사용)
service = Service(ChromeDriverManager().install())  # webdriver-manager로 자동 설치
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com/")
driver.implicitly_wait(100)
# 검색창이 로드될 때까지 대기
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/div[1]/form/input'))
)

# 검색어 창에 '파이썬' 입력
search_box.send_keys('파이썬')
search_box.send_keys('\n')  # 엔터키로 검색 실행

# 잠시 대기
time.sleep(10)

# 브라우저 종료
#driver.quit()
