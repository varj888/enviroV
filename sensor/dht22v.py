import board
import time
import datetime
import adafruit_dht

### Read the sensor 
def read_sensor(input_time, datetime_current, dht_sensor):
    humidity = dht_sensor.humidity
    temp_c = dht_sensor.temperature

    if humidity is not None and temp_c is not None:
        # C to F conversion
        temp_f = (temp_c * 9/5) + 32

        # Test print
        print("Time: {0} Temperature={1:0.1f} C ({2:0.1f} F) Humidity={3:0.1f}%".format(datetime_current.strftime('%d %b %Y %H:%M:%S'), temp_c, temp_f, humidity))

        sensor_list = [time.strftime('%H:%M:%S', input_time), temp_c, temp_f, humidity]
        return(sensor_list)

    else:
        print("Failed to retrieve data from temp/humidity sensor")

def main():
    dht_sensor = adafruit_dht.DHT22(board.D4)
    start_time = time.time() # Initial time for fancy sleep

    while True:
        # Gives everything the same time to fix a bug that came from calling 
        # time() a bunch of times
        read_time = time.localtime()
        datetime_current = datetime.datetime.now()
        
        read_sensor(dht_sensor, read_time, datetime_current)

        time.sleep(120.0 - ((time.time() - start_time) % 60.0))


if __name__ == "__main__":
    main()
