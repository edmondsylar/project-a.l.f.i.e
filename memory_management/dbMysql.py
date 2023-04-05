# this is going to be my database class.
# we are defining a class for all the CRUD operations and other database related operations.
# we are using pymysql library for this.

# we are going to check the file (../initialize.yaml) for the last system run date and time 
# and log the current date and time right after the system run.

# import all the required libraries
import pymysql.cursors
import yaml
import os
from pathlib import Path
from datetime import datetime

# get initialize.yaml file
init_file = "../initialize.yaml" 

# db class
#class takes connecting user and password as parameters
class dbMysql:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.conn = pymysql.connect(host='localhost',
                             user=self.user,
                             password=self.password,
                             db='alfie',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

        # test connection
        try:
            self.conn.ping(reconnect=True)
        except:
            print("Error: Connection to database failed", flush=True)
        
        # get last system run date and time
        with open(init_file) as file:
            init_params = yaml.load(file, Loader=yaml.FullLoader)
        self.last_run = init_params.get("last_run", "")
        
        # if the last system run == 00:00:00:00, then it is the first time the system is running.
        # call the first_run() function.

        # log current date and time
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        init_params["last_run"] = current_time
        with open(init_file, "w") as file:
            yaml.dump(init_params, file)
            
        
