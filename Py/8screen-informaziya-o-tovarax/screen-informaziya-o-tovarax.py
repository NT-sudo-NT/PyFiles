import sqlite3

def main():
    # Подключаемся к базе данных.
    # Если нужно, чтобы база не сохранялась на диске,
    # можно заменить "orders.db" на ":memory:".
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    # Создаём таблицу products, если она ещё не существует
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR(255),
    product_description VARCHAR(255),
    status VARCHAR(50),
    quantity INT,
    unit_price REAL
    )
    """)

    # Данные для вставки в таблицу products
    products_data = [
    ("Samsung Galaxy S23 Ultra", "Мобильный телефон", "Под заказ", 8, 96999.00),
    ("Nike Air Max 270 React", "Спортивная обувь", "Под заказ", 56, 17800.00),
    ("Яблоко красное горное", "Свежее яблоко", "Под заказ", 34, 66.00)
    ]

    # На всякий случай очистим таблицу перед вставкой (для повторных запусков)
    cursor.execute("DELETE FROM products")

    # Добавляем записи в таблицу products
    cursor.executemany("""
    INSERT INTO products (
    product_name,
    product_description,
    status,
    quantity,
    unit_price
    )
    VALUES (?, ?, ?, ?, ?)
    """, products_data)
    conn.commit()

    # Получаем все записи из таблицы products
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    # Выводим записи в консоль
    print("Содержимое таблицы products:\n")
    for row in rows:
        print(row)

    # Закрываем соединение
    cursor.close()
    conn.close()
if __name__ == "__main__":
    main()