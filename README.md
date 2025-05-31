# CSRFreakX

**CSRFreakX** es una herramienta ofensiva automatizada para la explotación avanzada de vulnerabilidades **Cross-Site Request Forgery (CSRF)**. Diseñada para **Bug Bounty, Red Teaming y pentesters profesionales**, permite detectar, explotar y automatizar ataques CSRF complejos con técnicas modernas de evasión, lógica de negocio y payloads maliciosos invisibles.

## 🧠 Características clave

☠️ Auto-explotación de endpoints vulnerables

☠️ Explotación de lógica subyacente y manipulación de privilegios

☠️ JavaScript EvilForm Caster (exploit en background sin interacción del usuario)

☠️ Stealth Mode: técnicas evasivas contra protecciones comunes (SameSite, Referer, etc.)

🔍 Modo Scan-Only para análisis pasivo

🚀 Auto-launch Exploit para pruebas reales en entornos controlados

📄 Generación de informes automáticos con payload incluido

## 🧪 Uso

```bash
python app.py -h
```

```bash
usage: app.py [-h] --target TARGET [--params PARAMS] [--method {GET,POST}] [--bypass] [--scan-only] [--launch] [--aggressive]

CSRFreakX - Real CSRF Auto-Exploiter

options:
  -h, --help           Mostrar ayuda
  --target TARGET      URL objetivo a escanear o atacar
  --params PARAMS      Parámetros de ataque (key1=val1&key2=val2)
  --method {GET,POST}  Método HTTP (por defecto POST)
  --bypass             Aplicar técnicas de evasión anti-CSRF
  --scan-only          Solo escanear sin explotar
  --launch             Lanzar el exploit automáticamente
  --aggressive         Modo agresivo con evasión avanzada y heurística

```

## 🎯 Ejemplos

**🔍 Solo escaneo pasivo:**
```bash
python app.py --target https://victima.com/endpoint --scan-only
```

**🛠️ Generar exploit manualmente:**

```bash
python app.py --target https://objetivo.com/delete_account --params "id=987"
```

**⚔️ Ejecutar ataque completo automáticamente:**

```bash
python app.py --target https://objetivo.com/actualizar --params "email=hacker@evil.com" --launch
```

**👁‍🗨 Modo sigiloso + evasión lógica:**

```bash
python app.py --target https://portal.secreto.com/transferir --params "monto=10000&to=attacker" --method POST --bypass --aggressive --launch
```

## 📄 Informes automáticos

Al finalizar un escaneo o ataque exitoso, CSRFreakX genera un informe en la carpeta informes/ con el siguiente contenido:

✅ Estado del endpoint (VULNERABLE o SEGURO)

📍 Target probado

📦 Parámetros utilizados

💉 Payload exploit generado

🧠 Observaciones sobre evasión o lógica explotada

## 🔐 Casos comunes de explotación

- Cambios de correo electrónico o contraseña sin token CSRF

- Eliminación de cuentas mediante enlaces o formularios

- Transferencias financieras sin protección adecuada

- Elevación de privilegios vía modificación de parámetros ID

- Explotación de lógica rota en formularios ocultos

## ✅ Estado del proyecto

💣 Estable, actualizado para 2025, probado en:

- Programas Bug Bounty de HackerOne y Bugcrowd

- Aplicaciones en React, Angular, Laravel, Django y Node.js

- Formularios tradicionales y SPA con backend RESTful

## ⚠️ Aviso legal

> CSRFreakX está destinada exclusivamente a auditorías autorizadas.
> El uso no ético o sin permiso en sistemas de terceros constituye un delito informático.
> El autor no se responsabiliza por daños derivados del mal uso de esta herramienta.

# 🤝 Contribuciones

Se aceptan pull requests, mejoras de código, integración con más fuentes OSINT y módulos de detección avanzados.
  <br />
	<br/>
      	<p width="20px"><b>Se aceptan donaciones para mantener este proyecto</p></b>
	      <a href="https://buymeacoffee.com/investigacq"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=investigacqc&button_colour=FF5F5F&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00" /></a><br />
      	<a href="https://www.paypal.com/paypalme/babiloniaetica"><img title="Donations For Projects" height="25" src="https://ionicabizau.github.io/badges/paypal.svg" /></a>
</div>

## ❤️ Créditos

> Autor: [Zuk4r1](https://github.com/Zuk4r1)  
> Licencia: MIT  
> Uso exclusivo para investigación ética y entornos controlados.
> Sígueme para más herramientas de Red Team y Bug Bounty.

# ¡Feliz hackeo! 🎯
