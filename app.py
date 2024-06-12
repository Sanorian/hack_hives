from flask import Flask, request, send_from_directory
import psycopg2
import os
import waitress

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
    with psycopg2.connect(dbname='videos', user='videos_user', password='videos_password', host='db') as conn:
      cursor = conn.cursor()
      # алгоритм поиска
      query = ""
      cursor.execute(query)
      response = {"videos": cursor.fetchall()}
  except Exception:
    print(str(sys.exc_info()[1]))
    response = {"error": str(sys.exc_info()[1])}
  return json.dumps(response)

@app.route("/upload", methods=['POST'])
def upload_video():
  try:
    response = Video.upload(FlaskAdapter(request),"/videos/")
    # логика для обработки видео
  except Exception:
    response = {"error": str(sys.exc_info()[1])}
  return json.dumps(response)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
