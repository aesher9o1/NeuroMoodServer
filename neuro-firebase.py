import requests
import json
from NeuroPy import NeuroPy
from time import sleep

neuropy = NeuroPy("COM5")
neuropy.connect()

firebase = 'https://eaisociety-1841c.firebaseio.com/brainwaves/aashis/.json'

try:
    while True:
        print(neuropy.raw_value)
        firebase_value = json.dumps({'attention': neuropy.attention, 'meditation': neuropy.meditation,'rawvalue':neuropy.raw_value})
        r = requests.put(url = firebase, data = firebase_value)
        sleep(5)

finally:
    neuropy.disconnect()