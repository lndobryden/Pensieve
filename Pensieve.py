import serial
ser = serial.Serial('/dev/tty.usbmodem221', 115200)
while True:
    print ser.readline()
