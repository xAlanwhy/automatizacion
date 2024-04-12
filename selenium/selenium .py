from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
import pytest
import os
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\\chrome\\chromedriver.exe"

options = webdriver.ChromeOptions()


@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    yield driver
    driver.quit()


def save_captura_pantalla(driver, name):
    captura_pantalla = "D:\\ITLA\\7mo Cuatrimestre\\Programacion 3\\Automatizacion\\selenium"
    if not os.path.exists(captura_pantalla):
        os.makedirs(captura_pantalla)

    captura_pantalla_s = os.path.abspath(captura_pantalla)
    print(f"Guardando captura de pantalla en: {captura_pantalla_s}")

    timestamp = time.strftime('%Y%m%d%H%M%S')
    captura_pantalla_file = os.path.join(captura_pantalla_s, f"{name}_{timestamp}.png")
    driver.save_screenshot(captura_pantalla_file)
    return captura_pantalla_file


# Initialize the driver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://store.steampowered.com/login/?redir=&redir_ssl=1&snr=1_4_4__global-header")

# Find username and password elements
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='_2eKVn6g5Yysx9JmutQe7WV']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responsive_page_template_content']/div[3]/div[1]/div/div/div/div[2]/div/form/div[2]/input")))
username.clear()
username.send_keys("alan2467")
password.clear()
password.send_keys("bernabe02")
time.sleep(5)
# Save screenshot
save_captura_pantalla(driver, "steam_login")

# Find login button and click
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='responsive_page_template_content']/div[3]/div[1]/div/div/div/div[2]/div/form/div[4]/button")))
login_button.click()

# Wait for a while
time.sleep(5)

# Save screenshot
save_captura_pantalla(driver, "steam_store")


searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="store_nav_search_term"]')))
searchbox.clear()
searchbox.send_keys("Call of duty")
searchbox.send_keys(Keys.ENTER)
# Save screenshot
save_captura_pantalla(driver, "steam_search")
time.sleep(5)



#chat users
driver.get("https://steamcommunity.com/chat/")
time.sleep(5)
# Save screenshot
save_captura_pantalla(driver, "steam_chat")


#profile 
driver.get("https://steamcommunity.com/profiles/76561198260036021//")
time.sleep(5)
# Save screenshot
save_captura_pantalla(driver, "steam_profile")


if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
    
# Close the driver
driver.close()

