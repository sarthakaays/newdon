from flask import Flask
import pyodbc 

server = 'sarthaksqlserver.database.windows.net' 
database = 'sarthakdb'
username = 'sarthak' 
password = 'Pathaan&5678'
driver = '{ODBC Driver 18 for SQL Server}'


app = Flask(__name__)

@app.route("/")
def hello():
    cnxn = pyodbc.connect('DRIVER=' + driver + 
                      ';SERVER=' + server + 
                      ';DATABASE=' + database + 
                      ';UID=' + username + 
                      ';PWD=' + password)

    cursor = cnxn.cursor()
    return 'Connection established'
