import sqlite3
import datetime
from datetime import timedelta


LOCAL_DB_PATH = r'D:\#Mega\Jeferson - Dev\02 - Linguagens\Python\Tempo_dinheiro\db\time_tracker.db'


def criar_tabela():
    conn = sqlite3.connect(LOCAL_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS tempo_registro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data DATETIME DEFAULT CURRENT_TIMESTAMP,
                hora INTEGER NOT NULL,
                minuto INTEGER NOT NULL,                
                tempo_total datetime DEFAULT CURRENT_TIMESTAMP                   
            )
        ''')

    conn.commit()
    conn.close()



if __name__ == "__main__":
    criar_tabela()
    print("Tabela criada com sucesso.")