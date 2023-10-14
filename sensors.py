import Adafruit_GPIO.SPI as SPI
import MAX6675.MAX6675 as MAX6675



class TempSensor():

    def __init__(self):

        # Raspberry Pi software SPI configuration.
        CLK = 25 #SCK
        CS  = 24 
        DO  = 18 #SO 
        self.sensor = MAX6675.MAX6675(CLK, CS, DO)

    
    def read_temp(self):

        return self.sensor.readTempC()