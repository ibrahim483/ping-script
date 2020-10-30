import os
import time

n = 5
p= 1


with open ("TEST_1") as file:
	dump = file.read()
	dump = dump.splitlines()
	
while n > 0:
	print("*"*60 + " loop Nmper ",p , "*"*60 + " " )
	print(p)
	n=n-1
	p =p+1
	print(p)
	for ip in dump:
		response = os.popen(f"ping -c 4 {ip}").read()
#		print (response)
		if "4 received" in response:
			print (f"UP {ip} ping successful")
		else:
			print (f"DOWN {ip} ping unsuccessful")



#		os.system("cls")

#		print ("pinging now", ip)

#		print("-"*60)

#		os.system("ping -c 5 {}".format(ip))

#		print("-"*60)

##		time.sleep(5)	
		
