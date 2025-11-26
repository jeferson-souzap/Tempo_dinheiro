import sqlite3
import datetime
from datetime import timedelta

from .config_db import LOCAL_DB_PATH


def inserir_registro(data, hora, minuto, tempo_total): 
    conn = sqlite3.connect(LOCAL_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tempo_registro (data, hora, minuto, tempo_total)
        VALUES (?, ?, ?, ?)
    ''', (data, hora, minuto, tempo_total))

    conn.commit()
    conn.close()

#não sei como usar ainda
def deletar_registro(registro_id):
    conn = sqlite3.connect(LOCAL_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM tempo_registro 
        WHERE id = ?
    ''', (registro_id,))

    conn.commit()
    conn.close()


def obter_registros():
    conn = sqlite3.connect(LOCAL_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tempo_registro')
    registros = cursor.fetchall()
    conn.close()
    return registros