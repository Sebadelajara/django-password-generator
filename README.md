# 🔐 Django Password Generator

Proyecto simple construido con **Django** que permite generar contraseñas seguras de manera rápida y personalizada. Ideal para practicar conceptos clave del desarrollo web con Django, como vistas, rutas, formularios y plantillas.

## 🌐 Demo en vivo

➡️https://django-passwordgenerator.onrender.com/

## 🛠️ Características

- Generación de contraseñas aleatorias
- Personalización de:
  - Longitud de la contraseña
  - Inclusión de letras mayúsculas
  - Inclusión de caracteres especiales
  - Inclusión de números
- Interfaz sencilla y responsive
- Basado en Django (Python)

## 🚀 Tecnologías usadas

- [Python 3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- HTML5 + CSS3
- Bootstrap (opcional)

## 📦 Instalación local

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Sebadelajara/django-password-generator.git
   cd django-password-generator
   
2. Crea un entorno virtual:
   
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

3. Instala las dependencias:
   
pip install -r requirements.txt

4. Ejecuta el servidor:

python manage.py runserver

5. Abre tu navegador en http://127.0.0.1:8000

📁 Estructura del proyecto

django-password-generator/
│
├── generator/          # App principal
│   ├── templates/      # Plantillas HTML
│   └── views.py        # Lógica del generador
│
├── password_generator/ # Configuración del proyecto Django
│
├── static/             # Archivos CSS/JS estáticos
├── db.sqlite3          # Base de datos SQLite
└── manage.py           # Script de administración


👨‍💻 Autor
Sebastián de la Jara
LinkedIn
https://www.sebastiandelajara.dev/

📄 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.




