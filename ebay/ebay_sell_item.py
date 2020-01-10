from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def makeListing(driver, itemName, itemDescription, itemPrice):
    searchBarEditText = driver.find_element_by_id("smac_complete")
    searchBarEditText.clear()
    searchBarEditText.send_keys(itemName)

    driver.find_element_by_id("hero-keyword_searchBox-2[0]").click()
    driver.minimize_window()
    pass