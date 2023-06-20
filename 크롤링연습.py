from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains


# 특정 포트에서 크롬실행 terminal에서 실행
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=/Users/eenaa/selenium/AutomationProfile &


# 크롬 드라이버 경로 설정
PATH = "/Users/eenaa/chromedriver"

# 크롬 드라이버 서비스 객체 생성
service = Service(PATH)

# 이미 열려있는 크롬 브라우저의 디버그 포트를 지정해줍니다.
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9222")




# 디버그 포트를 이용하여 크롬 드라이버를 생성합니다.
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 300)

driver.refresh()
ticket_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@onclick, 'goTicket')]")))


main_window_handle = driver.current_window_handle

ticket_button.click()

time.sleep(1)
# 링크나 버튼을 클릭하여 새로운 창을 엽니다.
# 새로운 창이 열리면 여러 개의 창 핸들이 있을 수 있습니다.

# 모든 창 핸들을 얻습니다.
all_window_handles = driver.window_handles

new_window_handle = None
for window_handle in all_window_handles:
    if window_handle != main_window_handle:
        new_window_handle = window_handle
        break
    

driver.switch_to.window(new_window_handle)




# iframe으로 전환
iframe = wait.until(EC.presence_of_element_located((By.ID, "ifrmBookStep")))
driver.switch_to.frame(iframe)


# 회차 선택
time_selector = driver.find_element(By.ID,'CellPlayDate')
time_selector.click()
driver.switch_to.parent_frame()


# Next 버튼 클릭
book_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='btn' and @id='LargeNextBtn']/a[@id='LargeNextBtnLink']/img[@id='LargeNextBtnImage']")))
book_button.click()



# iframe으로 전환
iframe1 = wait.until(EC.presence_of_element_located((By.ID, "ifrmSeat")))
driver.switch_to.frame(iframe1)

iframe_seat = wait.until(EC.presence_of_element_located((By.ID, "ifrmSeatView")))
driver.switch_to.frame(iframe_seat)

coords = "54,50,71,49,78,19,128,20,135,49,152,50,137,5,69,6"
element = wait.until(EC.presence_of_element_located((By.XPATH, f"//area[@coords='{coords}']")))

driver.execute_script("arguments[0].click();", element)

alert = wait.until(EC.alert_is_present())
time.sleep(3)


driver.switch_to.parent_frame()

iframe = wait.until(EC.presence_of_element_located((By.ID, "ifrmSeat")))
driver.switch_to.frame(iframe)


iframe2 = wait.until(EC.presence_of_element_located((By.ID, "ifrmSeatDetail")))
driver.switch_to.frame(iframe2)



#[B석] 합창석-F블록1열-1 -> 1열 5 / 2열 10 / 3열 14

# 좌석 선택
# 합창석
find_seats = set()
count = 1
lane = 1
while len(find_seats) < 2:
    if lane == 1 and count >=6:
        lane +=1
        count = 1
    elif lane == 2 and count >= 11:
        lane +=1
        count =1
    elif lane == 3 and count >=15:
        break
        
    try:
        seat_button = driver.find_element(By.XPATH, f"//img[@alt='[B석] 합창석-F블록{lane}열-{count}']")
        seat_button.click()
        find_seats.add(seat_button)
    except:
        count = count
    
    count += 1


driver.switch_to.parent_frame()
button = driver.find_element(By.XPATH, "//img[@alt='좌석선택완료 버튼']")
button.click()




# R석
# find_seats = set()
# count = 1
# lane = 1
# while len(find_seats) < 2:
#     if count >= 12:
#         lane +=1
#         count = 1
        
#     try:
#         seat_button = driver.find_element(By.XPATH, f"//img[@alt='[R석] 1층-C블록{lane}열-{count}']")
#         seat_button.click()
#         find_seats.add(seat_button)
#     except:
#         count = count
    
#     count += 1


# driver.switch_to.parent_frame()
# button = driver.find_element(By.XPATH, "//img[@alt='좌석선택완료 버튼']")
# button.click()


