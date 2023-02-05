from flask import Flask
from flask import render_template, request, url_for, redirect
from db_ops import UserDetails

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/media')
def media():
    return('<h2>Media</h2>')

@app.route('/success')
def success_page():
    return render_template('success.html.jinja')

# @app.route('/register', methods = ['POST', 'GET'])
# def register():
#     name = ''
#     email = ''
#     if request.method == 'POST':
#         name = request.form['user_name']
#         email = request.form['user_email']

#         user = UserDetails()
#         user.insert_row(name, email)

#         return redirect(url_for('success_page'))

#     return render_template('register.html.jinja')

@app.route('/inter', methods = ['POST', 'GET'])
def inter():
    name = ''
    email = ''
    if request.method == 'POST':
        name = request.form['user_name']
        email = request.form['user_email']

        user = UserDetails()
        user.insert_row(name, email)

        return redirect(url_for('success_page'))

    return render_template('inter.html')

@app.route('/danza', methods = ['POST', 'GET'])
def danza():
    name = ''
    email = ''
    if request.method == 'POST':
        name = request.form['user_name']
        email = request.form['user_email']

        user = UserDetails()
        user.insert_row(name, email)

        return redirect(url_for('success_page'))

    return render_template('danza.html')

@app.route('/ragam', methods = ['POST', 'GET'])
def ragam():
    name = ''
    email = ''
    if request.method == 'POST':
        name = request.form['user_name']
        email = request.form['user_email']

        user = UserDetails()
        user.insert_row(name, email)

        return redirect(url_for('success_page'))

    return render_template('ragam.html')

@app.route('/coding', methods = ['POST', 'GET'])
def coding():
    name = ''
    email = ''
    if request.method == 'POST':
        name = request.form['user_name']
        email = request.form['user_email']

        user = UserDetails()
        user.insert_row(name, email)

        return redirect(url_for('success_page'))

    return render_template('coding.html')