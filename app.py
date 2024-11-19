from flask import Flask, render_template, request, jsonify
from Read import read_home, read
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route("/repo")
def submain():
    return render_template("repo.html")

@app.route("/api/read_developer", methods=["GET"])
def reading():
    name = request.args.get('github_id')

    if not name:
        return jsonify({"error": "Missing 'name' parameter"}), 400

    res = read_home(name)
    return jsonify({"information" : res.to_dict()}), 200

@app.route("/api/read_repo", methods=["GET"])
def read_repo():
    name = request.args.get('github_id')
    if not name:
        return jsonify({"error": "Missing 'name' parameter"}), 400

    res = read(name)
    data = []
    for item in res:
        data.append({key: value.to_dict() if hasattr(value, 'to_dict') else value for key, value in item.items()})
    return jsonify({"information" : data}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1000 , debug=True)