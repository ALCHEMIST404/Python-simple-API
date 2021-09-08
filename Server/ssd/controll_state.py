import time

ind_change = 0 # Camera status indicator. 1 - Camera does not work. 0 - Camera works
time.sleep(0) # Waiting for the system to boot completely before starting work

while( ind_change == 0):
	f = open("/home/test/Desktop/Germany/Python-simple-API-main/Server/Server_1/ssd/state.txt", 'r')
	str_state = f.read()

	time.sleep(2)

	f1 = open("/home/test/Desktop/Germany/Python-simple-API-main/Server/Server_1/ssd/state.txt", 'r')
	str_state1 = f1.read()

	if str_state == str_state1:
		print("Camera does not work. Stopping the system")
		
		f = open("system_state_status.txt", 'w')
		f.write("101 - Camera does not work. Stopping the system")
		f.close()

		ind_change == 1
		#break
	else:
		f = open("system_state_status.txt", 'w')
		f.write("100 - Camera works")
		f.close()

		print("Camera works")

		ind_change == 0


