from flask import Flask, request
import requests
from datetime import datetime


app = Flask(__name__)

@app.route("/proxy", methods=["GET"])
def proxy():
    url = request.args.get("url")
    if not url:
        return {
            "error": "Missing URL",
            "timestamp": datetime.now().isoformat()
        }, 400

    try:
        # Eğer VPN üzerinden çıkmak için ek bir proxy gerekiyorsa bu kısmı düzenle
        response = requests.get(url, timeout=10, verify=False)
        return {
            "status_code": response.status_code,
            "timestamp": datetime.now().isoformat()
        }, 200
    except Exception as e:
        return {
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
