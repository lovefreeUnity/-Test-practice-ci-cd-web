from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from custom_exception import CustomException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')  # 필수
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("http://localhost:8080")
# [Test1]
title = WebDriverWait(driver=driver,timeout= 10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/h1'))
)

if(title.text != "Wellcom to my app"):
    raise CustomException("title initalize error")

# [Test2] 버튼 찾기
button = WebDriverWait(driver=driver,timeout= 10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/button'))
)
button.click()

# [Test3] title 찾기
title = WebDriverWait(driver=driver,timeout= 10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/h1'))
)

if(title.text != "Hellow Love Free Unity"):
    raise CustomException("[Test3] title changed error")
driver.quit()