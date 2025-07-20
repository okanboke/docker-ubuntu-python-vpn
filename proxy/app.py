from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/proxy", methods=["GET"])
def proxy():
    url = request.args.get("url")
    if not url:
        return "Missing URL", 400

    try:
        # Eğer VPN üzerinden çıkmak için ek bir proxy gerekiyorsa bu kısmı düzenle
        response = requests.get(url, timeout=10)
        return {"status_code": response.status_code}, 200
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
