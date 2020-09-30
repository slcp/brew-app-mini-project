from src.data_store.mysql_db import MySQLDB

db = MySQLDB("db", "brew_app", 3306, "root", "password")

db.load_people()
