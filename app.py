from flask import Flask, send_from_directory, send_file
import os

app = Flask(__name__)

# Получаем абсолютный путь к папке, где лежит этот скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return send_file(os.path.join(BASE_DIR, 'main.html'))

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == '__main__':
    print(f"Сервер запущен! Открой: http://localhost:5000")
    print(f"Папка проекта: {BASE_DIR}")
    app.run(host='0.0.0.0', port=5000, debug=True)