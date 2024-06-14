from flask import Flask, request, send_from_directory
import os
import waitress
from searching import Searcher

app = Flask(
  __name__,
  static_folder='videos'
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
publicDirectory = os.path.join(BASE_DIR, "videos")
if not os.path.exists(publicDirectory):
    os.makedirs(publicDirectory)

@app.route("/search")
def search():
  try:
    # q = "футбольная команда Мадрида"
    question = request.args.get("q")
    s = Searcher()
    s.execute_search_query(s.create_query(question))
    response = {"videos": cursor.fetchall()}
  except Exception as e:
    print(e)
    response = {"error": str(e)}
  return json.dumps(response)

@app.route("/upload", methods=['POST'])
def upload_video():
  try:
    response = Video.upload(FlaskAdapter(request),"/videos/")
    # логика для обработки видео
  except Exception as e:
    print(e)
    response = {"error": str(e)}
  return json.dumps(response)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
