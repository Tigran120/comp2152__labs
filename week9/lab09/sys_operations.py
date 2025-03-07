import os
import platform
import socket
print("Current Mchine Type")
print(platform.machine())
print("===========================")

print("Current Processor Type")
print(platform.architecture())
print("===========================")


print("Set Socket TimeOut to 50 seconds")
print(socket.setdefaulttimeout(50))
print("Get the current Soclet Timeout")
print(socket.getdefaulttimeout())
print("===========================")

print("Get the current Operating System Type")
print(os.name)
print("===========================")
print("Get the current Operating System Name")
print(platform.system())
print("===========================")

print("Current Process ID")
print(os.getpid())
print("===========================")


file_name="fdpractise.txt"
print(f"\n[Before  Fork] Process {os.getpid()}]")

file_handle=os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process ID] {os.getpid()}] Opened file_handle: {file_handle}")
print("===========================")