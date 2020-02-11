import os
# import env
from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key=os.getenv('SECRET_KEY')


""" list to saved the list of dictionaries """
messages = []


def add_message(username, message):
    """ function to add message to the list of messages """
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"time":now, 
    "username":username, 
    "message":message}
    messages.append(messages_dict)
    return messages


@app.route('/', methods=["GET", "POST"])
def index():
    """ Index page where the user enters his/her
    name to start using the chat app """
    if request.method == "POST":
        session['username'] = request.form['username']
    
    if 'username' in session:
        return redirect(url_for('user', username=session['username']))

    return render_template('index.html')


@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    """ view to display the user and the chat messages"""
    if request.method == "POST":
        username = session['username']
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for('user', username=username))

    return render_template('chat.html', username=username, messages=messages)


@app.route('/clear', methods=["GET", "POST"])
def clear():
    """ funtion to clear the chat messages """
    messages.clear()
    return redirect(url_for('user', username=session['username']))


if __name__ == "__main__":
    app.run(host=os.getenv('IP'), port=(int(os.getenv('PORT'))), debug=False)