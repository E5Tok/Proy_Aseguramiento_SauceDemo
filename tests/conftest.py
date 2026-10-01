import pytest
from selenium import webdriver
import os

URL = "https://www.saucedemo.com"
CARPETA_EVIDENCIA = os.path.join(os.path.dirname(__file__), "..", "evidencia")


@pytest.fixture
def driver():
    """Se ejecuta antes y después de cada prueba: abre y cierra el navegador."""
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv
    drv.quit()


def guardar_evidencia(driver, nombre_caso):
    """Guarda una captura de pantalla con el nombre del caso de prueba."""
    os.makedirs(CARPETA_EVIDENCIA, exist_ok=True)
    ruta = os.path.join(CARPETA_EVIDENCIA, f"{nombre_caso}.png")
    driver.save_screenshot(ruta)
    print(f"📸 Evidencia guardada: {ruta}")


def login_estandar(driver):
    """Función reutilizable: hace login con standard_user."""
    driver.get(URL)
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()




    