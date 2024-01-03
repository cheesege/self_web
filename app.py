from flask import Flask
from flask import render_template
from flask import request
from pytube import YouTube as YT
app = Flask(__name__)
#是固定用法，以便讓 Flask 知道在哪裡尋找資源。

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tool')
def tool():
    return render_template('tool.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        text_input = request.form['text_input']
        ytb = YT(text_input)
        videos = ytb.streams.filter(only_audio=True).first()
        url = videos.url
        fn = videos.title
        pic = ytb.thumbnail_url
        print(url)
        return render_template('download.html',link = url , name = fn , png = pic)

if __name__ == '__main__':
    app.run(debug=True)