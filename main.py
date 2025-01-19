import asyncio
from weakref import proxy
from flask import Flask, request, jsonify
import requests
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
from threading import Thread, Lock
from queue import Queue
import logging
from utils.Proxy import available_proxies,get_random_proxy

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

proxy_lock = Lock()

def build_proxy_dict(proxy):
    return {
        "http": f"http://{proxy['username']}:{proxy['password']}@{proxy['ip']}",
        "https": f"https://{proxy['username']}:{proxy['password']}@{proxy['ip']}"
    }

def process_request(action, url, *args, **kwargs):
    proxy = available_proxies.get()
    proxy_dict = build_proxy_dict(proxy)
    
    try:
        logger.info(f"Processing request for URL: {url} using proxy: {proxy['ip']}")

        kwargs['proxies'] = proxy_dict
        
        if asyncio.iscoroutinefunction(action):
            result = asyncio.run(action(url, *args, **kwargs))
        else:
            result = action(url, *args, **kwargs)

        available_proxies.put(proxy)

        return {"status": "success", "result": result}
    except Exception as e:
        logger.error(f"Error processing request for URL: {url} using proxy: {proxy['ip']} - {e}")
        available_proxies.put(proxy)

        return {"status": "error", "error": str(e)}
    

@app.route("/", methods=['GET'])
def welcome():
    return requests.get(
    "https://ipv4.webshare.io/",
    proxies={
        "http": "http://bchcorqb-rotate:iqvp6jozfsf9@p.webshare.io:80/",
        "https": "http://bchcorqb-rotate:iqvp6jozfsf9@p.webshare.io:80/"
    }
    ).text

@app.route('/download_video', methods=['GET'])
def download_video_endpoint():
    url = request.args.get('url')
    if not url:
        return jsonify({'status': 'error', 'error': 'URL parameter is required'}), 400
    
    result = process_request(download_video, url)
    return jsonify(result)

@app.route('/video_details', methods=['GET'])
def video_details_endpoint():
    url = request.args.get('url')
    if not url:
        return jsonify({'status': 'error', 'error': 'URL parameter is required'}), 400

    result = process_request(video_details, url)
    return jsonify(result)

@app.route('/video_resolution', methods=['GET'])
def video_resolution_endpoint():
    url = request.args.get('url')
    resolution = request.args.get('resolution')
    if not url or not resolution:
        return jsonify({'status': 'error', 'error': 'URL and resolution parameters are required'}), 400
    
    result = process_request(video_resolution, url, resolution)
    return jsonify(result)

@app.route('/download_audio', methods=['GET'])
def download_audio_endpoint():
    url = request.args.get('url')
    mp3 = request.args.get('mp3', 'true').lower() == 'true'
    if not url:
        return jsonify({'status': 'error', 'error': 'URL parameter is required'}), 400

    result = process_request(download_audio, url, mp3=mp3)
    return jsonify(result)

@app.route('/download_subtitles', methods=['GET'])
def download_subtitles_endpoint():
    url = request.args.get('url')
    language_code = request.args.get('language_code', 'en')
    filename = request.args.get('filename', 'captions.txt')
    if not url:
        return jsonify({'status': 'error', 'error': 'URL parameter is required'}), 400

    result = process_request(download_subtitles, url, language_code, filename)
    return jsonify(result)

@app.route('/download_playlist', methods=['GET'])
def download_playlist_endpoint():
    url = request.args.get('url')
    if not url:
        return jsonify({'status': 'error', 'error': 'URL parameter is required'}), 400

    result = process_request(download_playlist, url)
    return jsonify(result)

@app.route('/search_video', methods=['GET'])
def search_video_endpoint():
    query = request.args.get('query')
    if not query:
        return jsonify({'status': 'error', 'error': 'Query parameter is required'}), 400

    result = process_request(search_video, query)
    return jsonify(result)

@app.route('/download_channel', methods=['GET'])
def download_channel_endpoint():
    url = request.args.get('url')
    if not url:
        return jsonify({'status': 'error', 'error': 'URL parameter is required'}), 400

    result = process_request(download_channel, url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
