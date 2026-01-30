import os.path
import time
import argparse
from datetime import datetime
import sys
from os import listdir
from os.path import isfile, join

dirs = [
  "1071-Number_Spiral",
  "1082-Sum_of_Divisors",
  "1084-Apartments",
  "1091-Concert_Tickets",
  "1131-Tree_Diameter",
  "1132-Tree_Distances_I",
  "1140-Projects",
  "1158-Bookshop",
  "1190-Subarray_Sum_Queries",
  "1192-Counting_Rooms",
  "1195-Flight_Discount",
  "1197-Cycle_Finding",
  "1619-Restaurant_Customers",
  "1621-Distinct_Numbers",
  "1628-Meet_in_the_Middle",
  "1632-Movie_Festival_II",
  "1634-Minimizing_Coins",
  "1635-Coin_Combinations_I",
  "1636-Coin_Combinations_II",
  "1639-Edit_Distance",
  "1640-Sum_of_Two_Values",
  "1642-Sum_of_Four_Values",
  "1643-Maximum_Subarray_Sum",
  "1666-Building_Roads",
  "1667-Message_Route",
  "1668-Building_Teams",
  "1669-Round_Trip",
  "1671-Shortest_Routes_I",
  "1672-Shortest_Routes_II",
  "1674-Subordinates",
  "2166-Prefix_Sum_Queries",
  "2185-Prime_Multiples"
]

dirs = ["1071-Number_Spiral"]

faztudo_pre = (
"#!/bin/bash\n"
)

faztudo_power = (
"sudo modprobe msr\n"
"sudo ../RAPL/main "
)

faztudo_pos = (
"ulimit -s unlimited\n"
"make clean\n"
"make\n"
"speaker-test -t sine -f 1000 -l 1 -p20000\n"
)


cpu_on = (
"sudo echo 1 > /sys/devices/system/cpu/cpu1/online\n"
"sudo echo 1 > /sys/devices/system/cpu/cpu2/online\n"
"sudo echo 1 > /sys/devices/system/cpu/cpu3/online\n"
)


cpu_off = (
"sudo echo 0 > /sys/devices/system/cpu/cpu1/online\n"
"sudo echo 0 > /sys/devices/system/cpu/cpu2/online\n"
"sudo echo 0 > /sys/devices/system/cpu/cpu3/online\n"
)

logDir = "log/"
logFile = "myLog.txt"
prevDir = "../"
makefileDir = 'scripts/'
expDir = "last_run/"

def create_dir (mydir):
  if not os.path.exists(mydir):
    os.makedirs(mydir)

def write_log (msg):
  print(msg)
  with open(logDir + logFile, "a+") as f:
    f.write(f"{datetime.now()}: {msg}\n")

def getEntries():
  entries = [f for f in listdir("./test") if isfile(join("./test", f))]
  return entries


def generateEntryline(entries):
  line = "export TEST = "
  for ent in entries:
    line = line + "../test/" + ent + " "
  line = line + "\n"
  return line

def generateMakefileText(mydir, make_config, dataFormatada):
  lang = make_config.lang
  cpu = make_config.cpu
  machine = make_config.machine
  power_limit = make_config.power_limit

  texto = f"export PROBLEM = {mydir}-{lang}-{cpu}-{power_limit}W-{machine}-{dataFormatada}\n"

  texto  = texto + "export CPPFLAGS = -DONLINE_JUDGE -std=c++17 -O2" + "\n"
  
  texto = texto + "export OUTPUT = 2>&1 > /dev/null\n"
  
  entries = getEntries()
  entryline  = generateEntryline(entries)
  texto = texto + entryline
  texto = texto + f"all:\n\t+$(MAKE) -C {expDir}\n"
  texto = texto + f"clean:\n\trm {expDir}/*.exe  {expDir}/*.class\n"
  return texto


def createFazTudo(mydir, make_config):
  texto = faztudo_pre
  
  texto += cpu_on
  #if make_config.cpu == "sing":
  #  texto += cpu_off
  #else:
  #  texto += cpu_on
  
  texto += faztudo_power + " " + make_config.power_limit + "\n"
  
  texto += faztudo_pos
  
  with open("faztudo.sh","w") as f:
    f.write(texto) # write the data back
    f.truncate() # set the file size to the current size
  
  os.chmod("faztudo.sh", 0o775) 


def createMakefile(mydir, make_config, dataFormatada):
  texto = generateMakefileText(mydir, make_config, dataFormatada)
  with open("Makefile","w") as f:
    f.write(texto) # write the data back
    f.truncate() # set the file size to the current size


def generateexperimentdir(mydir, make_config):
  os.system('rm -rf ' + mydir + '/' + expDir)
  os.system('mkdir ' + mydir + '/' + expDir)
  lang = make_config.lang
  cmd = f"cp  {mydir}/{lang}/*  {mydir}/{expDir}"
  print(f"My cmd = {cmd}")
  os.system(cmd)


def copyMakefilesubdir(mydir, make_config):
  lang = make_config.lang
  if lang == 'c++':
    cmd = f"cp  {makefileDir}/Makefile-perf  {mydir}/{expDir}/Makefile"
  else:
    print(f'Unrecognized experiment type. Aborting.\nmake_config = {make_config}.')
    sys.exit()

  print(f"copy make {cmd}")
  os.system(cmd)


def config_parser(parser):
  parser.add_argument('lang', choices=['c++'])
  parser.add_argument('machine', choices=['elite'])
  parser.add_argument('cpu', choices=['sing', 'mult'])
  parser.add_argument('power_limit', choices=['0', '2', '10', '15', '25'])


parser = argparse.ArgumentParser(description='Generate makefiles.')
config_parser(parser)
make_config = parser.parse_args()
print(make_config)

dataAtual = datetime.now()
dataFormatada = dataAtual.strftime("%d-%m-%Y-%H-%M")

if not os.path.exists(logDir):
  os.makedirs(logDir)    
write_log("Generating Makefiles")


for mydir in dirs:
  write_log("Working on " + mydir)
  os.chdir(mydir)
  createFazTudo(mydir,make_config)
  createMakefile(mydir,make_config,dataFormatada)
  os.chdir(prevDir)
  generateexperimentdir(mydir, make_config)
  copyMakefilesubdir(mydir, make_config)
write_log("Makefiles Complete")

