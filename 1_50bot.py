# "https://zzzscore.com/1to50/#" 웹사이트에서 1~50번 까지 자동으로 클릭하는 프로그램입니다.
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

driver.get("https://zzzscore.com/1to50/#")
driver.implicitly_wait(300)

# 버튼 찾기
btns = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[*]')

print(len(btns))
print(btns[0].text)

# 1~50번 까지 자동으로 클릭
num = 1

while num <= 50 :
    for btn in btns:
        if btn.text == str(num):
            btn.click()
            num += 1

# 잠시 대기
time.sleep(30)

# 브라우저 종료
#driver.quit()

# /html/body/div[1]/div[2]/div[3]/div[1]/span
# //*[@id="grid"]
