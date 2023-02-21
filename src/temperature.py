from datab_con import *

import board
import adafruit_dht

dhtDevice_obyvak = adafruit_dht.DHT22(board.D20, use_pulseio=False)
dhtDevice_loznice = adafruit_dht.DHT22(board.D21, use_pulseio=False)


class DhtSensor(database):

    def __init__(self, user, password, host, name_of_database, port, sensorID, temperature):
        super().__init__(user, password, host, name_of_database, port)
        self.sensorID = sensorID
        self.temperature = temperature

    def mess_temperature(self):
        temp = 0
        divide = 0
        for i in range(10):
            if self.sensorID == "Obyvak_DHT":
                try:
                    temp += round(dhtDevice_obyvak.temperature, 3)
                    divide += 1
                except:
                    temp = 0
                    divide = 1

            if self.sensorID == "Loznice_DHT":
                try:
                    temp += round(dhtDevice_loznice.temperature, 3)
                    divide += 1
                except:
                    temp = 0
                    divide = 1
        if divide != 0:
            self.temperature = round(temp / divide, 3)
        else:
            self.temperature = round(temp, 3)

    def add_temp_database(self):
        sql = "INSERT INTO `Bakalarka`.`temp_in` ( `sensor_id`, `temp`) VALUES ('{}',{})".format(self.sensorID,
                                                                                                 self.temperature)
        try:
            self.insert_to_database(sql)
            return 1
        except:
            return 0