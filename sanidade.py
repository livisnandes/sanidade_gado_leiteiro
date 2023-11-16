import datetime
import random
import sqlite3

# Conectar ao banco de dados (substitua 'nome_do_banco.db' pelo nome do seu banco de dados)
conn = sqlite3.connect('nome_do_banco.db')
c = conn.cursor()

# Criar tabela para armazenar dados de sanidade do gado leiteiro
c.execute('''
          CREATE TABLE IF NOT EXISTS sanidade_gado_leiteiro (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              data_registro TEXT,
              temperatura REAL,
              sintomas TEXT,
              tratamento TEXT
          )
          ''')

# Função para adicionar um novo registro de sanidade do gado leiteiro
def adicionar_registro_sanidade(temperatura, sintomas, tratamento):
    data_registro = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO sanidade_gado_leiteiro (data_registro, temperatura, sintomas, tratamento) VALUES (?, ?, ?, ?)",
              (data_registro, temperatura, sintomas, tratamento))
    conn.commit()
    print(f"Registro de sanidade do gado leiteiro adicionado.")

# Função para consultar registros de sanidade por período
def consultar_sanidade_por_periodo(data_inicial, data_final):
    c.execute("SELECT * FROM sanidade_gado_leiteiro WHERE data_registro BETWEEN ? AND ?",
              (data_inicial, data_final))
    rows = c.fetchall()
    for row in rows:
        print(row)

# Exemplo de uso das funções
temperatura_gado = random.uniform(37.0, 40.0)  # Temperatura do gado em graus Celsius (um exemplo aleatório)
sintomas_gado = "Tosse e espirros"  # Sintomas observados (um exemplo fixo)
tratamento_gado = "Administração de antibiótico"  # Tratamento aplicado (um exemplo fixo)
adicionar_registro_sanidade(temperatura_gado, sintomas_gado, tratamento_gado)

# Consultar registros de sanidade para o último mês
data_atual = datetime.datetime.now()
data_inicial = (data_atual - datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
data_final = data_atual.strftime("%Y-%m-%d %H:%M:%S")
consultar_sanidade_por_periodo(data_inicial, data_final)

# Fechar a conexão com o banco de dados
conn.close()
