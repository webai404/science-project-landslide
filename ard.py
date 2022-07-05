import serial
import time
from threading import Thread

ser = serial.Serial("/dev/ttyUSB0", 115200)


def check():
	try:
		data = last_recv
	except:
		print("err")
		return 0
	data = data.replace(b'\r', b'')
	data = data.replace(b'\n', b'')

	data = data.split(b" ")
	#print(data)
	if data != None:
		if int(data[0]) == 0:
			return 1
		elif int(data[1]) < 70:
			return 2
	
	return 0


def recv(ser):
	global last_recv
	buffer_string = b''
	while True:
		buffer_string += ser.read(ser.inWaiting())
		if b'\n' in buffer_string:
			lines = buffer_string.split(b'\n')
			last_recv = lines[-2]
			buffer_string = lines[-1]

Thread(target = recv, args=(ser, )).start()

if __name__ == "__main__":
	while True:
		print(check())		
		time.sleep(5)




















