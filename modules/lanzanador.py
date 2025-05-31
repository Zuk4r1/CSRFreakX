from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
import os

def launch_exploit(filepath):
    options = Options()
    options.headless = True
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Evasión básica
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                window.navigator.chrome = { runtime: {} };
                Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
                Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
            """
        })

        logging.info("🚀 Ejecutando exploit real en navegador headless (evasión activada)...")
        driver.get("file://" + os.path.abspath(filepath))
        time.sleep(5)  # Tiempo para que el exploit actúe

        # Captura de evidencia visual del resultado del exploit
        screenshot_path = filepath.replace(".html", "_evidencia.png")
        driver.save_screenshot(screenshot_path)
        logging.info(f"🖼️ Captura de pantalla guardada: {screenshot_path}")

    except (WebDriverException, TimeoutException) as e:
        logging.error(f"❌ Error al ejecutar el exploit en navegador headless: {e}")

    finally:
        driver.quit()
