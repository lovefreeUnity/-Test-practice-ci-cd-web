from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from custom_exception import CustomException
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("http://localhost:8080")
# [Test1]
try:
    title = WebDriverWait(driver=driver,timeout= 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/h1'))
    )
except TimeoutException:
    print("[Test1] Title 요소를 찾는 데 시간이 초과되었습니다.")
except Exception as e:
    print(f"[Test1] 다른 예외 발생: {e}")

if(title.text != "Wellcom to my app"):
    raise CustomException("title initalize error")

# [Test2] 버튼 찾기
try:
    button = WebDriverWait(driver=driver,timeout= 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/button'))
    )
except TimeoutException:
    print("[Test2] 요소를 찾는 데 시간이 초과되었습니다.")
except Exception as e:
    print(f"[Test2] 다른 예외 발생: {e}")
button.click()

# [Test3] title 찾기
try:
    title = WebDriverWait(driver=driver,timeout= 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/h1'))
    )
except TimeoutException:
    print("[Test3] 요소를 찾는 데 시간이 초과되었습니다.")
except Exception as e:
    print(f"[Test3] 다른 예외 발생: {e}")

if(title.text != "Hellow Love Free Unity"):
    raise CustomException("[Test3] title changed error")
driver.quit()