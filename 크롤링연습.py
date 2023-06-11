from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


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
wait = WebDriverWait(driver, 10)

ticket_button = driver.find_element(By.XPATH, "//a[contains(@onclick, 'goTicket')]")

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

iframe2 = wait.until(EC.presence_of_element_located((By.ID, "ifrmSeatDetail")))
driver.switch_to.frame(iframe2)


# select_seat_button = driver.find_element(By.XPATH, "//img[@alt='[R석] 1층-D블록7열-3']")


# 좌석 선택
find_seats = set()
count = 3
lane = 4
while len(find_seats) < 2:
    if count >= 12:
        lane +=1
        count = 3
    for i in range(count,count+2):
        if len(find_seats) >= 2: break
        
        try:
            seat_button = driver.find_element(By.XPATH, f"//img[@alt='[R석] 1층-C블록{lane}열-{i}']")
            find_seats.add(seat_button)
        except:
            count += 1
            find_seats.clear()

for seat in find_seats:
    seat.click()

driver.switch_to.parent_frame()
button = driver.find_element(By.XPATH, "//img[@alt='좌석선택완료 버튼']")
button.click()


