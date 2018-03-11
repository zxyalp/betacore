from selenium import webdriver

CHROME_DRIVER = "D:\\selenium\\chromedriver_2.29\\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
