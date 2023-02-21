from datab_con import *


class Switch(database):
    def __init__(self, user, password, host, name_of_database, port, location, actual_state, gpio_port):
        super().__init__(user, password, host, name_of_database, port)
        self.location = location
        self.actual_state = actual_state
        self.gpio_port = gpio_port

    def get_actual_state(self):
        sql = "SELECT * FROM akalarka.switches WHERE location={name_switch}".format(name_switch=self.location)
        online_state_switch = self.select_from_database(sql)
        self.actual_state = int(online_state_switch[0][2])
        print(self.actual_state)

    def update_database_state(self):
        sql = "UPDATE `Bakalarka`.`switches` SET state = {state} WHERE name_switch={switch_name}".format(state=self.actual_state,
                                                                                        switch_name=self.location)
        try:
            self.insert_to_database(sql)
            return 1
        except:
            return 0