from selenium import webdriver
import time

d = webdriver.Chrome('/Users/xiaolongxia/Downloads/chromedriver')
time.sleep(2)
d.get('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4')
time.sleep(20)
d.maximize_window()
var =1
while var== 1:
    target = d.find_element_by_xpath("//*[@class ='prev']/following-sibling::span/a")
    d.execute_script("arguments[0].scrollIntoView();", target)
    target.click()


