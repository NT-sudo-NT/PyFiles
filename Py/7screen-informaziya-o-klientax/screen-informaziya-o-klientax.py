import sqlite3

def main():
    # Подключение (или создание) файла базы данных
    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()

    # Создаём таблицу clients, если её ещё нет
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name VARCHAR,
    organization VARCHAR,
    status VARCHAR,
    phone_number VARCHAR,
    email VARCHAR,
    description VARCHAR,
    responsible VARCHAR
    )
    """)

    # Для удобства при повторном запуске скрипта очистим таблицу
    cursor.execute("DELETE FROM clients")

    # Данные для вставки
    clients_data = [
    ("Дмитрий", "ТехноСервис", "Активный",      "+79250689110", "dmitriy13@gmail.com", "Менеджер по закупкам",    "Новиков Тимофей"),
    ("Василий", "ЭкоПродукты", "Активный",      "+7925028348",  "vasiliy.a@gmail.com", "Директор по развитию",    "Новиков Тимофей"),
    ("Олег Уваров", "СтройГарант", "Активный",  "+79917174850", "oleg.uvarov@mail.com","Начальн. отдела снабж.", "Новиков Тимофей")
    ]

    # Добавляем записи в таблицу
    cursor.executemany("""
    INSERT INTO clients (
    client_name,
    organization,
    status,
    phone_number,
    email,
    description,
    responsible
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, clients_data)
    conn.commit()

    # Выбор и вывод всех записей таблицы clients
    cursor.execute("SELECT * FROM clients")
    rows = cursor.fetchall()

    print("Содержимое таблицы clients:\n")
    for row in rows:
        print(row)

    # Закрываем соединение
    cursor.close()
    conn.close()
if __name__ == "__main__":
    main()