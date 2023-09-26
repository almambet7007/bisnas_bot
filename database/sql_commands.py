import sqlite3
from database import sql_query

class Database:
        def __init__(self):
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursor = self.connection.cursor()

        def sql_create_db(self):
            if self.connection:
                print("Database connected successfully")

            self.connection.execute(sql_query.create_fsm_table)
            self.connection.execute(sql_query.create_product_table)
            self.connection.commit()

        def sql_insert_fsm_table(self,telegram_id,nickname,admin_or_sot):
            self.cursor.execute(sql_query.insert_fsm_table,(None,telegram_id,nickname,admin_or_sot))
            self.connection.commit()

        def sql_select_fsm_table(self):
            return self.cursor.execute(sql_query.select_fsm_table).fetchall()

        def sql_insert_product_table(self, title, county, name, description, price, photo):
            self.cursor.execute(sql_query.insert_product_table, (None, title, county, name, description, price, photo))
            self.connection.commit()

        def sql_select_product_table(self):
            return self.cursor.execute(sql_query.select_product_table).fetchall()

        def sql_delete_product_table(self):
            self.cursor.execute(sql_query.delete_product_table)
            self.connection.commit()
