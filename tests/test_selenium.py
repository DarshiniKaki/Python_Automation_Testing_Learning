from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_google_search():
    driver = webdriver.Chrome()

    driver.get("https://www.google.com")
    driver.implicitly_wait(5)

    search = driver.find_element(By.NAME, "q")
    search.send_keys("automation testing")
    search.send_keys(Keys.RETURN)
    print(driver.title)
    driver.quit()