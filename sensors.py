class Sensor:
    def __init__(self, uuid, location):
        self.uuid = uuid
        self.location = location
        self.meter_list = list()

class DHTSensor(Sensor):
    def __init__(self, uuid, location, dht_sensor, pin):
        super().__init__(self, uuid, location, meter_list)
        self.dht_sensor = dht_sensor
        self.pin = pin
    
    def collect_temp():
        pass

