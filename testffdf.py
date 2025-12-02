import time


def test_new_pipeline(page):
    new_item_loc = "a[href='/view/all/newJob']"
    pipeline_multi_loc = "Freestyle project"
    #pipeline_multi_loc = "New Item"
    message_loc = "div#itemname-required"
    message = "» This field cannot be empty, please enter a valid name"

    page.goto("/")
    page.locator(new_item_loc).click()
    page.get_by_text(pipeline_multi_loc).click()
    assert  message in page.text_content(message_loc)
    time.sleep(1)
