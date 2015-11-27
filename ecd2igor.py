#!/usr/bin/env python

import os
import re
import shutil
from sys import argv
BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

outputpath = os.getcwd() + "/output/"
start = 0
if os.path.exists(outputpath):
        print FAIL + "Debag Mode On --- \"output\" directory already exist!!! --- " + ENDC
	print ">>delete \"output\" directory ? " + BLUE + "(yes/no)" + ENDC
	de = 0
	while de < 1:
		yn = raw_input(">>")
		if yn == "yes":
			shutil.rmtree("output")
			print ">>" + FAIL + "\"output\" deleted!!!" + ENDC
			print ">>continue ? " + BLUE + "(yes/no)" + ENDC
			while start < 1:
				swit = raw_input(">>")
				if swit == "yes":
					start = 1
				elif swit == "no":
					break
				else:
					print ">>" + FAIL + "input \"yes\" or \"no\"" + ENDC
			break
		elif yn == "no":
			break
		else:
			print ">>" + FAIL + "input \"yes\" or \"no\"" + ENDC
else:
	start = 1
if start == 0:
	pass
else:
    os.mkdir("output")
    iselect = []
    path = os.getcwd()
    file_list = os.listdir(path)
    aa = 0
    bb = 0
    for file in file_list:
        file = os.path.join(path,file)
        if os.path.isdir(file):
            os.chdir(file)
	    bb = bb + 1
            for filename in os.listdir(file):
                name = file.split("/")[-1]
                if filename.endswith("ecd"):
			f1 = open(filename)
			outputname = filename.replace('.ecd',"."+name+'.csv')
			iselect.append(outputname)
			f2 = open(outputname,"w")
			for line1 in f1.readlines():
				if re.match('^[0-9]',line1):
					line2 = ",".join(line1.split("\t"))
					f2.write(line2)
			f2.close()
			shutil.move(outputname,path)
			os.chdir(path)
			print "running... in",name,filename,"->"+GREEN+outputname+ENDC
			shutil.move(outputname, "output")
			f1.close()
			os.chdir(file)
			aa = aa + 1
            os.chdir(file)        
    os.chdir(path)
    print WARNING + "--- integrate parameter select ---" + ENDC
    ab = aa/(bb-1)
    tsk = 0
    while tsk < 1:
	    lig = []
	    dd = 0
	    print ">>parameter select " + BLUE + "(auto/manual)" + ENDC
	    tsn = 0
	    while tsn < 1:
		    ts = raw_input(">>")
		    if ts == "auto":
			    break
		    elif ts == "manual":
			    break
		    else:
			    print ">>" +FAIL+ "input \"auto\" or \"manual\"" + ENDC
	    if ts == "auto":
		    while dd < ab:
			    print WARNING+"|"+ENDC+iselect[dd].split(".")[0]+WARNING+"| "+BLUE+"(on/off)"+ENDC+" on"
			    lig.append(iselect[dd].split(".")[0])
			    dd = dd + 1
	    elif ts == "manual":
		    while dd < ab:
			    jk = 0
			    while jk < 1:
				    str = raw_input(WARNING+"|"+ENDC+iselect[dd].split(".")[0]+WARNING+"| "+BLUE+"(on/off) "+ENDC)
				    if str == "on":
					    break
				    elif str == "off":
					    break
				    else:
					    print ">>" + FAIL + "input \"on\" or \"off\"" + ENDC
			    if str == "on":
				    lig.append(iselect[dd].split(".")[0])
			    else:
				    pass
			    dd = dd + 1
	    print ">>parameter select, ok? " + BLUE + "(ok/retry)" + ENDC
	    endc = 0
	    while endc < 1:
		    target = raw_input(">>")
		    if target == "ok":
			    tsk = 1
			    endc = 1
		    elif target == "retry":
			    endc = 1
		    else:
			    print ">>" + FAIL + "input \"ok\" or \"retry\"" + ENDC
    print WARNING + "--- integrate parameter selected ---" + ENDC
    print ">>file.csv -> " +GREEN+ "output" + ENDC
    print ">>integrating .csv file "
    outputpath = os.getcwd() +"/output/"
    csvpath = outputpath + "/integrated.csv"
    name_list = []
    name_2nd = []
    for line4 in os.listdir(outputpath):
	    line5 = line4.split(".")[0]
	    line8 = line4.split(".")[1]
	    if line5 in lig:
		    name_list.append(line5)
		    name_2nd.append(line8)
    if os.path.exists(csvpath):
	    print FAIL + ">>Debag Mode On --- integrated.csv already exist!!! ---" + ENDC
    else:
	    os.chdir(outputpath)
	    file_list = os.listdir(outputpath)
	    f1 = open("integrated.csv","w")
	    length = []
	    i = 0
	    file_list_2 = []
	    for line6 in file_list:
		    line7 = line6.split(".")[0]
		    if line7 in lig:
			    file_list_2.append(line6)
	    cd = open(file_list_2[0],"r")
	    for line in cd:
		    length.append(line.rstrip())
	    while i < len(length):
		    latest = []
		    for file in file_list_2:
			    data = open(file,"r")
			    list = []
			    for line in data:
				    list.append(line.rstrip())
			    latest.append(list[i]) 
		    j = 0
		    for line2 in latest:
			    line3 = line2.rsplit(',')
			    if j < 1:
				    f1.write(line3[0]+","+line3[1]+",")
				    j = j + 1
			    else:
				    f1.write(line3[1]+",")
		    f1.write("\n")
		    i = i + 1
	    f1.close
	    print ">>integrated! -> " + GREEN + "integrated.csv" + ENDC
	    os.chdir(outputpath)
	    k = 0
	    s = 0
	    print WARNING + "--- IGOR plot setting ---" + ENDC
	    while s < 1:
		    print ">>IGOR plot setting " + BLUE + "(auto/manual)" + ENDC
		    while k < 1:
			    igor = raw_input(">>")
			    if  igor == "auto":
				    k = k + 1
			    elif igor == "manual":
				    k = k + 1
			    else:
				    print ">>"+ FAIL + "input \"auto\" or \"manual\"" + ENDC
		    if igor == "auto":
			    print WARNING+"|"+ENDC+"wave defining"+WARNING+"| "+BLUE+"(auto/manual) "+ENDC+"auto"
			    wave = "auto"
			    print WARNING+"|"+ENDC+"save to 4kjpg"+WARNING+"| "+BLUE+"(on/off) "+ENDC+"off"
			    save = "off"
			    print WARNING+"|"+ENDC+"graphoverplot"+WARNING+"| "+BLUE+"(on/off) "+ENDC+"off"
			    over = "off"
		    elif igor == "manual":
			    k = 0
			    while k < 1:
				    wave = raw_input(WARNING+"|"+ENDC+"wave defining"+WARNING+"| "+BLUE+"(auto/manual) "+ENDC)
				    if wave == "auto":
					    k = k + 1
				    elif wave == "manual":
					    k = k + 1
				    else:
					    print ">>" + FAIL + "input \"auto\" or \"manual\"" + ENDC
			    k = 0
			    while k < 1:
				    save = raw_input(WARNING+"|"+ENDC+"save to 4kjpg"+WARNING+"| "+BLUE+"(on/off) "+ENDC)
				    if  save == "on":
					    k = k + 1
				    elif save == "off":
					    k = k + 1
				    else:
					    print ">>" + FAIL + "input \"on\" or \"off\"" + ENDC
			    k = 0
			    while k < 1:
				    over = raw_input(WARNING+"|"+ENDC+"graphoverplot"+WARNING+"| "+BLUE+"(on/off) "+ENDC)
				    if  over == "on":
					    k = k + 1
				    elif over == "off":
					    k = k + 1
				    else:
					    print ">>" + FAIL + "input \"on\" or \"off\"" + ENDC
		    t = 0
		    print ">>IGOR plot setting, ok? " + BLUE + "(ok/retry)" + ENDC
		    while t < 1:
			    cr = raw_input(">>")
			    if cr == "ok":
				    s = 1
				    t = 1
			    elif cr == "retry":
				    k = 0
				    t = 1
			    else:
				    print ">>" +FAIL + "input \"ok\" or \"retry\"" + ENDC
	    print WARNING + "--- IGOR plot setting end ---" + ENDC
	    if wave == "auto":
		    print WARNING + "--- wave auto define ---" + ENDC
		    file3 = open("igor_display.txt","w")
		    i = 1
		    file3.write("Rename wave0,times\n")
		    print "wave0 -> times"
		    while i <= len(name_list):
			    file3.write("Rename wave"+`i`+","+name_list[i-1]+name_2nd[i-1]+"\n")
			    print "wave"+`i`+" -> "+name_list[i-1]+name_2nd[i-1]
			    if over == "on":
				    if i > 1:
					    file3.write("AppendToGraph "+name_list[i-1]+name_2nd[i-1]+" vs times\n")
				    else: 
					    file3.write("Display "+name_list[i-1]+name_2nd[i-1]+" vs times\n")
			    elif over == "off":
				    file3.write("Display "+name_list[i-1]+name_2nd[i-1]+" vs times\n")
				    if save == "on":
					    file3.write("SavePICT/Q=1/T=\"JPEG\"/B=288 as \""+name_list[i-1]+name_2nd[i-1]+".jpg\"\n")
				    else:
					    pass
			    else:
				    pass
			    i = i + 1
		    if over == "on":
			    if save == "on":
				    file3.write("SavePICT/Q=1/T=\"JPEG\"/B=288 as \""+"overplot"+".jpg\"\n")
			    elif save == "off":
				    pass
		    elif over == "off":
                            pass	
		    i = 1
		    j = j + 1
		    print WARNING + "--- waves were defined ---" + ENDC
	    elif wave == "manual":
		    print WARNING + "--- wave define manual mode on ---" + ENDC
		    wnl = []
		    print ">>input \"wave name\" or \"pass\""
		    file3 = open("igor_display.txt","w")
		    i = 1
		    file3.write("Rename wave0,times\n")
		    print "wave0 -> times"
		    number = []
		    igorlist = ['times','pass']
		    while i <= len(name_list):
			    igorlist.append("wave"+`i`)
			    i = i + 1
		    i = 1
		    cc = 0
		    while i <= len(name_list):
			    m = 0
			    while m < 1:
				    tfn = raw_input("wave"+`i`+" -> ")
				    if tfn == "pass":
					    m = m + 1		    
				    elif tfn in igorlist:
					    print ">>" + FAIL + "\"" + tfn  + "\" already exist!" + ENDC
				    else:
					    igorlist.append(tfn)
					    m = m + 1
			    if tfn == "pass":
				    pass
			    else:
				    file3.write("Rename wave"+`i`+","+tfn+"\n")
				    if over == "on":
					    if cc > 0:
						    file3.write("AppendToGraph "+tfn+" vs times\n")
					    elif cc == 0:
						    file3.write("Display "+tfn+" vs times\n")
						    cc = 1
				    elif over == "off":
					    file3.write("Display "+tfn+" vs times\n")
					    if save == "on":
						    file3.write("SavePICT/Q=1/T=\"JPEG\"/B=288 as \""+tfn+".jpg\"\n")
					    elif save == "off":
						    pass
				    number.append(tfn)
			    i = i + 1
                    if over == "on":
                            if save == "on":
                                    file3.write("SavePICT/Q=1/T=\"JPEG\"/B=288 as \""+"overplot"+".jpg\"\n")
                            elif save == "off":
                                    pass
                    elif over == "off":
                            pass
		    print WARNING + "--- waves were defined ---" + ENDC
	    else:
		    print ">>" + FAIL + "input \"auto\" or \"manual\"" + ENDC
    i = 1
    file3.close
    print ">>IGOR script finished!! -> " + GREEN + "igor_display.txt" + ENDC
    print ">>Your Project Finished!!!"
    print "--------------------------------------------"
    print "load \"" + GREEN + "integrated.csv" + ENDC +"\" without options"
    print "copy \"" + GREEN + "igor_display.txt" + ENDC +"\" and paste to IGOR"
    print "--------------------------------------------"
