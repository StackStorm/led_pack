import requests

from st2reactor.sensor.base import PollingSensor

__all__ = [
    'SwitchSensor'
]


class SwitchSensor(PollingSensor):
    def __init__(self, sensor_service, config=None, poll_interval=None):
        super(SwitchSensor, self).__init__(sensor_service=sensor_service,
                                           config=config,
                                           poll_interval=poll_interval)
        self._switch_trigger = 'led_pack.switch_change'
        self._logger = self._sensor_service.get_logger(__name__)
        self._prev_on = False

    def _trigger(self, data):
        self._sensor_service.dispatch(
            trigger=self._switch_trigger,
            payload=data
        )


    def poll(self):
        switch_request = requests.get('http://192.168.33.10:8080/switches/')
        switch_data = switch_request.json()

	if switch_data['is_on'] and switch_data['change']:
            self._trigger(switch_data)

	elif not self._prev_on and switch_data['is_on']:
            switch_data['red'] = 100
            switch_data['green'] = 100
            switch_data['blue'] = 100

            self._trigger(switch_data)

	elif self._prev_on and not switch_data['is_on']:
            switch_data['red'] = 0
            switch_data['green'] = 0
            switch_data['blue'] = 0

            self._trigger(switch_data)

        self._prev_on = switch_data['is_on']

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass

    def setup(self):
        pass

    def cleanup(self):
        pass
