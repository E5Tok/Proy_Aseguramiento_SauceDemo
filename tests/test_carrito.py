from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import guardar_evidencia, login_estandar


# CP-10: Agregar un producto al carrito
def test_agregar_producto_al_carrito(driver):
    login_estandar(driver)

    # Esperar a que cargue el catálogo
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Agregar el primer producto 
    boton_agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    boton_agregar.click()

    # Verificar que el botón cambió a "Remove"
    boton_remove = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "remove-sauce-labs-backpack"))
    )

    # Verificar que el contador del carrito muestra 1
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    guardar_evidencia(driver, "CP-10_agregar_al_carrito")

    assert boton_remove is not None, "FALLÓ: el botón no cambió a Remove"
    assert contador.text == "1", f"FALLÓ: el contador muestra {contador.text}, se esperaba 1"





    