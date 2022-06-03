  #!/usr/bin/python3 -u
from sh import bluetoothctl
import socket
class Hub :
    
    def updater(self):
        try:
            while True:
                devices= bluetoothctl("paired-devices")
                if devices:
                    print(devices)
                    self.devicelist = devices
                
        except Exception as e:
            print(f'Something went wrong: {e}')
            

    def init(self):
            self.name = socket.gethostname()
            self.devicelist =[]
            self.wifiname = ""
            self.wifissid = ""
            self.wifipassword =  ""
            self.ipaddress = ""
            self.isbusy = False
            self.updater()

    





    







