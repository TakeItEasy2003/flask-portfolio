from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = '1234'

# Use DATABASE_URL from environment
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'postgresql://akhilajoy@localhost/portfolio'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

# Contact form model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Skills page
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Contact page - GET and POST
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        new_msg = Message(name=name, email=email, message=message)
        db.session.add(new_msg)
        db.session.commit()
        return redirect('/')
    return render_template('contact.html')

# Admin login
@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '1234':
            session['admin'] = True
            return redirect('/messages')
        else:
            return "Access Denied. Invalid credentials."
    return render_template('admin_login.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')

# Protected messages page
@app.route('/messages')
def messages():
    if not session.get('admin'):
        return redirect('/admin-login')
    all_messages = Message.query.all()
    return render_template('messages.html', messages=all_messages)

# Delete a message
@app.route('/delete/<int:id>')
def delete_message(id):
    if not session.get('admin'):
        return redirect('/admin-login')
    msg_to_delete = Message.query.get_or_404(id)
    db.session.delete(msg_to_delete)
    db.session.commit()
    return redirect('/messages')

if __name__ == '__main__':
    app.run(debug=True)
