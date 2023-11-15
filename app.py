from flask import Flask
from flask import render_template
app = Flask(__name__)
#是固定用法，以便讓 Flask 知道在哪裡尋找資源。

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tool')
def tool():
    return render_template('tool.html')

if __name__ == '__main__':
    app.run(debug=True)