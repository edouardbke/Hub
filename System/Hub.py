  #!/usr/bin/python3 -u
from sh import bluetoothctl
import socket
class Hub :
    
    def updater(self):
        try:
            print('Listening for connection...')
            client, address = s.accept()
            print(f'Connected to {address}')

            while True:
                devices= bluetoothctl("power","on")
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

    





    







