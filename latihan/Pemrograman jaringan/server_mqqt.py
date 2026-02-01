import json
import paho.mqtt.client as mqtt
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

BROKER = "localhost"
TOPIC = "iot/monitor/cpu"

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    socketio.emit("update", data)
    print("MQTT diterima:", data)

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883)
client.subscribe(TOPIC)
client.loop_start()

@app.route("/")
def index():
    return app.send_static_file("dashboard.html")

if __name__ == "__main__":
    socketio.run(app, port=5000)
