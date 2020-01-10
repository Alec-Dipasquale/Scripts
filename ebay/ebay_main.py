import re 
import credentials
import ebay_login
import ebay_sell_item
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")



driver = webdriver.Chrome(chrome_options=chrome_options)
driver.fullscreen_window()
driver.get('https://www.ebay.com/')
print("driver.page_source")

assert "Electronics, Cars, Fashion, Collectibles, Coupons and More | eBay"
# choice = input("What would you like to do?\nLogin_______0\n")

username = credentials.EBAY_USERNAME
password = credentials.EBAY_PASSWORD
print(username + " " + password)

driver.find_element_by_link_text("Sign in").click()
ebay_login.login(driver, username, password)


itemName = "Shorty Clutch Brake Levers for Yamaha YZF R1 R1M/S R3 R6 R125 R15 600R 750/1000R"
itemDescription = """ever's size: 147mm shorty

We can offer 10 kinds colors for the levers, BLACK GOLD SILVER RED ORANGE BLUE GREEN GRAY PINK PURPLE

8 colors for the adjusters,BLACK GOLD SILVER RED ORANGE BLUE GREEN GRAY

please don't forget to leave me message what colors you

 Machined CNC Billt 6061 T6 Aluminum

6 Position Lever Adjustment stainless steel fasteners

Precision Machined Pivot Bore To Ensure A Perfect Fit

7075 Type 3 Black Anodized Cam Block For Improved Longvity

Custom Cadmium Plated Springs & Brass Pivot Bushing

Stainless Steel Hardware"""
itemPrice = 19.46
driver.find_element_by_link_text("Sell").click()
ebay_sell_item.makeListing(driver, itemName, itemDescription, itemPrice)


