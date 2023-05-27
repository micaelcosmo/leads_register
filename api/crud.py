from connection import create_connection


def create_item(item):
    conn = create_connection()
    cursor = conn.cursor()
    # Lógica para criar um novo item no banco de dados
    # Exemplo:
    # cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", item['name'], item['price'])
    # conn.commit()


def read_item(item_id):
    conn = create_connection()
    cursor = conn.cursor()
    # Lógica para ler um item específico do banco de dados
    # Exemplo:
    # cursor.execute("SELECT * FROM items WHERE id=?", item_id)
    # row = cursor.fetchone()
    # return row


def update_item(item_id, updated_item):
    conn = create_connection()
    cursor = conn.cursor()
    # Lógica para atualizar um item no banco de dados
    # Exemplo:
    # cursor.execute("UPDATE items SET name=?, price=? WHERE id=?", updated_item['name'], updated_item['price'], item_id)
    # conn.commit()


def delete_item(item_id):
    conn = create_connection()
    cursor = conn.cursor()
    # Lógica para excluir um item do banco de dados
    # Exemplo:
    # cursor.execute("DELETE FROM items WHERE id=?", item_id)
    # conn.commit()
