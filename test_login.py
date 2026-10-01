from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# CP-01: Login exitoso con usuario estándar
def test_login_exitoso():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # 1. Ir a SauceDemo
        driver.get("https://www.saucedemo.com")

        # 2. Ingresar usuario válido
        driver.find_element(By.ID, "user-name").send_keys("standard_user")

        # 3. Ingresar contraseña válida
        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        # 4. Hacer clic en el botón de login
        driver.find_element(By.ID, "login-button").click()

        # 5. Esperar a que cargue la página de inventario
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        # 6. Verificar que el login fue exitoso (resultado esperado)
        assert "inventory" in driver.current_url, "FALLÓ: no se redirigió a inventory"
        print("✅ CP-01 PASÓ: Login exitoso, usuario redirigido a /inventory.html")

        # Pausa para que puedas ver el resultado antes de cerrar
        time.sleep(3)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_exitoso()








    