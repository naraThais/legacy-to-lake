import requests
import sqlite3
import os

# URL da API
API_URL = "http://localhost:3001/pedidos"

# Caminho para o banco de dados
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "data.db")

# 1. Requisição para a API
response = requests.get(API_URL)
if response.status_code != 200:
    print("Erro ao acessar a API:", response.status_code)
    exit()

pedidos = response.json()

# 2. Conectar ao banco SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Excluir tabela se ela já existir
cursor.execute("DROP TABLE IF EXISTS pedidos")

# 3. Criar a tabela corretamente
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY,
        cliente_id INTEGER,
        produto TEXT,
        valor REAL
    )
""")
# 4. Inserir os pedidos
for pedido in pedidos:
    cursor.execute("""
        INSERT OR REPLACE INTO pedidos (id, cliente_id, produto, valor)
        VALUES (?, ?, ?, ?)
    """, (pedido["id"], pedido["clienteId"], pedido["produto"], pedido["valor"]))

print(pedidos)


# 5. Salvar e fechar
conn.commit()
conn.close()

print("Pedidos extraídos e salvos com sucesso!")
