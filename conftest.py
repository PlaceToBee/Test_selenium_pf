import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:\projects\chromedriver.exe')
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    pytest.driver.find_element_by_id('email').send_keys('27591test@mail.ru')
    pytest.driver.find_element_by_id('pass').send_keys('27591test')
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    pytest.driver.find_element_by_xpath('/html/body/nav/button/span').click()
    pytest.driver.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[1]/a').click()

    yield

    pytest.driver.quit()