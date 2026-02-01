import json
import time
import psutil
import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPIC = "iot/monitor/cpu"

client = mqtt.Client()
client.connect(BROKER, 1883)

print("=== AGENT MQTT AKTIF ===")

while True:
    data = {
        "device": "Agent-01",
        "cpu_usage": psutil.cpu_percent(),
        "timestamp": time.strftime("%H:%M:%S")
    }

    client.publish(TOPIC, json.dumps(data))
    print("Publish:", data)
    time.sleep(2)
