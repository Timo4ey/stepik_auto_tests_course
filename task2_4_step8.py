from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from calc import calc

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение.
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

    assert price == True
    button = browser.find_element(By.ID, 'book')
    button.click()

    x = browser.find_element(By.ID, 'input_value')
    theAnswer = calc(x.text)

    form = browser.find_element(By.ID, 'answer')
    form.send_keys(theAnswer)

    submit = browser.find_element(By.ID, 'solve')
    submit.click()

    print(browser.switch_to.alert.text)

except Exception as ex:
    print(f"Error: {ex}")
finally:
    sleep(5)
    browser.quit()
