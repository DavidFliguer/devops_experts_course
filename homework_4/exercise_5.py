from homework_4 import common

# Create chromedriver
chrome_driver = common.prepare_web_driver('chrome', screen_manipulation='maximize')

# Go to URL
chrome_driver.get("https://www.youtube.com")

# Type Bob Marley
chrome_driver.find_element_by_xpath("//input[@id='search']").send_keys("Bob Marley")

# Click on search
chrome_driver.find_element_by_xpath("//button[@id='search-icon-legacy']").click()

# Close the driver
chrome_driver.close()
