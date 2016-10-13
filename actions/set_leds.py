import requests

from st2actions.runners.pythonrunner import Action

__all__ = [
    'SetLEDs'
]


class SetLEDs(Action):
    def run(self, red, green, blue):
        led_state = {
            "red": red,
            "green": green,
            "blue": blue
        }
        requests.post("http://10.0.0.246:8080/leds/", json=led_state)
