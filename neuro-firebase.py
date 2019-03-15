import requests
import json
from NeuroPy import NeuroPy
from time import sleep

neuropy = NeuroPy("COM11")
neuropy.start()

firebase = 'https://eaisociety-1841c.firebaseio.com/brainwaves/aashis/.json'

try:
    while True:
        firebase_value = json.dumps({'attention': neuropy.attention,
         'meditation': neuropy.meditation,
         'rawValue': neuropy.rawValue,
         'delta': neuropy.delta,
         'theta': neuropy.theta,
         'lowAlpha': neuropy.lowAlpha,
         'highAlpha': neuropy.highAlpha,
         'lowBeta': neuropy.lowBeta,
         'highBeta': neuropy.highBeta,
         'lowGamma': neuropy.lowGamma,
         'midGamma': neuropy.midGamma})
        r = requests.put(url = firebase, data = firebase_value)
        sleep(5)
        print(r.status_code)

finally:
    neuropy.stop()
