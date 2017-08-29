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
            return requests.post(self.config['led_controller'], json=led_state).json()

        if not is_on:
            led_state = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            return requests.post(self.config['led_controller'], json=led_state).json()
