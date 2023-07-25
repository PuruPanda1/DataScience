from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/getvideo/<path:video_link>")
def getVideo(video_link):
    video ={
        "videoLink": video_link,
        "videoTile":"Hey i am a title",
        "videoDesc":"Hey I am a description"
    }
    
    extra = request.args.get("v")
    channel = request.args.get("ab_channel")
    if extra:
        video["extra"] = extra
        video["videoLink"] = video["videoLink"]+"?v="+extra+"&ab_channel="+channel
        print(extra)
    return jsonify(video), 200


if __name__ == "__main__":
    app.run(debug=True)
