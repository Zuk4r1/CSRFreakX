import logging

def setup_logging():
    log_format = '%(asctime)s.%(msecs)03d - [%(levelname)s] - %(module)s: %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    
    logging.basicConfig(
        level=logging.DEBUG,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.FileHandler("csrfreakx.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

    logging.info("🔥 Iniciando CSRFreakX - Scanner y Explotador Avanzado de CSRF 2025...")
