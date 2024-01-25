import time
import requests
import base64
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

RUCAPTCHA_KEY = ""
def get_captcha_image():
    captcha_element = driver.find_element(By.ID, "captcha_image")
    captcha_image = captcha_element.screenshot_as_png
    return base64.b64encode(captcha_image)

def solve_captcha(image_base64):
    url = "http://rucaptcha.com/in.php"
    params = {
        "key": RUCAPTCHA_KEY,
        "method": "base64",
        "body": image_base64.decode("utf-8"),
        "json": 1
    }
    response = requests.post(url, params=params)
    request_result = response.json()
    if request_result["status"] == 1:
        return request_result["request"]
    else:
        raise Exception("Не удалось отправить капчу")

def get_captcha_result(captcha_id):
    url = f"http://rucaptcha.com/res.php?key={RUCAPTCHA_KEY}&action=get&id={captcha_id}&json=1"
    for _ in range(10):  # Пытаемся получить результат до 10 раз
        response = requests.get(url)
        result = response.json()
        if result["status"] == 1:
            return result["request"]
        time.sleep(5)
    raise Exception("Не удалось получить результат капчи")

def report_bad_captcha(captcha_id):
    url = f"http://rucaptcha.com/res.php?key={RUCAPTCHA_KEY}&action=reportbad&id={captcha_id}&json=1"
    response = requests.get(url)
    result = response.json()
    if result["status"] != 1:
        print("Не удалось отправить жалобу на неверную капчу")

# Создаем список ссылок
with open('links.txt', 'r') as f:
    links = [line.strip() for line in f.readlines()]

# Запускаем браузер
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)

# Цикл по ссылкам
for link in links:
    # Заходим на страницу
    driver.get("https://eais.rkn.gov.ru/feedback/")

    # Ждем, пока элементы загрузятся
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Type")))

    # Выбираем тип обращения
    select = Select(driver.find_element(By.ID, "Type"))
    select.select_by_value("narcotics")

    # Ставим галочку
    checkbox = driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="MediaTypeU[]"][value="4"]')
    checkbox.click()

    # Вводим имя, фамилию, отчество
    driver.find_element(By.ID, "ReporterLastName").send_keys("Михайличенко")
    driver.find_element(By.ID, "ReporterFirstName").send_keys("Артём")
    driver.find_element(By.ID, "ReporterMiddleName").send_keys("Юрьевич")

    # Вводим email
    driver.find_element(By.ID, "ReporterEmail").send_keys("xdmaik.xdfox@gmail.com")
    checkbox = driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="SendNotification"][value="true"]')
    checkbox.click()

    # Вводим ссылку
    input_field = driver.find_element(By.ID, "ResourceUrl")
    input_field.send_keys(link)

    # Внутренний цикл для повторных попыток ввода капчи
    for attempt in range(5): # Максимум 5 попыток
        # Получаем изображение капчи
        captcha_image_base64 = get_captcha_image()

        # Отправляем изображение капчи на RuCaptcha
        captcha_id = solve_captcha(captcha_image_base64)

        # Получаем результат капчи
        captcha_result = get_captcha_result(captcha_id)

        # Вводим результат капчи в поле на веб-странице
        captcha_field = driver.find_element(By.ID, "captcha")
        captcha_field.clear()
        captcha_field.send_keys(captcha_result)

        # Нажимаем кнопку отправки
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()

        # Ждем появления сообщения об отправке
        try:
            message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "divMsgModalText")))
            if message.text == "Неверно указан защитный код":
                print("Неверно указан защитный код, отправляем жалобу на капчу")
                report_bad_captcha(captcha_id)
                continue # Повторяем попытку ввода капчи
            else:
                break # Выходим из внутреннего цикла, если капча введена правильно
        except TimeoutException:
            print("Не удалось найти сообщение об отправке. Повторяем отправку формы.")
            submit_button.click()

    print("Отправка сообщения завершена")

    time.sleep(5)
# Закрываем браузер
driver.quit()
