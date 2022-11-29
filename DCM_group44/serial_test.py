import serial
import serial.tools.list_ports as listports
import struct

def main():
    
    devicelist=listports.comports()
    print(len(devicelist))
    
    for Device in devicelist:
        print("---------------")
        print("device: " + str(Device.device))
        print("name: " + str(Device.name))
        print("hwid: " + str(Device.hwid))
        print("vid: " + str(Device.vid))
        print("pid: " + str(Device.pid))
        print("serial_number: " + str(Device.serial_number))
        print("location: " + str(Device.location))
        print("manufacturer: " + str(Device.manufacturer))
        print("product: " + str(Device.product))

    return

if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()