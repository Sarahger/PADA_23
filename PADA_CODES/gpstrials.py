import serial,time,pynmea2

port = '/dev/ttyAMA0'
baud = 9600

serialPort = serial.Serial(port, baudrate = baud, timeout = 0.5)

lat1 = 19.044356759382666 % 10000 #CRCE
lon1 = 72.82036700137729 % 10000

while True:

    str = ''
    try:
        str = serialPort.readline().decode().strip()
    except Exception as e:
        print(e)
    #print(str)
    
    if str.find('GGA') > 0:
        try:
            msg = pynmea2.parse(str)
            # print(msg.timestamp,'Lat:',(msg.latitude),'Lon:',(msg.latitude),'Alt:',msg.altitude,'Sats:',msg.num_sats)
            latitude = float(msg.latitude)
            longitude = float(msg.longitude)
        except Exception as e:
            print(e)
    time.sleep(0.5)
