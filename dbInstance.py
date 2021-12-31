import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

db_instance =  mysql.connector.connect(host=config['MYSQL_HOST'], user=config['MYSQL_USER'], password=config['MYSQL_PASSWORD'], database=config['MYSQL_DB'])