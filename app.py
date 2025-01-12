from flask import Flask, request, jsonify
from script import (
    download_video,
    video_details,
    video_resolution,
    download_audio,
    download_subtitles,
    download_playlist,
    search_video,
    download_channel
)

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to YouTube Downloader"

@app.route('/download_video', methods=['GET'])
def download_video_endpoint():
    url = request.args.get('url')
    try:
        video_path = download_video(url)
        return jsonify({'status': 'success', 'video_path': video_path})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})

@app.route('/video_details', methods=['GET'])
def video_details_endpoint():
    url = request.args.get('url')
    try:
        details = video_details(url)
        return jsonify({'status': 'success', 'details': details})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})

@app.route('/video_resolution', methods=['GET'])
def video_resolution_endpoint():
    url = request.args.get('url')
    resolution = request.args.get('resolution')
    try:
        video_url = video_resolution(url, resolution)
        return jsonify({'status': 'success', 'video_url': video_url})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})

@app.route('/download_audio', methods=['GET'])
def download_audio_endpoint():
    url = request.args.get('url')
    mp3 = request.args.get('mp3', 'true').lower() == 'true'
    try:
        audio_path = download_audio(url, mp3=mp3)
        return jsonify({'status': 'success', 'audio_path': audio_path})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})

@app.route('/download_subtitles', methods=['GET'])
def download_subtitles_endpoint():
    url = request.args.get('url')
    language_code = request.args.get('language_code', 'en')
    filename = request.args.get('filename', 'captions.txt')
    try:
        subtitle_path = download_subtitles(url, language_code, filename)
        return jsonify({'status': 'success', 'subtitle_path': subtitle_path})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})

@app.route('/download_playlist', methods=['GET'])
def download_playlist_endpoint():
    url = request.args.get('url')
    try:
        playlist_downloads = download_playlist(url)
        return jsonify({'status': 'success', 'videos': playlist_downloads})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})

@app.route('/search_video', methods=['GET'])
def search_video_endpoint():
    query = request.args.get('query')
    try:
        search_results = search_video(query)
        return jsonify({'status': 'success', 'search_results': search_results})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})

@app.route('/download_channel', methods=['GET'])
def download_channel_endpoint():
    url = request.args.get('url')
    try:
        channel_name, results = download_channel(url)
        return jsonify({'status': 'success', 'channel_name': channel_name, 'results': results})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
