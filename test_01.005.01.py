import time


def test_new_pipeline(page):
    """локатор кнопки new item"""
    new_item_loc = "a[href='/view/all/newJob']"
    """Локатор кнопки Multibranch pipeline"""
    pipeline_multi_loc = "Freestyle project"
    """Локатор сообщения о пустом поле"""
    message_loc = "div#itemname-required"
    message = "» This field cannot be empty, please enter a valid name"

    page.goto("/")
    page.locator(new_item_loc).click()
    page.get_by_text(pipeline_multi_loc).click()
    """Проверка, что текст сообщения об ошибке появляется на странице"""
    assert  message in page.text_content(message_loc)
    time.sleep(1)
