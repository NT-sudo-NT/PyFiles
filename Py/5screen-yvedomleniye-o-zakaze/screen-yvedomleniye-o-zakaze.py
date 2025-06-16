import sqlite3

def main():
    # Подключение к файлу БД (будет создан автоматически, если его нет).
    # Для тестовых целей можно использовать ":memory:",
    # чтобы хранить БД в оперативной памяти.
    conn = sqlite3.connect("notifications.db")
    cursor = conn.cursor()

    # Создаём таблицу notifications (уведомления) 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    notification_text TEXT,
    notification_date DATE,
    order_id INTEGER,
    settings VARCHAR
    )
    """)

    # Набор данных для вставки
    notifications_data = [
    ("Успешная оплата заказа", "2023-01-10", 20, "priority=normal"),
    ("Заказ отправлен",       "2023-02-15", 11, "priority=high"),
    ("Новая заявка",          "2023-09-01", None, "priority=low"),
    ]

    # Очищаем таблицу (на случай повторного запуска)
    cursor.execute("DELETE FROM notifications")

    # Добавляем записи в таблицу
    cursor.executemany("""
    INSERT INTO notifications (
    notification_text,
    notification_date,
    order_id,
    settings
    )
    VALUES (?, ?, ?, ?)
    """, notifications_data)
    conn.commit()

    # Извлекаем и выводим все записи из таблицы уведомлений
    cursor.execute("SELECT * FROM notifications")
    rows = cursor.fetchall()

    print("Содержимое таблицы notifications:\n")
    for row in rows:
        print(row)

    # Закрываем соединение
    cursor.close()
    conn.close()
if __name__ == "__main__":
    main()