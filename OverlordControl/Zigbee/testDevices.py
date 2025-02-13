import paho.mqtt.client as mqtt
import json

BROKER = "localhost"
TOPIC = "zigbee2mqtt/bridge/devices"


# Функция обработки полученного сообщения
def on_message(client, userdata, message):
    devices = json.loads(message.payload.decode("utf-8"))
    for device in devices:
        # print(
        #     f"Устройство - {device['friendly_name']}\n"
        #     f"(тип: {device['type']}, "
        #     f"IEEE: {device['ieee_address']}, "
        #     f"адрес в сети: {device['network_address']}"
        #     f"state: {device['state']})"
        # )
        print(device, "\n\n")


# Подключение к MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.connect(BROKER, 1883, 60)

# Подписка на получение списка устройств
client.subscribe(TOPIC)

# Запуск прослушивания
client.loop_forever()
