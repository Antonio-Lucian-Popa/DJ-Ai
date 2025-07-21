# 🎧 DJ Automat AI (Flask)

Un DJ automat care caută piese de pe YouTube, le descarcă și le mixează automat într-un set continuu, cu interfață web responsive.

## ✅ Funcționalități
- Căutare automată piese YouTube după gen
- Descărcare + conversie audio (`yt-dlp` + `ffmpeg`)
- Mixare automată cu `pydub` și `crossfade`
- Interfață web simplă și frumoasă (Bootstrap 5)

---

## 🧱 Structura proiectului
```
DJ_Ai/
├── app.py                # Aplicația Flask
├── requirements.txt      # Dependențe Python
├── static/               # Conține mixurile generate (.mp3)
├── temp/                 # Fișiere temporare YouTube
└── templates/
    └── index.html        # Interfață web
```

---

## 🚀 Cum rulezi local

### 1. Clonează sau descarcă proiectul

### 2. Creează un mediu virtual (opțional dar recomandat)
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalează dependențele
```bash
pip install -r requirements.txt
```

### 4. Instalează FFmpeg (obligatoriu)
- Descarcă de la: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
- Descarcă `ffmpeg-release-essentials.zip`
- Dezarhivează-l în `C:\ffmpeg`
- Verifică: `C:\ffmpeg\bin\ffmpeg.exe` și `ffprobe.exe` există

### 5. Adaugă calea `C:\ffmpeg\bin` în variabila de mediu `PATH`

### 6. Rulează aplicația
```bash
python app.py
```

Accesează apoi: [http://localhost:5000](http://localhost:5000)

---

## 📝 Exemple de genuri
- `manele`
- `trap romanesc`
- `techno`
- `house 2023`
- `chill lofi`

---

## 🔧 Probleme comune
- ❌ `ffmpeg not found`: setează manual calea în `app.py`
```python
AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = "C:\\ffmpeg\\bin\\ffprobe.exe"
```

- ❌ `yt-dlp` erori: verifică că ai setat corect `ffmpeg_location` în `ydl_opts`

---

## 📦 Dependențe
```
Flask
flask-cors
pydub
yt-dlp
```

---

## 💡 Dezvoltări viitoare
- Selector presetat de genuri
- Mixer live cu tranziții avansate
- Generare cover AI
- Export video pentru YouTube/Instagram

---

## 🧠 Creat cu ❤️ și AI pentru petreceri automate!
