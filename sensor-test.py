import time
import Adafruit_DHT
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--type", "-t", help='set sensor type - DHT11 or DHT22 only')
parser.add_argument("--pin", "-p", help="set data pin number")

args = parser.parse_args()
# DHT_SENSOR = Adafruit_DHT.DHT22
# DHT_PIN = 2


if str(args.type) ==  "DHT22":
    DHT_SENSOR = Adafruit_DHT.DHT22
elif str(args.type) == "DHT11":
    DHT_SENSOR = Adafruit_DHT.DHT11
else:
    print ('Type of sensor is not correct. You have to specific type [DHT22|DHT11]. Use --help')
    exit (1)

if int(args.pin) < 48:
    DHT_PIN = int(args.pin)
else:
    print ("Wrong pin number. Use --help")
    exit (1)

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
