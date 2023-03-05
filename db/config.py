import psycopg2 #importing postgre

#setting a config object to our postgresql
config = {
    "database": "guilds_info",
    "user_name": "postgres",
    "password": "xxx",
    "host": "localhost",
    "port": "5432"
}

#connection
connection = psycopg2.connect(database = config["database"],
                              user = config["user_name"],
                               password = config["password"],
                                host = config["host"],
                                 port =config["port"] )
connection.autocommit = True #We can make it autocommit by this code. 

cursor = connection.cursor() #getting our cursor function to execute our commands



