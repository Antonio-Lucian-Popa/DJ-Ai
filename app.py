import os
import uuid
import shutil
from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
from flask_cors import CORS
from pydub.utils import which
from pydub import AudioSegment
import yt_dlp

AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe   = "C:\\ffmpeg\\bin\\ffprobe.exe"


app = Flask(__name__)
CORS(app)

OUTPUT_FOLDER = "static"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
TEMP_FOLDER = "temp"
os.makedirs(TEMP_FOLDER, exist_ok=True)


def download_youtube_audio(query, num_results=2):
    ffmpeg_path = "C:\\ffmpeg\\bin\\ffmpeg.exe"

    ydl_opts = {
        'ffmpeg_location': ffmpeg_path,  # ✅ corect
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'outtmpl': f'{TEMP_FOLDER}/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    search_query = f"ytsearch{num_results}:{query}"
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download=True)
        return [entry['id'] + ".mp3" for entry in info['entries'][:num_results]]


def mix_tracks(tracks):
    mixed = None
    for i, track_file in enumerate(tracks):
        audio = AudioSegment.from_mp3(os.path.join(TEMP_FOLDER, track_file))
        if mixed is None:
            mixed = audio
        else:
            crossfade = 4000  # 4 seconds
            mixed = mixed.append(audio, crossfade=crossfade)
    return mixed


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        genre = request.form.get("genre", "manele")
        try:
            files = download_youtube_audio(genre, num_results=3)
            mixed = mix_tracks(files)

            filename = f"mix_{uuid.uuid4().hex}.mp3"
            filepath = os.path.join(OUTPUT_FOLDER, filename)
            mixed.export(filepath, format="mp3")

            for f in os.listdir(TEMP_FOLDER):
                os.remove(os.path.join(TEMP_FOLDER, f))

            return redirect(url_for("index", mix=filename))
        except Exception as e:
            return render_template("index.html", error=str(e))

    mix_filename = request.args.get("mix")
    return render_template("index.html", mix=mix_filename)


@app.route("/static/<path:filename>")
def serve_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)
