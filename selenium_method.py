from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import json

driver = webdriver.Chrome("E:\Downloads\chromedriver.exe")
driver.get("https://prices.tcgplayer.com/price-guide")
driver.implicitly_wait(20)
driver.find_element(By.CLASS_NAME, "dfwid-close").click()


Magic = {}
set_list = []

def get_sets():
    select = Select(driver.find_element(By.ID, 'set'))
    select_list = select.options
    for option in select_list:
        set_list.append(option.get_attribute('value'))


def get_cards_in_set():
    driver.get(f'https://prices.tcgplayer.com/price-guide/magic/{set_list[2]}')
    # select = Select(driver.find_element(By.ID, "set"))
    # selected_option = select.first_selected_option
    # title = selected_option.text
    # print(title)
    Magic[f'{set_list[2]}'] = {}

    table = driver.find_element(By.CSS_SELECTOR, 'table')
    x = 0
    for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
        Magic[f'{set_list[2]}'][f'{x}'] = {}
        for cell in row.find_elements(By.CSS_SELECTOR, 'a'):
            # print(cell.text)
            Magic[f'{set_list[2]}'][f'{x}']['Card_Name'] = cell.text
        for cell in row.find_elements(By.CLASS_NAME, 'thumbnail'):
            href = cell.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            # print(href)
            Magic[f'{set_list[2]}'][f'{x}']['Card_URL'] = href
        x += 1
    
    magic = json.dumps(Magic)
    f = open("dict.json", "w")
    f.write(magic)
    f.close()




get_sets()
get_cards_in_set()

driver.quit()