from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import guardar_evidencia, login_estandar


# CP-14: Completar una compra con datos válidos.
def test_checkout_completo(driver):
    # 1. Login
    login_estandar(driver)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # 2. Agregar un producto al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # 3. Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
    )

    # 4. Iniciar checkout
    driver.find_element(By.ID, "checkout").click()

    # 5. Llenar el formulario 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    driver.find_element(By.ID, "first-name").send_keys("Juan")
    driver.find_element(By.ID, "last-name").send_keys("Pérez")
    driver.find_element(By.ID, "postal-code").send_keys("01001")
    driver.find_element(By.ID, "continue").click()

    # 6. Verificar la pantalla de resumen (Overview)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_info"))
    )
    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    guardar_evidencia(driver, "CP-14_checkout_resumen")

    # 7. Finalizar la compra
    driver.find_element(By.ID, "finish").click()

    # 8. Verificar el mensaje de éxito
    mensaje_exito = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    guardar_evidencia(driver, "CP-14_checkout_confirmacion")

    assert "Thank you for your order" in mensaje_exito.text, "FALLÓ: no se confirmó la compra"
    print(f"✅ CP-14 PASÓ. {total}")





    