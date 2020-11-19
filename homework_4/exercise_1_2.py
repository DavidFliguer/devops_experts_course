import random
from homework_4 import common

# Create firefox driver
firefox_driver = common.prepare_web_driver('firefox', screen_manipulation='minimize')

# Create chromedriver
chrome_driver = common.prepare_web_driver('chrome', screen_manipulation='minimize')

# Add both drivers to a dictionary - Where the key is an integer ;-)
my_drivers = {
    1: firefox_driver,
    2: chrome_driver
}

# Randomly select one of the drivers
selected_driver = my_drivers[random.randint(1, 2)]

# Maximize
selected_driver.maximize_window()

# Go to URL
selected_driver.get("http://www.ynet.co.il")

# Set expected
expected_title = selected_driver.title

# Refresh driver
selected_driver.refresh()

# Get the actual
actual_title = selected_driver.title

# Assert
assert actual_title == expected_title

# Close firefox driver
firefox_driver.close()

# Close chrome driver
chrome_driver.close()
