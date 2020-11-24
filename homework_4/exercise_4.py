import time

from homework_4 import common

# Create driver
chrome_driver = common.prepare_web_driver('chrome', screen_manipulation='maximize')

# Go to URL
chrome_driver.get("https://translate.google.com/")

# Type in hebrew
chrome_driver.find_element_by_xpath("//textarea").send_keys("שלום עולם")

# Some sleep so you can see it...
time.sleep(5)

# Close the driver
chrome_driver.close()
