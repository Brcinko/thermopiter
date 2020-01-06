import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 2

while True:
    try: 
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            print("Datetime={0}; Temp={1:0.1f}*C;  Humidity={2:0.1f}%".format(time.strftime('%d/%m/%Y-%H:%M:%S'), temperature, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")
    except RuntimeError as e:
        print("Error: ", e.args)
    time.sleep(1)
