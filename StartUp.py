



import sys
from InitDir import InitDir
from utils import mycolors
from System.Hub import Hub

def main():
    try:
        InitDir.init()
        
        hub = Hub()
        hub.init()

    
    except Exception as error:
        Functions.errorprint(error)
    sys.stdout.write(mycolors.RESET)


class Functions:
    def errorprint(errmsg):
        if errmsg != None:
            sys.stdout.write(mycolors.RED)
            print(errmsg)
        else:
            print('No error provided')
        sys.stdout.write(mycolors.RESET) 


if __name__ == "__main__":
    main()
