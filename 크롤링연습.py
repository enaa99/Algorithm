import random
import threading

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException, \
    JavascriptException, NoAlertPresentException, TimeoutException

from selenium.webdriver.chrome.service import Service

import re
import time
import os
import sys
import warnings
import logging

# 특정 포트에서 크롬실행 terminal에서 실행
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=/Users/enaJJJ/selenium/AutomationProfile &


# 크롬 드라이버 경로 설정
PATH = "/Users/eenaa/chromedriver"

# 크롬 드라이버 서비스 객체 생성
service = Service(PATH)

# 이미 열려있는 크롬 브라우저의 디버그 포트를 지정해줍니다.
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9222")

# 디버그 포트를 이용하여 크롬 드라이버를 생성합니다.
driver = webdriver.Chrome(service=service, options=options)

ticket_button = driver.find_element(by='xpath',value="//img[contains(@alt, '미클로시 페레니 & 피닌 콜린스 듀오 콘서트')]/ancestor::a")
ticket_button.click()

time.sleep(3)
# 날짜 선택
# iframe 요소를 찾을 때까지 10초 기다림

driver.switch_to.default_content()
try:
    iframe = driver.find_element(By.ID,'ifrmBookStep')
except:
    iframe = driver.find_element(By.ID,'ifrmBookStep')
driver.switch_to.frame(iframe)

# 변경된 값을 가진 요소를 클릭


# 회차 선택
time_selector = driver.find_element_by_css_selector('li.time:nth-child(2) > a:nth-child(1) > img:nth-child(1)')
time_selector.click()
time.sleep(1)

# 예매하기 버튼 클릭
book_button = driver.find_element_by_css_selector('#SmallNextBtn')
book_button.click()
time.sleep(1)

# 좌석 선택
seat_button = driver.find_element_by_css_selector('#ifrmSeat > div.seatL > ul > li:nth-child(2) > div > a')
seat_button.click()
time.sleep(1)

# 좌석 선택 완료 버튼 클릭
seat_select_button = driver.find_element_by_css_selector('#ifrmSeatDetail > div.wrap_bk_btn > a')
seat_select_button.click()
time.sleep(1)

# 매수 선택
ticket_num_selector = Select(driver.find_element_by_css_selector('#CountSelect'))
ticket_num_selector.select_by_visible_text('1')
time.sleep(1)

# 다음단계 버튼 클릭
next_button1 = driver.find_element_by_css_selector('#LargeNextBtn')
next_button1.click()
time.sleep(1)

# 생년월일 입력
birth_year = driver.find_element_by_css_selector('#YY')
birth_year.send_keys('YYYY')
birth_month = driver.find_element_by_css_selector('#MM')
birth_month.send_keys('MM')
birth_day = driver.find_element_by_css_selector('#DD')
birth_day.send_keys('DD')
time.sleep(1)

# 다음단계 버튼 클릭
next_button2 = driver.find_element_by_css_selector('#LargeNextBtn')
next_button2.click()
time.sleep(1)

# 무통장입금 선택
payment_option_button = driver.find_element_by_css_selector('#PayMethodList > li:nth-child(2) > label')
payment_option_button.click()
time.sleep(1)

# 입금 은행 선택
bank_selector = Select(driver.find_element_by_css_selector('#BankCode'))
bank_selector.select_by_visible_text('은행이름')
time.sleep(1)

# 다음단계 버튼 클릭
next_button3 = driver.find_element_by_css_selector('#LargeNextBtn')
next_button3.click()
time.sleep(1)

# 체크 버튼 클릭
check_button = driver.find_element_by_css_selector('#Agree')
check_button.click()
time.sleep(1)

# 결제하기 버튼 클릭
pay_button = driver.find_element_by_css_selector('#LargeNextBtn')
pay_button.click()