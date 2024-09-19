from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector


app = Flask(__name__)


def employee_data():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'employees'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT Employee_Name, Title FROM employee_data')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


@app.route('/')
def index():        
    return render_template('home.html')
        
        

@app.route('/employee_data')
def view_employees():
    employees = employee_data()
    return render_template('employee_data.html', employees=employees)

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        
        name = request.form['name']
        title = request.form['title']
        
        
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',
            'port': '3306',
            'database': 'employees'
        }
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "INSERT INTO employee_data (Employee_Name, Title) VALUES (%s, %s)"
        values = (name, title)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()        
        
    
    return render_template('add_employee.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
