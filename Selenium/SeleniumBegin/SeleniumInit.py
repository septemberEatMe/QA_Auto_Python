from selenium import webdriver


driver = webdriver.Firefox(executable_path="../../../../SeleniumDrivers/geckodriver")
driver.get("http://www.google.com")