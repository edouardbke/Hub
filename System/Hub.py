  #!/usr/bin/python3 -u
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
                    if val not in subprocess.run(['hcitool',' con'], stdout=subprocess.PIPE):
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

    





    







