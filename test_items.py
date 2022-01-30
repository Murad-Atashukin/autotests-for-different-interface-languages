link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
import time
def test_for_different_languages(browser):
    browser.get(link)
    time.sleep(5)

    button = browser.find_elements_by_css_selector("#add_to_basket_form > button")
    assert button is not None, 'Не нашел, та и фиг с ним, скоро на стройку'
    button.click()


