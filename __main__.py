# main 26.04.2022
from mongo import Mongo
from mqtt import MQTT
# from signal import pause
# signal geht nur mit Linux

mongo = Mongo()
mqtt = MQTT(mongo)

mongo.connect()

while True:
    mqtt.run()
    s = input('Service started: ')
    if s == 'Ende':
		    break
# try:
#    pause()
# except KeyboardInterrupt:
#   pass
mqtt.stop()
mongo.disconnect()