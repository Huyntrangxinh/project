# menu_model.py

import sqlite3

class MenuModel:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path

    def get_menu(self):
        """
        Fetch all menu items from the 'menus' table.
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        # Create table if it doesn't exist (for demo purposes)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS menus (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT
            )
        """)

        # Optional: Insert sample data if the table is empty (for demo)
        cursor.execute("SELECT COUNT(*) FROM menus")
        count = cursor.fetchone()[0]
        if count == 0:
            sample_data = [
                ("Classic Cheeseburger", 8.99, "Juicy beef patty, cheese, lettuce, tomato."),
                ("Veggie Wrap", 7.49, "Tortilla, grilled veggies, hummus."),
                ("Caesar Salad", 6.99, "Romaine lettuce, Caesar dressing, croutons."),
                ("Grilled Chicken Sandwich", 9.49, "Chicken breast, lettuce, tomato."),
                ("French Fries", 3.49, "Crispy fries with ketchup.")
            ]
            cursor.executemany("INSERT INTO menus (name, price, description) VALUES (?, ?, ?)", sample_data)
            connection.commit()

        # Now fetch the menu items
        cursor.execute("SELECT id, name, price, description FROM menus")
        results = cursor.fetchall()

        connection.close()

        # Convert the results into a list of dictionaries
        menu_items = []
        for row in results:
            item_id, name, price, description = row
            menu_items.append({
                "id": item_id,
                "name": name,
                "price": price,
                "description": description
            })

        return menu_items

    def store_menu(self, name, price, description):
        """
        Insert a new menu item into the 'menus' table.
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        # Insert a new record into the 'menus' table
        cursor.execute(
            """
            INSERT INTO menus (name, price, description)
            VALUES (?, ?, ?)
            """,
            (name, price, description)
        )

        connection.commit()
        connection.close()

