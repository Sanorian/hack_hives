from flask import Flask, request

import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
publicDirectory = os.path.join(BASE_DIR, "videos")
if not os.path.exists(publicDirectory):
    os.makedirs(publicDirectory)

@app.route("/search")
def search():
    question = request.args.get("q")
    #логика поиска

@app.route("/upload", methods=['POST'])
def upload_video():
  try:
    response = Video.upload(FlaskAdapter(request),"/videos/")
    # логика для обработки видео
  except Exception:
    response = {"error": str(sys.exc_info()[1])}
  return json.dumps(response)
app.run()
