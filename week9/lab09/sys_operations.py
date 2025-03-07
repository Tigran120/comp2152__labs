import os
import platform
import socket
import sys

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

file_object_TextIO=os.fdopen(file_handle, "w+")

file_object_TextIO.write("Some string to write to the file")
file_object_TextIO.flush()

print(f"\n[Before Process {os.getpid()}] Forking now")
pid=os.fork()

if pid == 0:
    #Child Process
    print(f"\n[Child PID: {pid} has Parent Process ID: {os.getpid()}]")
    os.lseek(file_handle, 0,0)
    print(f"[Child Process: {os.getpid()} File Content: {os.read(file_handle, 100).decode()}]")

    os.close(file_handle)
    sys.exit(0)
else:
    #Parent PID
    print(f"\n[Parent Process ID: {os.getpid}], Child PID: {pid}")
    print("Wait for the Child to complete the modification")
    os.wait()
    print("Child Process Finished the modification")
    file_object_TextIO.close()
print(f"\n[Process {os.getpid}] File Closed. Exiting now..")
sys.exit(0)