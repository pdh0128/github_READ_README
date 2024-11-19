from flask import Flask, render_template, request, jsonify
from Read import read
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")
@app.route("/api/read", methods=["GET"])
def reading():
    name = request.args.get('github_id')

    if not name:
        return jsonify({"error": "Missing 'name' parameter"}), 400

    res = read(name)
    data = {"information" : res.to_dict()}
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1000 , debug=True)