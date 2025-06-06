import serial


def switch_read(port, debuglog=True):
    ser = serial.Serial(port, baudrate=19200, bytesize=8, stopbits=1, xonxoff=False, rtscts=False, dsrdtr=False,
                        timeout=1)

    hex_befehl = [0x01, 0x01, 0x52, 0x0D]

    ser.write(bytearray(hex_befehl))

    response = ser.readline()
    response = response.decode('utf-8').strip()

    if debuglog:
        print("Ant-Switch Response: '" + response + "'")

    ser.close()

    return response


if __name__ == '__main__':
    switch_read('/dev/ttyUSB0')
