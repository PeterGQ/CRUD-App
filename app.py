# import libraries: Flask and sql
from flask import Flask, render_template, request
import sqlite3

# take in user input
# checks which command was executed by the user(create, search, delete, update)
# Create function
# Search function
# Update function
# Delete function
# add table to html page
app = Flask(__name__)

def table():
    databaseConnect = sqlite3.connect("HW2.db")
    databaseConnect.row_factory = sqlite3.Row
    cursor = databaseConnect.cursor()
    cursor.execute("SELECT * FROM users")
    table = cursor.fetchall()
    return table

@app.route('/',methods=['GET','POST'])
def index():
    table1 = table()
    print(table1)
    return render_template('index.html', table1=table1)

@app.route('/CRUD', methods=['POST'])
def CRUD():
    databaseConnect = sqlite3.connect("HW2.db")
    databaseConnect.row_factory = sqlite3.Row
    cursor = databaseConnect.cursor()
    name = request.form['name']
    id = request.form['ID']
    points = request.form['Points']
    method = request.form['CRUDOP']
    dataSearch = "SELECT name FROM users WHERE Id='"+id+"'"
    cursor.execute(dataSearch)
    findId = cursor.fetchall()

    dataSearch2 = "SELECT name FROM users WHERE Points='" + points + "'"
    cursor.execute(dataSearch2)
    findPoints = cursor.fetchall()

    dataSearch3 = "SELECT name FROM users WHERE Name='"+name+"'"
    cursor.execute(dataSearch3)
    findName = cursor.fetchall()

    if(len(findName) == 100):
        return "Error: not found"
    else:
        if method == "Create":
            if(len(findId) == 0) and len(id) != 0 and len(name) != 0 and len(points) != 0:
                dataCreate = "INSERT INTO users VALUES ('"+name+"','"+id+"','"+points+"')"
                cursor.execute(dataCreate)
                databaseConnect.commit()
        if method == "Delete":
            if len(findId) != 0:
                dataDelete = "DELETE FROM users WHERE Id='"+id+"'"
                cursor.execute(dataDelete)
                databaseConnect.commit()
        if method == "Search":
            dataSearch = "SELECT Name,Id,Points FROM users WHERE Name='" + name + "'"
            cursor.execute(dataSearch)
            dataFind = cursor.fetchall()
            table1=table()
            return render_template('index.html', table1=table1,dataFind=dataFind)
        if method == "Update":
            if len(name) != 0 and len(findId) != 0 and len(points) != 0:
                dataUpdate = "UPDATE users SET Name='"+name+"',Id='"+id+"',Points='"+points+"' WHERE Id='"+id+"'"
                cursor.execute(dataUpdate)
                databaseConnect.commit()
            elif len(name) == 0 and len(findId) != 0 and len(points) != 0:
                dataUpdate = "UPDATE users SET Id='" + id + "',Points='" + points + "' WHERE Id='" + id + "'"
                cursor.execute(dataUpdate)
                databaseConnect.commit()
            elif len(name) != 0 and len(findId) != 0 and len(points) == 0:
                dataUpdate = "UPDATE users SET Name='" + name + "',Id='" + id + "' WHERE Id='" + id + "'"
                cursor.execute(dataUpdate)
                databaseConnect.commit()
        table1 = table()
        return render_template('index.html', table1=table1)
        # if method == "Select":
        #
        # if method == "Delete":
        #
        # if method == "Update":




if __name__ == '__main__':
    app.run(debug=True)