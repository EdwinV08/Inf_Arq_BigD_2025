# Inf_Arq_BigD_2025

# 📊 Proyecto de Ingesta de Datos en Big Data  

Este proyecto realiza la extracción de datos desde una API pública, los almacena en una base de datos SQLite y genera evidencias complementarias en formatos CSV y TXT. Además, cuenta con una automatización mediante GitHub Actions, que ejecuta el proceso diariamente de forma programada.  

## 🛠 Tecnologías Utilizadas  
- Python 3.9+ (para la ingesta de datos)  
- SQLite3 (para el almacenamiento de datos)  
- Pandas (para la manipulación y exportación de datos)  
- GitHub Actions (para la automatización del proceso)  
- GitHub Codespaces (para el desarrollo en la nube)  

## 📌 Estructura del Proyecto  
[nombre_apellido]  
├── setup.py                      # Script opcional para instalación de dependencias  
├── README.md                      # Documentación del proyecto  
├── .github  
│   └── workflows  
│       └── bigdata.yml            # Configuración de GitHub Actions  
└── src  
    ├── static  
    │   ├── auditoria  
    │   │   └── ingestion.txt      # Archivo de auditoría  
    │   ├── db  
    │   │   └── ingestion.db       # Base de datos SQLite  
    │   └── xlsx  
    │       └── ingestion.xlsx     # Archivo de muestra  
    └── ingestion.py               # Script de ingesta de datos  

## 🚀 Configuración y Ejecución Manual  
Si deseas ejecutar el script manualmente en tu computadora o en GitHub Codespaces, sigue estos pasos:  

### 1️⃣ Clonar el Repositorio  
```bash  
git clone https://github.com/usuario/nombre_apellido.git  
cd nombre_apellido  
