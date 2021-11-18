import pytest
from collections import Counter



# Присутствуют все питомцы.
def test_all_pets():
    card_pets = pytest.driver.find_element_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr')
    names = pytest.driver.find_element_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    number_of_pets = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').text
    number_of_pets = number_of_pets.split()
    number_of_pets = int(number_of_pets[1])
    pets_names = []
    for i in range(len(names)):
        assert names[i] != ''
        pets_names.append(names[i].text)
    assert number_of_pets == len(card_pets)

# У половины питомцев есть фото
def test_half_of_the_pets_have_photos():
    number_of_pets = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').text
    number_of_pets = number_of_pets.split()
    number_of_pets = int(number_of_pets[3])
    images = pytest.driver.find_element_by_xpath("//*[@id='all_my_pets']/table/tbody/tr/th/img")
    names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    photo = []
    for i in range(len(names)):
        photo.append(images[i].get_attribute('src'))

    photo = Counter(photo)
    assert photo[''] < number_of_pets / 2

# У всех питомцев есть имя, возраст и порода.
def test_pets_names_age_breed():
   names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
   age = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[3]')
   breed = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[2]')

   for i in range(len(names)):
      assert names[i].text != ''
      assert age[i].text != ''
      assert breed[i].text != ''

# У всех питомцев разные имена
def test_all_pets_different_names():
    names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    name = []
    for i in range(len(names)):
        name.append(names[i].text)
    duplicate_names = Counter(name)
    for key in duplicate_names:
        assert duplicate_names[key] == 1
