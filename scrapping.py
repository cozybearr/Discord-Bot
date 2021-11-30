from selenium import webdriver
from time import sleep

key = input('Enter your key\n >>')
driver = webdriver.Chrome()
driver.implicitly_wait(5)


driver.get('https://www.youtube.com/results?search_query={}'.format(key))
print('URL:======================', driver.current_url)
print('Title:====================', driver.title)

# Find a first web element with video thumbnail on the page

# link_webelement = driver.find_element(
#     By.CSS_SELECTOR, 'div#contents ytd-item-section-renderer>div#contents a#thumbnail')


# Grab webelement's href
# links = link_webelement.get_attribute('href')]
# driver.save_screenshot('filename.png')


# print(links)
driver.close()
