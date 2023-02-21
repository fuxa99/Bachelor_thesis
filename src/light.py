from datab_con import *
import RPi.GPIO as GPIO

class Light(database):
    def __init__(self, user, password, host, name_of_database, port, location, actual_state, gpio_port):
        super().__init__(user, password, host, name_of_database, port)
        self.location = location
        self.actual_state = actual_state
        self.gpio_port = gpio_port

    def update_datab_state(self):
        if self.actual_state == 1:
            GPIO.setup(self.gpio_port, GPIO.OUT)
        else:
            GPIO.setup(self.gpio_port, GPIO.IN)

        sql = "UPDATE `Bakalarka`.`lights` SET state = {state} WHERE location={light_name}".format(state=self.actual_state,
                                                                                        light_name=self.location)
        try:
            self.insert_to_database(sql)
            return 1
        except:
            return 0