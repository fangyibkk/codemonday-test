from flask import Flask, Response, jsonify, send_file, render_template
from os.path import isfile

app = Flask(__name__, static_folder='./static')

if isfile('count.txt'):
    print ("Count file exist")
else:
    print ("Count file not exist -> create a new one")
    with open('count.txt', 'w+') as f:
        f.write("1")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/count/<count>')
def update_count(count):
    with open('count.txt', 'w+') as f:
        f.write(count)
    return jsonify(count=count)

@app.route('/api/count')
def get_count():
    count = ''
    with open('count.txt', 'r') as f:
        count = f.read()
    return jsonify(count=count)

if __name__ == '__main__':
    app.run()