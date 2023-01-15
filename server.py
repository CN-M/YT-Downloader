from flask import Flask, request, send_file
from pytube import YouTube
from subprocess import call

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download():
    video_url = request.args.get('url')
    if video_url is None:
        return 'Please provide a valid video URL as a query parameter.', 400
    else:
        yt = YouTube(video_url)
        video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
        audio = yt.streams.filter(only_audio=True).first()
        video.download('videos')
        audio.download('audios')
        file_name = video.default_filename.split('.')[0]
        call(['ffmpeg', '-i', 'videos/' + video.default_filename, '-i', 'audios/' + audio.default_filename, '-c', 'copy', file_name + '.mp4'])
        return send_file(file_name + '.mp4', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')