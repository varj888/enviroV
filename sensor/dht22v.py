import board
import time
import Adafruit_DHT

### Read the sensor 
def read_sensor(dht_sensor, dht_pin, input_time):
    humidity, temp_c = Adafruit_DHT.read_retry(dht_sensor, dht_pin)

    if humidity is not None and temp_c is not None:
        # C to F conversion
        temp_f = (temp_c * 9/5) + 32

        # Test print
        print("Temp={0:0.1f} C ({1:0.1f} F) Humidity={2:0.1f}%".format(temp_c, temp_f, humidity))

        sensor_list = [time.strftime('%H:%M:%S', input_time), temp_c, temp_f, humidity]
        return(sensor_list)

    else:
        print("Failed to retrieve data from humidity sensor")

def main():
    dht_sensor = Adafruit_DHT.DHT22
    start_time = time.time() # Initial time for fancy sleep

    while True:
        # Gives everything the same time to fix a bug that came from calling 
        # time() a bunch of times
        read_time = time.localtime()
        
        read_sensor(dht_sensor, board.D17, read_time)

        time.sleep(120.0 - ((time.time() - start_time) % 60.0))


if __name__ == "__main__":
    main()
