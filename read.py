import serial, time
arduino = serial.Serial('/dev/ttyACM0', 9600,  timeout=1)
time.sleep(2)
co=0
while co==0:
    rawString = arduino.readline()
    print(rawString)
arduino.close()