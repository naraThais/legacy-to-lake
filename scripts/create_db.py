import sqlite3
import os

# Caminho para o banco
db_path = os.path.join('db', 'produtos.db')

# Conecta (ou cria)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Cria tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    preco REAL
)
''')

# Insere dados simulados
produtos = [
    (1, 'Notebook', 3500.00),
    (2, 'Mouse', 80.50),
    (3, 'Teclado', 120.00)
]

cursor.executemany('INSERT INTO produtos VALUES (?, ?, ?)', produtos)

# Salva e fecha
conn.commit()
conn.close()

print("✅ Banco SQLite criado com sucesso.")
