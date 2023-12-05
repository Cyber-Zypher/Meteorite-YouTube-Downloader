from flask import Flask, render_template, request, send_file, flash
from pytube import YouTube

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    resolution = request.form['resolution']
    audio_only = 'audio' in request.form

    if 'youtube.com' in url or 'youtu.be' in url:
        yt = YouTube(url)
        if audio_only:
            video = yt.streams.filter(only_audio=True).first()
        else:
            video = yt.streams.filter(res=f'{resolution}p').first()

        file_path = video.download()
        return send_file(file_path, as_attachment=True)
    else: 
        print("Invalid URL")
    return 'Invalid URL'


if __name__ == '__main__':
    app.run(debug=True)
