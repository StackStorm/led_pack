import requests

from st2reactor.sensor.base import PollingSensor

__all__ = [
    'TestSensor'
]


class TestSensor(PollingSensor):
    def __init__(self, sensor_service, config=None, poll_interval=None):
        super(TestSensor, self).__init__(sensor_service=sensor_service,
                                           config=config,
                                           poll_interval=poll_interval)
        self._kvp_trigger = 'led_pack.kvp_change'
        self._logger = self._sensor_service.get_logger(__name__)

    def _trigger(self, data):
        self._sensor_service.dispatch(
            trigger=self._kvp_trigger,
            payload=data
        )


    def poll(self):
        self._logger.info('Ran once')
	kvp_value = self._sensor_service.get_value('kvp_test.kvp', local=False)
        if kvp_value:
            self._logger.info('KVP Value: %s' % (kvp_value))
            data = {
                "value": kvp_value
            }
            self._trigger(data)
        else:
            self._logger.info('No KVP Value.')

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
