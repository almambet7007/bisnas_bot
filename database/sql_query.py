create_fsm_table = """
CREATE TABLE IF NOT EXISTS fsm_form_table(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
telegram_id INTEGER,
nickname VARCHAR(255) NOT NULL,
admin_or_sot INTEGER NOT NULL,
UNIQUE(telegram_id))
"""
insert_fsm_table = """
INSERT OR IGNORE INTO fsm_form_table(id,telegram_id,nickname,admin_or_sot) VALUES(?,?,?,?)"""""

select_fsm_table = """
SELECT * FROM fsm_form_table
"""

create_product_table = """
CREATE TABLE IF NOT EXISTS product_table(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(255),
county INTEGER ,
name VARCHAR(255),
description VARCHAR(255),
price INTEGER ,
photo TEXT,
UNIQUE(title))"""

insert_product_table = """
INSERT OR IGNORE INTO product_table(id,title,county,name,description,price,photo) VALUES(?,?,?,?,?,?,?)"""

select_product_table = """
SELECT * FROM product_table
"""