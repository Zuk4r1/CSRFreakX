import argparse
import traceback
from modules.scanner import scan_target
from modules.exploit_engine import generate_exploit
from modules.launcher import launch_exploit
from modules.utils import setup_logging
import datetime
import os


def print_banner():
    banner = """
               ▀▄▀▄▀▄ CSRFreakX ▄▀▄▀▄▀
    “Los formularios existen para ser traicionados.”

       ☠️ Auto-explotación de endpoints CSRF
       ☠️ Explotar la lógica subyacente
       ☠️ JavaScript EvilForm Caster
       ☠️ Stealth Mode Exploitation

    ↳ Hack the logic. Not the frontend.
    """
    print(banner)
    print("CSRFreakX - Herramienta desarrollada por @Zuk4r1\n")


def generar_informe(target, exploit_path, exito=True):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"informe_csrfreakx_{timestamp}.txt"
    ruta_archivo = os.path.join("informes", nombre_archivo)
    os.makedirs("informes", exist_ok=True)
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write("== INFORME CSRFreakX ==\n")
        f.write(f"Fecha y hora: {timestamp}\n")
        f.write(f"Objetivo: {target}\n")
        if exito:
            f.write("Resultado: VULNERABLE A CSRF\n")
            f.write(f"Exploit exitoso guardado en: {exploit_path}\n")
            with open(exploit_path, "r", encoding="utf-8") as exp:
                f.write("\n--- PAYLOAD EXPLOIT ---\n")
                f.write(exp.read())
        else:
            f.write("Resultado: No se detectaron vulnerabilidades CSRF.\n")
    print(f"[+] Informe generado: {ruta_archivo}")


if __name__ == '__main__':
    setup_logging()
    print_banner()
    parser = argparse.ArgumentParser(description='CSRFreakX - Real CSRF Auto-Exploiter')
    parser.add_argument('--target', required=True, help='URL objetivo para escanear o atacar')
    parser.add_argument('--params', help='Parámetros del ataque (ej: key1=val1&key2=val2)')
    parser.add_argument('--method', choices=['GET', 'POST'], default='POST', help='Método HTTP')
    parser.add_argument('--bypass', action='store_true', help='Aplicar técnicas de evasión')
    parser.add_argument('--scan-only', action='store_true', help='Solo escanear sin atacar')
    parser.add_argument('--launch', action='store_true', help='Lanzar el exploit automáticamente')
    parser.add_argument('--aggressive', action='store_true', help='Modo agresivo con evasión y trucos avanzados')

    args = parser.parse_args()

    params = args.params if args.params is not None else ""
    method = args.method if args.method is not None else "POST"
    bypass = args.bypass if args.bypass is not None else False
    aggressive = args.aggressive if args.aggressive is not None else False

    if args.scan_only:
        scan_target(args.target)
    else:
        print("[+] Generando exploit...")
        try:
            print(f"[DEBUG] target={args.target}, params={params}, method={method}, bypass={bypass}, aggressive={aggressive}")
            import inspect
            print(f"[DEBUG] generate_exploit signature: {inspect.signature(generate_exploit)}")
            exploit_result = generate_exploit(
                target=args.target,
                params=params,
                method=method,
                bypass=bypass,
                aggressive=aggressive
            )
            # Si el resultado parece ser código y no una ruta, lo guardamos en un archivo
            if isinstance(exploit_result, str) and ("const fs" in exploit_result or exploit_result.strip().startswith("<")):
                # Guardar el exploit en un archivo temporal
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                exploit_path = os.path.join("exploits", f"exploit_{timestamp}.js")
                os.makedirs("exploits", exist_ok=True)
                with open(exploit_path, "w", encoding="utf-8") as f:
                    f.write(exploit_result)
            else:
                exploit_path = exploit_result

            print(f"[+] Exploit generado: {exploit_path}")

            if args.launch:
                print("[+] Lanzando ataque real...")
                resultado = launch_exploit(exploit_path)
                if resultado:
                    generar_informe(args.target, exploit_path, exito=True)
                else:
                    generar_informe(args.target, exploit_path, exito=False)
            else:
                generar_informe(args.target, exploit_path, exito=True)
        except Exception as e:
            print(f"[!] Error al generar el exploit: {e}")
            traceback.print_exc()
