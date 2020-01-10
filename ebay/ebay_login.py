from selenium import webdriver


def login(driver, username, password):

    assert "Sign in or Register | eBay" in driver.title

    usernameEditText = driver.find_element_by_id("userid")
    usernameEditText.clear()
    usernameEditText.send_keys(username)

    passwordEditText = driver.find_element_by_id("pass")
    passwordEditText.clear()
    passwordEditText.send_keys(password)

    driver.find_element_by_id("sgnBt").click()
    pass