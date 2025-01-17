# "https://chzzk.naver.com/clips/KWydos957E" 웹사이트에서 클립 영상을 다운받는 프로그램입니다.
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

driver.get("https://chzzk.naver.com/clips/KWydos957E")
time.sleep(3)

# iframe으로 전환
iframe = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.TAG_NAME, "iframe"))
)
driver.switch_to.frame(iframe)

# video 태그 확인
# 비디오 태그를 명시적으로 기다림
try:
    url_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, 'video'))
    )
    print(url_element)
    # 비디오 URL 가져오기
    vid_url = url_element.get_attribute('src')

except Exception as e:
    print("Error:", e)
finally:
    print("비디오 URL:", vid_url)
    # 잠시 대기

# 제목 추출 -> 보완필요
# try:
#     # "si_desc" 클래스가 있는 <p> 태그 찾기
#     p_element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "si_desc"))
#     )
    
#     # 텍스트에서 <a> 태그를 제외하고 텍스트만 추출
#     text = p_element.text.strip()
    
#     # 출력
#     print(p_element)
#     print(p_element.text)
#     print("추출된 텍스트:", text)
    
# except Exception as e:
#     print("Error:", e)
# finally:
#     driver.quit()

# url로 영상 다운로드
from urllib.request import urlretrieve
urlretrieve(vid_url, 'a.mp4')

time.sleep(30)
driver.quit()
