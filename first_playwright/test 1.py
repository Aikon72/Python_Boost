

def test_folder(driver):

    driver.goto("/")
    new_item_loc = "#tasks > div:nth-child(1) > span > a"
    driver.locator(new_item_loc).click()
