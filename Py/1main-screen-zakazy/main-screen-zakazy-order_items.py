import sqlite3

def main():
    # Подключаемся к базе данных (если файл orders.db не существует, он будет создан)
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    # Создадим таблицу order_items (позиции в заказе), если она ещё не существует
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    price DECIMAL
    )
    """)

    # Набор данных для вставки в таблицу order_items
    # Допустим, мы хотим связать позицию с некими "заказами" и "товарами"
    # (числовые значения order_id и product_id здесь условны).
    # "quantity" — количество товара, "price" — цена на позицию.
    order_items_data = [
    (1, 1001, 2, 24000.00),
    (2, 1002, 1, 7000.00),
    (3, 1003, 3, 4500.00),
    (4, 1004, 2, 9800.00),
    (5, 1005, 4, 11000.00),
    (6, 1001, 2, 14000.00),
    (7, 1006, 1, 5000.00),
    (8, 1002, 2, 6700.00),
    (9, 1007, 1, 12300.00),
    (10, 1008, 4, 5600.00),
    (11, 1009, 5, 10000.00),
    (12, 1010, 2, 9000.00),
    (13, 1011, 7, 17000.00),
    (14, 1012, 1, 4500.00),
    (15, 1013, 3, 12000.00),
    (16, 1014, 2, 6400.00),
    (17, 1011, 1, 12400.00),
    (18, 1015, 5, 15000.00),
    (19, 1016, 4, 20000.00),
    (20, 1017, 2, 2300.00),
    ]

    # Очищаем таблицу перед вставкой во избежание дублирования (опционально)
    cursor.execute("DELETE FROM order_items")

    # Вставляем записи в таблицу order_items
    cursor.executemany("""
    INSERT INTO order_items (
    order_id,
    product_id,
    quantity,
    price
    )
    VALUES (?, ?, ?, ?)
    """, order_items_data)

    conn.commit()

    # Считываем и выводим все записи из таблицы order_items
    cursor.execute("SELECT * FROM order_items")
    rows = cursor.fetchall()

    print("Содержимое таблицы order_items:\n")
    for row in rows:
        print(row)

    # Закрываем соединение
    cursor.close()
    conn.close()
if __name__ == "__main__":
    main()