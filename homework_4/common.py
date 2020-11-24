from selenium import webdriver
import platform


def prepare_web_driver(webdriver_type, implicit_wait_time=30, screen_manipulation=None):
    # Set driver as None
    driver = None

    # Create a webdriver
    if webdriver_type == 'chrome':
        if platform.system() == 'Windows':
            driver = webdriver.Chrome("chromedriver.exe")
        elif platform.system() == 'Linux':
            driver = webdriver.Chrome("./chromedriver")
    elif webdriver_type == 'firefox':
        driver = webdriver.Firefox(executable_path="./")

    # Set implicit wait
    driver.implicitly_wait(implicit_wait_time)

    if screen_manipulation == 'minimize':
        # Minimize
        driver.minimize_window()
    elif screen_manipulation == 'maximize':
        # Maximize
        driver.maximize_window()

    return driver
