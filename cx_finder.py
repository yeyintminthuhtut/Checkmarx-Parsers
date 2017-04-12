####################################################################
#  Copyright By Ye Yint Min Thu Htuts
#  Description:
#  Issue new Cx result by checking on source files where last modified date is according to user defined date
####################################################################
#### DO NOT EDIT LINES BELOW #############

import os
import datetime
import time
import csv
import sys
os.system('cls')
os.system('color f0')
infile = raw_input("Provide your cx file in csv format:\n (E.g: C:\Users\pentester\Desktop\inscope_finder\mycxfile.csv )\n\n")

if os.path.isfile(infile) and os.access(infile, os.R_OK):
	CONST_NO_OF_DAY = raw_input("\n\nDefine when the application was modified.\n\n (eg. If it was 90 days ago, put 90.)\n\n")
else:
	print "Either file is missing or permission error"
	sys.exit()
head, tail = os.path.split(infile)
tail = tail.replace(".csv","")
resultfile = head + os.path.sep + tail + "_result.csv"
with open(infile,'r') as csvfile:
	with open(resultfile,'a') as outfile:
		reader = csv.DictReader(csvfile)
		header = "Query, FileName, Line, NodeId, Name, Type, DestFileName, DestLine, DestColumn, DestNodeId, DestName, DestType, Modification Date, Comment\n"
		outfile.write(header)
		for column in reader:
			qu = (column['Query'])
			F = (column['FileName'])
			line = (column['Line'])
			NodID = (column['NodeId'])
			na = (column['Name'])
			typ3 = (column['Type'])
			dstfname = (column['DestFileName'])
			dstline = (column['DestLine'])
			dstcol = (column['DestColumn'])
			dstnd = (column['DestNodeId'])
			dstname = (column['DestName'])
			dsttype = (column['DestType'])
			modi_date = datetime.datetime.fromtimestamp(os.path.getmtime(F))
			today = datetime.datetime.today()
			duration = today - modi_date
			if duration.days < CONST_NO_OF_DAY:
				a = "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, In Scope\n" % (qu, F, line, NodID, na, typ3, dstfname, dstline, dstcol, dstnd, dstname, dsttype, modi_date)
				outfile.write(a)

print "\n\nDone! Your result filename is: " + resultfile

			





