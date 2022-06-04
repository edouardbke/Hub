  #!/usr/bin/python3 -u
from locale import delocalize
from sh import bluetoothctl
import os
import subprocess
import re

import socket
class Hub :
    
    def updater(self):
        try:
            while True:
                
                devices= bluetoothctl("paired-devices").split("\n")
                devices = [device.split() for device in  devices]
                toberemoved = []
                for dev in devices:
                    if len(dev) > 1:
                        val = dev[1]
                        toberemoved.append(val)
                
                devices = toberemoved.copy()
                out = subprocess.check_output(["hcitool", "con"]).decode("utf-8")
                out = out.split('\n')
                mac_addr_re = re.compile("^.*([0-9,:,A-F]{17}).*$")

                for line in out:
                    mac_addr = mac_addr_re.match(line)
                    if mac_addr != None:
                        if len(line.split()) > 2:
                            addr = line.split()[2]
                            val = addr in toberemoved
                            if val in toberemoved:
                                toberemoved.remove(addr)
                       
                    
                    print(devices)
                    print(toberemoved)
                    # self.devicelist = devices
                    continue
                    
                
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

    





    







