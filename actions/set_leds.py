import requests

from st2actions.runners.pythonrunner import Action

__all__ = [
    'SetLEDs'
]


class SetLEDs(Action):
    def run(self, change, is_on, red, green, blue):
        if change and is_on:
            led_state = {
                "red": red,
                "green": green,
                "blue": blue
            }
            requests.post("http://192.168.33.52:8080/leds/", json=led_state)

        if not is_on:
            led_state = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            requests.post("http://192.168.33.52:8080/leds/", json=led_state)
