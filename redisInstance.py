import redis
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

redis_instance =  redis.Redis(host=config['REDIS_HOST'], port=config['REDIS_PORT'], db=config['REDIS_DB'])