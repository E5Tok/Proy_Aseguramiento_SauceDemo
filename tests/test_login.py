from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import URL, guardar_evidencia


def test_login_exitoso(driver):
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    guardar_evidencia(driver, "CP-01_login_exitoso")
    assert "inventory" in driver.current_url


def test_login_password_incorrecta(driver):
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("clave_incorrecta")
    driver.find_element(By.ID, "login-button").click()

    error = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    guardar_evidencia(driver, "CP-02_login_password_incorrecta")
    assert "Username and password do not match" in error.text
    assert "inventory" not in driver.current_url


def test_login_usuario_bloqueado(driver):
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    guardar_evidencia(driver, "CP-03_usuario_bloqueado")
    assert "locked out" in error.text.lower()
    assert "inventory" not in driver.current_url







    