  #!/usr/bin/python3 -u
from locale import delocalize
from sh import bluetoothctl
import os
import subprocess

import socket
class Hub :
    
    def updater(self):
        try:
            while True:
                
                devices= bluetoothctl("paired-devices").split('\n')


                for device in devices:
                    val = device.split()[1] 
                    devlist = subprocess.check_output(['hcitool','con'])
                    if val not in devlist.split("\n"):
                        print(devices)
                        print(device)
                        print(val)

                        self.devicelist = devices
                        continue
                    print('is there ? : \n')
                    print(devices)
                    print(device)
                    print(val)
                
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

    





    







