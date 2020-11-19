from homework_4 import common

# Create chromedriver
chrome_driver = common.prepare_web_driver('chrome', screen_manipulation='maximize')

# Go to URL
chrome_driver.get("https://translate.google.com/")

# Find same element using different locators
element_by_locator_1 = chrome_driver.find_element_by_tag_name("textarea")
element_by_locator_2 = chrome_driver.find_element_by_xpath("//*[@aria-label='Source text']")
element_by_locator_3 = chrome_driver.find_element_by_xpath("//*[@role='combobox']")

# Assert elements are the same
assert element_by_locator_1 == element_by_locator_2

# Assert elements are the same
assert element_by_locator_2 == element_by_locator_3

# Close the driver
chrome_driver.close()
