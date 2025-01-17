# "http://zzzscore.com/color/" 색이 다른 버튼을 찾는 프로그램입니다.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # By 모듈 임포트
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
from collections import Counter

# ChromeDriver 경로 설정 (수동으로 경로를 설정하거나 webdriver-manager를 사용)
service = Service(ChromeDriverManager().install())  # webdriver-manager로 자동 설치
driver = webdriver.Chrome(service=service)

driver.get("http://zzzscore.com/color/")
driver.implicitly_wait(300)

# 버튼 찾기
btns = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div')

# 버튼 개수
# print(len(btns))
# print(btns[0].text)

# 다른 버튼이 어디에 있는지 분석하는 함수
def analysis():
    # 리스트 컴프리헨션 각 btn에서 배경색 추출하여 리스트에 저장
    btns_rgba = [btn.value_of_css_property('background-color') for btn in btns]
    # pprint(btns_rgba)

    # 버튼 배경색의 출현 빈도를 계산
    result = Counter(btns_rgba)
    # pprint(result)

    # 버튼 빈도가 1 이라면 출력 - 한 번만 나온 버튼이기 때문에
    for key, value in result.items():
        if value == 1:
            answer = key
            break
    else:
        answer = None
        print("정답을 찾을 수 없습니다.")

    # 버튼 빈도가 1인 버튼의 인덱스를 가진 버튼을 클릭
    if answer:
        index = btns_rgba.index(answer)
        btns[index].click()

# 프로그램 시작 후 60초 동안 진행
if __name__=="__main__":
    start = time.time()
    while time.time() - start <= 60:
        analysis()

# 잠시 대기
time.sleep(30)

# 브라우저 종료
#driver.quit()
