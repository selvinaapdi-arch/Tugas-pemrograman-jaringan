import socket
import json
import threading
from flask import Flask, request, jsonify
from flask_socketio import SocketIO

# ================= FLASK =================
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
DATA_FILE = "data.json"
USER_FILE = "users.json"

# ================= UDP LISTENER =================
def udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print("=== UDP SERVER AKTIF ===")

    while True:
        data, addr = sock.recvfrom(1024)
        decoded = json.loads(data.decode())

        # Simpan ke file
        with open(DATA_FILE, "a") as f:
            f.write(json.dumps(decoded) + "\n")

        # Kirim ke client WebSocket
        socketio.emit("update", decoded)

        print("Data diterima dari", addr, decoded)

# ================= REST API LOGIN =================
@app.route("/login", methods=["POST"])
def login():
    req = request.get_json()
    username = req.get("username")
    password = req.get("password")

    with open(USER_FILE) as f:
        users = json.load(f)

    if username in users and users[username] == password:
        return jsonify({"status": "ok"})
    else:
        return jsonify({"status": "fail"}), 401

# ================= DASHBOARD =================
@app.route("/")
def dashboard():
    return app.send_static_file("dashboard.html")

# ================= MAIN =================
if __name__ == "__main__":
    threading.Thread(target=udp_server, daemon=True).start()

    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        ssl_context=("cert.pem", "key.pem")
    )
