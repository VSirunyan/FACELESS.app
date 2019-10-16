import os
import json
import socket
from viewinfo.models import WifiDatabase


class Constants:
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    TIME = "time"
    WIFI = "wifi"
    TYPE = "type"
    DIAP = "diap"
    CHANNELS = "max_channels_count"
    MAC = "mac_address"
    IP = "ip_address"
    POWER = "power"


class WifiParser:
    def __init__(self, data):
        self.wifis = []

        for wifi in data[Constants.WIFI]:
            cur_wifi_data = {
                Constants.LATITUDE: data[Constants.LATITUDE],
                Constants.LONGITUDE: data[Constants.LONGITUDE],
                Constants.TIME: data[Constants.TIME],
                Constants.TYPE: wifi[Constants.TYPE],
                Constants.DIAP: wifi[Constants.DIAP],
                Constants.CHANNELS: wifi[Constants.CHANNELS],
                Constants.MAC: wifi[Constants.MAC],
                Constants.IP: wifi[Constants.IP],
                Constants.POWER: wifi[Constants.POWER]
            }
            self.wifis.append(Wifi(cur_wifi_data))


class Wifi:
    def __init__(self, data):
        self.latitude = data[Constants.LATITUDE]
        self.longitude = data[Constants.LONGITUDE]
        self.time = data[Constants.TIME]
        self.type = data[Constants.TYPE]
        self.diap = data[Constants.DIAP]
        self.max_channels = data[Constants.CHANNELS]
        self.mac_address = data[Constants.MAC]
        self.ip_address = data[Constants.IP]
        self.power = data[Constants.POWER]

    def add_new_wifi(self):
        wifis = WifiDatabase.objects.filter(latitude=self.latitude,
                                            longitude=self.longitude,
                                            time = self.time,
                                            type = self.type,
                                            diap = self.diap,
                                            channels = self.max_channels,
                                            mac = self.mac_address,
                                            ip = self.ip_address,
                                            power = self.power)
        if wifis.count() != 0:
            return

        wifi = WifiDatabase(latitude=self.latitude,
                            longitude=self.longitude,
                            time=self.time,
                            type=self.type,
                            diap=self.diap,
                            channels=self.max_channels,
                            mac=self.mac_address,
                            ip=self.ip_address,
                            power=self.power)
        wifi.save()


def parse_data(data):
    wifi_parser = WifiParser(data)
    return wifi_parser.wifis


def start_server():
    script_dir = os.path.dirname(__file__)
    db_file_path = os.path.join(script_dir, "database.json")

    try:
        with open(db_file_path, "r") as db_content:
            database = json.load(db_content)
    except:
        database = []

    host = '127.0.0.1'
    port = 55555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    conn, addr = s.accept()
    print('Connected by', addr)

    while 1:
        data_package = conn.recv(1024)
        data = json.loads(data_package, encoding='ascii')

        wifis = parse_data(data)
        for wifi in wifis:
            wifi.add_new_wifi()

        with open(db_file_path, "w") as db_file:
            json.dump(database, db_file, indent=1)

        conn.sendall("OK")

    conn.close()
