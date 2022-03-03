# # ----------------------------------------------------------------------------------------------------
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import requests as rs
from selenium.webdriver import ActionChains
import urllib3
# from collections import OrderedDict
import time
import datetime
import logging
import logging.handlers
#

#'warning' 경고 무시하기
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Chrome driver에 대한 경로를 지정해줌
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome("C:/Users/ysou5/PycharmProjects/practice/selenium/chromedriver.exe",options=chrome_options)

#로그인 페이지 접속후 계정 입력 및 로그인 버튼 클릭
driver.implicitly_wait(5)
driver.get('https://www.irms.sktelecom.com/irms-operation-web/login/Login.do')
login_x_path="""/html/body/div[1]/div[1]/div[1]/button"""
login_x_path1="""/html/body/div[2]/div[1]/div/div[1]/div[2]"""
driver.find_element_by_name('userId').send_keys('SKN20001315')
driver.find_element_by_name('userPwd').send_keys('ys2933162!')
driver.find_element_by_xpath(login_x_path).click()
driver.find_element_by_xpath(login_x_path1).click()

#'통합RCU 감시'창으로 이동 → '전체기지국'에서 '수도권유선Infra팀' 선택하는 동작 수행
driver.switch_to.window(driver.window_handles[1])
driver.get_window_position(driver.window_handles[1])
driver.get('https://www.irms.sktelecom.com/irms-operation-web/integration/InteMain.do')
integration_x_path1="""/html/body/div[2]/div[2]/ul/li/input"""
integration_x_path2="""/html/body/div[2]/div[2]/ul/li/ul/li[1]/input"""
integration_x_path3="""/html/body/div[2]/div[3]/button"""
driver.find_element_by_xpath(integration_x_path1).click()
driver.find_element_by_xpath(integration_x_path2).click()
driver.find_element_by_xpath(integration_x_path3).click()

#'통합RCU감시'창에서 파싱진행
req = rs.get('https://www.irms.sktelecom.com/irms-operation-web/integration/InteMain.do',verify=False)
soup = BeautifulSoup(req.text, 'html.parser')
#RMS상의 경보에 대한 DataFrame 생성
result = {'station': [], 'alarm': [], 'li': []}
li_range = range(1, 55)

for li_value in li_range:
	try:
		total_info = driver.find_element_by_xpath(f'/html/body/div[4]/div[1]/div/ul/li[{li_value}]').get_attribute('title')

		if ' : ' in total_info:
			for info in total_info.split('\n'):
				station, alarm = info.split(' : ')
				result['station'].append(station)
				result['alarm'].append(alarm)
				result['li'].append(li_value)
	except Exception as e:
		print(e)
		continue

df_result = pd.DataFrame(result)
print(df_result)
print('')
print(df_result.info())

high_temp_site = df_result.loc[df_result.alarm.str.contains('고온')]
high_temp_site2 = high_temp_site.loc[high_temp_site.alarm.str.contains('전송망' or '전송망(485)')]
print(high_temp_site2)

high_temp_li = list(map(int, high_temp_site2['li']))

print(high_temp_li)

high_temp_station = list(map(str, high_temp_site2['station']))
high_temp_station1 = '[' + ', '.join(high_temp_station) + ']'
print('[' + ', '.join(high_temp_station) + ']')




def getTopRank(logger):
	logger.info('========================================')
	now = datetime.datetime.now()
	logger.info(now.strftime("%Y/%m/%d %H:%M:%S"))
	logger.info('========================================')
	for i in high_temp_li:
			time.sleep(2)

			title = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/ul/li[' + format(i) + ']')
			#<li>값에 해당되는 국소를 더블클릭해서 들어감
			action = ActionChains(driver)
			action.double_click(title).perform()
			#해당되는 국사 RCU 제어창에서 파싱진행
			driver.switch_to.window(driver.window_handles[2])
			driver.get_window_position(driver.window_handles[2])
			driver.get('https://www.irms.sktelecom.com/irms-operation-web/integration/BldDetailInfo.do')
			req = rs.get('https://www.irms.sktelecom.com/irms-operation-web/integration/BldDetailInfo.do', verify=False)
			soup = BeautifulSoup(req.text, 'html.parser')

			try:
				for j in range(1, 4):
					if driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[' + format(j) + ']/div/div/div[1]/h1/span').text in high_temp_station1:
						time.sleep(1)
						# 국사명 출력
						print(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[' + format(j) + ']/div/div/div[1]/h1/span').text, ":",end=' ')
						# print(result['station'] == high_temp_li,":", end=' ')
						for k in range(1, 5):
							high_temp_ext = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[' + format(j) + ']/div/div/div[4]/div/div/div[9]/table/tbody/tr[1]/td[' + format(k) + ']/span').text
							# 해당 국사내의 온도센서 #1~4의 온도값 반복문 통해 가져오기
							print(high_temp_ext,'/', end=' ')


			except NoSuchElementException:
				# 창닫기
				driver.close()
				# "통합 RCU 감시"창으로 돌아가기
				driver.switch_to.window(driver.window_handles[1])
				driver.get_window_position(driver.window_handles[1])
				print('\n')
				continue

	logger.info('')


daemon_flag = True;

reflash_time = 10;
#
#
def Daemon():
    # 1. 로거 인스턴스를 만든다
    logger = logging.getLogger('mylogger')

    # 포매터를 만든다
    # fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
    fomatter = logging.Formatter('')

    # 스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
    filedate = datetime.datetime.now()
    fileHandler = logging.FileHandler('./myLog_%s.log' % (filedate.strftime("%Y%m%d")))
    streamHandler = logging.StreamHandler()

    # 각 핸들러에 포매터를 지정한다.
    fileHandler.setFormatter(fomatter)
    streamHandler.setFormatter(fomatter)

    # 로거 인스턴스에 스트림 핸들러와 파일핸들러를 붙인다.
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)

    # 로거 인스턴스로 로그를 찍는다.
    logger.setLevel(logging.DEBUG)

    while (daemon_flag):
        getTopRank(logger);

        time.sleep(reflash_time)

if __name__ == '__main__':
    Daemon()

#--------------------------------------------------------------------------------------------
