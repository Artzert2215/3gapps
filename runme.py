#!/bin/env python

import sys
import os
import time

os.chdir(sys.path[0]) #run in folder containing script

if len(sys.argv) < 2:
    print("You must provide a path to your system image.")
    print("Usage: sudo python runme.py /path/to/system_image.img")
    exit()

if not os.path.isfile(sys.argv[1]):
    print("Invalid argument.")
    exit()

#build dict with all blacklisted apps
if not os.path.isfile("./blacklist.txt"):
    print("Missing blacklist text file.")
    exit()

blacklist = dict()
tempFile = open('./blacklist.txt','r')
lines = tempFile.readlines()

for line in lines:
    line = line.strip()
    if line[0] != "#":
        blacklist[line.split()[0]] = True

tempFile.close()

#print(blacklist)


os.system(f'sudo bash ./mountImage.sh {sys.argv[1]}')


for appfolder in ["d/system/product/priv-app", "d/system/product/app", "d/system/priv-app"]:
    #check if apps folder exists

    if not os.path.isdir(appfolder):
        print(f"cant find {appfolder}")

    privapps = [name for name in os.listdir(appfolder)]

    for privapp in privapps:
        if privapp in blacklist:
            os.system(f'sudo rm -rf {appfolder}/{privapp}/')
            print(f"=-= removed app: {privapp}")
        #else:
            #print(f"=+= kept app: {privapp}")

print("you must now manually run: sudo bash ./unmountImage.sh")
print("then you're ready to flash slimmer.img to your device")