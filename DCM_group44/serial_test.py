import serial
import serial.tools.list_ports as listports
import struct

def main():
    
    devicelist=listports.comports()
    print(len(devicelist))
    
    for Device in devicelist:
        print("---------------")
        print("device: " + Device.device)
        print("name: " + Device.name)
        print("hwid: " + Device.hwid)
        print("vid: " + Device.vid)
        print("pid: " + Device.pid)
        print("serial_number: " + Device.serial_number)
        print("location: " + Device.location)
        print("manufacturer: " + Device.manufacturer)
        print("product: " + Device.product)

    return

if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()