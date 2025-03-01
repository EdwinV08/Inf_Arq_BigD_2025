import requests
import sqlite3
import pandas as pd
import json
import os

# Configuración de rutas
DB_PATH = "src/static/db/ingestion.db"
CSV_PATH = "src/static/xlsx/ingestion.xlsx"
AUDIT_PATH = "src/static/auditoria/ingestion.txt"

# API Pública (Clima)
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m"

def fetch_data():
    """ Extrae datos de la API """
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def save_to_db(data):
    """ Guarda los datos en SQLite """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Crear tabla si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        time TEXT,
                        temperature REAL)''')

    # Insertar datos
    for i in range(len(data["hourly"]["time"])):
        cursor.execute("INSERT INTO weather (time, temperature) VALUES (?, ?)", 
                      (data["hourly"]["time"][i], data["hourly"]["temperature_2m"][i]))

    conn.commit()
    conn.close()

def export_to_csv():
    """ Exporta los datos a CSV """
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM weather", conn)
    df.to_excel(CSV_PATH, index=False)
    conn.close()

def generate_audit_log():
    """ Crea archivo de auditoría """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM weather")
    db_count = cursor.fetchone()[0]
    
    with open(AUDIT_PATH, "w") as f:
        f.write(f"Registros extraídos de la API: {len(fetch_data()['hourly']['time'])}\n")
        f.write(f"Registros almacenados en la base de datos: {db_count}\n")

    conn.close()

if __name__ == "__main__":
    print("Iniciando ingesta de datos...")
    data = fetch_data()
    if data:
        save_to_db(data)
        export_to_csv()
        generate_audit_log()
        print("Ingesta completada con éxito.")
    else:
        print("Error en la extracción de datos.")
