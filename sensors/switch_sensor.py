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
        self._trigger_ref = 'led_pack.switch_change'
        self._logger = self._sensor_service.get_logger(__name__)

    def poll(self):
        switch_request = requests.get('http://10.0.0.245:8080/switches/')
        switch_data = switch_request.json()

        if switch_data['state_change']:
            self._sensor_service.dispatch(trigger=self._trigger_ref)

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
