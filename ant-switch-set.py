import serial
import sys


def switch_control(port, new_ant, debuglog=True):
    ser = serial.Serial(port, baudrate=19200, bytesize=8, stopbits=1, xonxoff=False, rtscts=False, dsrdtr=False,
                        timeout=1)

    if new_ant == 1:
        hex_befehl = [0x01, 0x02, 0x57, 0x31, 0x0D]
    elif new_ant == 2:
        hex_befehl = [0x01, 0x02, 0x57, 0x32, 0x0D]
    elif new_ant == 3:
        hex_befehl = [0x01, 0x02, 0x57, 0x33, 0x0D]
    elif new_ant == 4:
        hex_befehl = [0x01, 0x02, 0x57, 0x34, 0x0D]
    else:
        raise ValueError("Invalid antenna number. Must be 1, 2, 3 or 4.")

    ser.write(bytearray(hex_befehl))

    response = ser.readline()
    response = response.decode('utf-8').strip()

    if debuglog:
        print("Ant-Switch Response: '" + response + "'")

    ser.close()

    return response


if __name__ == '__main__':
    assert len(sys.argv) == 2, "Usage: python ant-switch-set.py <antenna_number>"
    ant = int(sys.argv[1])

    switch_control('/dev/ttyUSB1', ant)
