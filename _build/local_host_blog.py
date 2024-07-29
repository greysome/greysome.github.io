import os
from flask import Flask, send_from_directory

app = Flask(__name__)

SITE_DIR = '../_site'

@app.errorhandler(404)
def page_not_found(e):
    return send_from_directory(SITE_DIR, '404.html')

@app.route('/')
def root():
    return send_from_directory(SITE_DIR, 'index.html')

@app.route('/<filename>')
def serve_static(filename):
    return send_from_directory(SITE_DIR, filename)

@app.route('/<path:path>/<filename>')
def serve_static_in_dir(path, filename):
    return send_from_directory(f'{SITE_DIR}/{path}', filename)

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    app.run(port=8000, debug=True)