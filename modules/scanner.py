import requests
from bs4 import BeautifulSoup
import logging
import re

def scan_target(url):
    logging.info(f"🔍 Escaneando {url} en busca de formularios vulnerables a CSRF...")

    headers = {
        'User-Agent': 'Mozilla/5.0 (CSRF-Scanner-Aggressive/2025)',
        'Accept': 'text/html,application/xhtml+xml'
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        # Recolectar formularios
        forms = soup.find_all('form')
        iframes = soup.find_all('iframe')

        if not forms:
            logging.warning("⚠️ No se encontraron formularios directamente en la página.")

        for i, form in enumerate(forms):
            action = form.get('action') or url
            method = form.get('method', 'GET').upper()
            inputs = form.find_all('input')
            tokens = [inp.get('name') for inp in inputs if 'csrf' in (inp.get('name') or '').lower()]

            hidden_fields = [inp.get('name') for inp in inputs if inp.get('type') == 'hidden']
            has_csrf = any('csrf' in (name or '').lower() for name in hidden_fields)

            logging.info(f"\n  [FORM {i}] Acción: {action}")
            logging.info(f"           Método: {method}")
            logging.info(f"           Tokens CSRF detectados: {tokens}")
            logging.info(f"           Campos ocultos: {hidden_fields}")

            if not tokens and method == "POST":
                logging.warning("    🚨 Posible formulario vulnerable: POST sin token CSRF visible.")

        # Búsqueda en <meta> tags y JS embebido
        metas = soup.find_all('meta')
        meta_csrf = [m.get('name') for m in metas if 'csrf' in (m.get('name') or '').lower()]
        if meta_csrf:
            logging.info(f"🧠 Meta etiquetas CSRF encontradas: {meta_csrf}")

        scripts = soup.find_all('script')
        js_csrf = []
        for s in scripts:
            if s.string and re.search(r'csrf[_-]?token', s.string, re.IGNORECASE):
                js_csrf.append(s.string.strip()[:100])

        if js_csrf:
            logging.info(f"🧠 Tokens CSRF detectados en JavaScript embebido: {len(js_csrf)} ocurrencias.")

        if iframes:
            logging.info(f"🖼️  Detectados {len(iframes)} iframe(s): podrías escanearlos para formularios anidados.")

    except requests.RequestException as e:
        logging.error(f"❌ Error al conectar: {e}")
    except Exception as ex:
        logging.error(f"❌ Error general durante escaneo: {ex}")
