import sys
import os
import tarfile
import time
import subprocess
import subprocess, _thread, threading
import multiprocessing, socket, struct, re, types, fnmatch, platform, telnetlib
sys.path.insert (0, 'C:\Python38\Lib\site-packages\PyVISA-1.5-py3.8.egg')
import visa
from visa import *
   
#======================================================================
def InitPSU(address):
   print("------------------------ PSU INIT ---------------------------------")
   try:
      time.sleep(2)
      psu_handle = instrument(address)
      print("esto")
      if (psu_handle != ""):
         msg = "PSU: %s" % psu_handle.ask("*IDN?")
         print(msg)
         psu_handle.write("OUTP OFF")
         time.sleep (5)
         return psu_handle
      else:
         print("PSU Init fail.")
   except:
      print("PSU init failed.")
      #roska = input(" Power INIT failed. Did you run PyVISA_Install\setup.bat? Close this bat file, try again or use manually.")

#======================================================================
def SetPSUOutput(on_off, handle):
   print("---------------------- PSU OUTPUT ON_OFF ------------------------------")
   try:
      msg = ("OUTP %s")% on_off
      print(msg)
      handle.write(msg)
   except:
      print("PSU error during switch ON.")
      #roska = input(" Power ON failed. Switch 48V 5A ON (N5767). Then press ENTER")      
	  
#======================================================================
def ClosePSU(handle):
   print("---------------------- PSU CLOSE ------------------------------")
   try:
      handle.Close()
   except:
      print("PSU error during PSU closing .")        

#======================================================================
def ivoReset(handle):
   print("------------------------ IVO RESET --------------------------------")
   try:
      msg = ("OUTP OFF")
      print(msg)
      handle.write(msg)
      time.sleep(5)
      msg = ("OUTP ON")
      print(msg)
      handle.write(msg)      
   except:
      print("PSU error during switch ON.")        
      #roska = input(" Power ON failed. Switch 48V OFF AND ON (N5767). Then press ENTER")

#======================================================================
# quit function
def SetPSULimits(volt, curr, psu_handle):
   print("---------------- PSU VOLT AND CURR SET ----------------------------")
   try:
      commandstr = ("VOLT %s")% volt
      psu_handle.write(commandstr)
      print("PSU: set VOLT: %s V" % volt)
      commandstr = ("CURR %s")% curr
      psu_handle.write(commandstr)
      print("PSU: set CURR: %s A" % curr)
   except:
      print("PSU", "Set limits to PSU: Voltage: %s - Current: %s" % (volt, curr))         
#======================================================================
# MAIN SCRIPT
def main():
   print("-------------------------------------------------------------------")
   #roska = input("Continue by pressing ENTER......................")
   
   PsuHandle = InitPSU("TCPIP0::10.0.0.103::INSTR")
   SetPSULimits("48", "21", PsuHandle)
   SetPSUOutput("OFF", PsuHandle)
   
   print(".....Wait 10 seconds...")
   time.sleep(2)
   
   #ivoReset(PsuHandle)
   #SetPSUOutput("OFF", PsuHandle)
   #time.sleep(2)
   #PsuHandle.Close()
   
   exit()

main()
