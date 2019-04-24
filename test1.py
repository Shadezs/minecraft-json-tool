import json

def main():
	f=open("test1.txt","w+")
	for i in range(20):
		f.write("this is just a test for line %d\r\n" +(i+1))
	f.close()