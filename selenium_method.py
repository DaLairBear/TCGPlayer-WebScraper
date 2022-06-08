from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("E:\Downloads\chromedriver.exe")
driver.get("https://prices.tcgplayer.com/price-guide")
driver.implicitly_wait(20)
driver.find_element(By.CLASS_NAME, "dfwid-close").click()


Magic = {}

def get_card_info():
    select = Select(driver.find_element(By.ID, "set"))
    selected_option = select.first_selected_option
    title = selected_option.text
    print(title)
    Magic[f'{title}'] = {}

    table = driver.find_element(By.CSS_SELECTOR, 'table')
    x = 0
    for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
        Magic[f'{title}'][f'{x}'] = {}
        for cell in row.find_elements(By.CSS_SELECTOR, 'a'):
            # print(cell.text)
            Magic[f'{title}'][f'{x}']['Card_Name'] = cell.text
        for cell in row.find_elements(By.CLASS_NAME, 'thumbnail'):
            href = cell.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            # print(href)
            Magic[f'{title}'][f'{x}']['Card_URL'] = href
        for cell in row.find_elements(By.CLASS_NAME, "marketPrice"):
            # print(cell.text)
            Magic[f'{title}'][f'{x}']['Card_Market_Price'] = cell.text
        print(Magic)
        x += 1


get_card_info()
print(Magic)


driver.quit()