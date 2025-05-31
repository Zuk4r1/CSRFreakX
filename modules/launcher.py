from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import logging
import time
import os

def launch_exploit(filepath):
    # Configurar opciones avanzadas para el navegador headless con evasión
    options = Options()
    options.headless = True
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = None  # Ensure driver is defined
    try:
        # Iniciar Chrome con WebDriver Manager para mayor compatibilidad
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        # Anti-detección adicional con script inyectado
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                window.navigator.chrome = { runtime: {} };
                Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
                Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
            """
        })

        logging.info("🚀 Ejecutando exploit real en navegador headless (modo stealth activado)...")
        driver.get("file://" + os.path.abspath(filepath))
        time.sleep(5)

        # Captura de evidencia del resultado del exploit
        screenshot_path = filepath.replace(".html", "_proof.png")
        driver.save_screenshot(screenshot_path)
        logging.info(f"📸 Evidencia capturada: {screenshot_path}")

    except WebDriverException as e:
        logging.error(f"❌ Error al ejecutar el exploit: {e}")

    finally:
        if driver is not None:
            driver.quit()
