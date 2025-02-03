📁 estudio_medico/
│── 📁 app/                      # Código principal de la aplicación
│   │── 📁 static/                # Archivos estáticos (CSS, JS, imágenes)
│   │   │── 📁 img/ 

│   │   │── 📁 css/               # Estilos CSS
│   │   │   ├── styles.css        # Estilos generales
│   │   │── 📁 js/                # Scripts de JavaScript


│   │── 📁 templates/             # Archivos HTML (Frontend)
│   │   │── home.html            # Página de inicio (Home) 
│   │   │── login.html            # Página de inicio de sesión
│   │   │── panel_admin.html      # Panel de administrador
│   │   │── panel_secretario.html # Panel del secretario
│   │   │── panel_medico.html     # Panel del médico
│   │   │── panel_paciente.html   # Panel del paciente
│   │── 📁 routes/                # Módulos con rutas Flask
│   │   │── __init__.py           # Inicializa rutas
│   │   │── auth_routes.py        # Rutas de autenticación
│   │   │── admin_routes.py        # Rutas de usuarios 
│   │   │── paciente_routes.py      # Rutas de turnos médicos
│   │   │── medicos_routes.py
│   │   │── secretario_routes.py

│   │── 📁 models/                # Modelos de la base de datos
│   │   │── __init__.py           # Inicializa modelos
│   │   │── user_model.py         # Modelo de usuarios


│   │── config.py                 # Configuración de la base de datos y Flask
│   │── app.py                    # Punto de entrada de la app
│── config.py
│── init_bd.py

│── requirements.txt           # Dependencias del proyecto 

│── .venv                           # Variables de entorno (ej. DB_URL) 
│── run.py                         # Script para ejecutar la aplicación
│── README.md                      # Documentación del proyecto


# Plataforma de Gestión de Turnos Médicos

## Descripción
Este proyecto es una plataforma de gestión de turnos médicos desarrollada en el marco de un simulacro Scrum. Su objetivo es digitalizar y optimizar la administración de turnos en el Centro Médico Integral, mejorando la experiencia tanto para los profesionales de la salud como para los pacientes.

## Características Principales
- **Profesionales:**
  - Definir horarios de atención por día y franja horaria.
  - Configurar la duración de las consultas.
  - Marcar días no laborables por vacaciones o licencias.
  - Crear un perfil con nombre, especialidad, número de matrícula y obras sociales aceptadas.
  - Acceder a un calendario para visualizar turnos del día y semana.
  - Marcar asistencia de los pacientes a la consulta.

- **Pacientes:**
  - Buscar profesionales por especialidad, obra social o nombre.
  - Solicitar turnos eligiendo un profesional y un horario disponible.
  - Cancelar turnos con al menos 24 horas de anticipación.
  - Recibir recordatorios automáticos por email 24 horas antes de la consulta.
  - Acceder a su historial de turnos y gestionar cancelaciones.

- **Gestión de Turnos:**
  - Evita turnos superpuestos.
  - Libera turnos cancelados con anticipación.
  - Registra cancelaciones con información de quién canceló.
  
## Estructura del Proyecto
```
consultorio/
│── app/
│   │── __init__.py
│   │── app.py
│   │── config.py
│   │── routes.py
│── static/
│   │── css/
│   │── img/
│   │── js/
│── templates/
│── requirements.txt
│── README.md
```

## Tecnologías Utilizadas
- **Backend:** Flask
- **Frontend:** React 
- **Base de Datos:**  MySQL
- **Despliegue:** Planeado en entorno de producción


## Requisitos de Instalación
### Clonar el repositorio
```bash
git clone https://github.com/LourdesVidela/programacion4-losalfa.git
cd consultorio
```

### Crear y activar entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate    # En Windows
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

## Ejecución del Proyecto
```bash
flask run
```
Por defecto, la aplicación se ejecuta en `http://127.0.0.1:5000/`.
