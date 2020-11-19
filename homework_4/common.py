from selenium import webdriver


def prepare_web_driver(webdriver_type, implicit_wait_time=30, screen_manipulation=None):
    # Set driver as None
    driver = None

    # Create a webdriver
    if webdriver_type == 'chrome':
        driver = webdriver.Chrome("chromedriver.exe")
    elif webdriver_type == 'firefox':
        driver = webdriver.Firefox(executable_path="geckodriver.exe")

    # Set implicit wait
    driver.implicitly_wait(implicit_wait_time)

    if screen_manipulation == 'minimize':
        # Minimize
        driver.minimize_window()
    elif screen_manipulation == 'maximize':
        # Maximize
        driver.maximize_window()

    return driver
