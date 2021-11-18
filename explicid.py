import pytest
from collections import Counter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_all_pets():
   card_pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')))
   names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')))
   number_of_pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div/div[1]'))).text
   number_of_pets = number_of_pets.split()
   number_of_pets = int(number_of_pets[3])
   pets_names = []
   for i in range(len(names)):
      assert names[i] != ''
      pets_names.append(names[i].text)
   assert number_of_pets == len(card_pets)


def test_half_of_the_pets_have_photos():
   number_of_pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div/div[1]'))).text
   number_of_pets = number_of_pets.split()
   number_of_pets = int(number_of_pets[3])
   images = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/th/img")))
   names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')))
   photo = []
   for i in range(len(names)):
      photo.append(images[i].get_attribute('src'))

   photo = Counter(photo)
   assert photo[''] < number_of_pets / 2

def test_pets_names_age_breed():
   names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[1]")))
   age = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[3]")))
   breed = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[2]")))

   for i in range(len(names)):
      assert names[i].text != ''
      assert age[i].text != ''
      assert breed[i].text != ''


def test_all_pets_different_names():
   names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')))
   name = []
   for i in range(len(names)):
      name.append(names[i].text)
   duplicate_names = Counter(name)
   for key in duplicate_names:
      assert duplicate_names[key] == 1