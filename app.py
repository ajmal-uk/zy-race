from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start-game')
def static_files(filename):
    return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)