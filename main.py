from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from config import USERNAME, PASSWORD

options = Options()
options.add_argument("--start-maximized")  # Делает окно браузера большим
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("https://github.com/login")

username_field = driver.find_element(By.ID, "login_field")
password_field = driver.find_element(By.ID, "password")

username = USERNAME
password = PASSWORD

username_field.send_keys(username)
password_field.send_keys(password)

# Нажимаем Enter для входа
password_field.send_keys(Keys.RETURN)

time.sleep(3)

# Проверка входа
if "github.com" in driver.current_url:
    print("✅ Вход выполнен успешно!")
else:
    print("❌ Что-то пошло не так!")

driver.get("https://github.com/new")
time.sleep(2)

try:
    repo_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[class*='prc-components-Input']"))
    )
    repo_name = ("TestSelenium")
    repo_name_input.send_keys(repo_name)
except:
    print("❌ Ошибка: Поле имени репозитория не найдено!")
    driver.quit()
    exit()


is_private = False  # Изменить на False, если нужен публичный репозиторий

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "visibilityGroup"))
)


if is_private:
    private_repo = driver.find_element(By.XPATH, "//input[@name='visibilityGroup' and @value='private']")
    private_repo.click()
else:
    public_repo = driver.find_element(By.XPATH, "//input[@name='visibilityGroup' and @value='public']")
    public_repo.click()

time.sleep(2)

create_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create repository')]"))
)
create_button.click()

time.sleep(5)
driver.quit()


