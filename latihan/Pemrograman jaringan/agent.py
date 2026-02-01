import socket
import json
import time
import psutil   # pip install psutil

# ================= KONFIGURASI =================
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

# ================= SOCKET UDP =================
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("=== AGENT MONITORING AKTIF ===")

while True:
    cpu_usage = psutil.cpu_percent(interval=1)

    data = {
        "device": "Agent-01",
        "cpu_usage": cpu_usage,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    message = json.dumps(data).encode()
    sock.sendto(message, (SERVER_IP, SERVER_PORT))

    print("Data terkirim:", data)
    time.sleep(2)
