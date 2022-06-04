  #!/usr/bin/python3 -u
import time
import pexpect
from sh import bluetoothctl
import os
import subprocess
import re

import socket
class BluetoothctlError(Exception):
    """This exception is raised, when bluetoothctl fails to start."""
    pass
class Hub :
    
    def updater(self):
        try:
            while True:
                self.removenotconnecteddevices()
                    
                
        except Exception as e:
            print(f'Something went wrong: {e}')
    
    def get_output(self, command,pause = 0):
        self.child = pexpect.spawn("bluetoothctl", echo = False)
        self.child.send(command + "\n")
        time.sleep(pause)
        start_failed = self.child.expect(["bluetooth", pexpect.EOF])
        if start_failed:
            raise BluetoothctlError("Bluetoothctl failed after running " + command)

        return self.child.before.split("\r\n")

    def removenotconnecteddevices(self):
        try:
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
                if mac_addr != None and len(line.split()) > 2:
                    addr = line.split()[2]
                    if addr in toberemoved:
                        toberemoved.remove(addr)
                else :
                    continue
            
            for dev in toberemoved:
                confirm = self.get_output("remove " + dev, 3)
                print(confirm)
    

            print(devices)
            print(toberemoved)
            print('-----------------------------------')
                
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

    





    







