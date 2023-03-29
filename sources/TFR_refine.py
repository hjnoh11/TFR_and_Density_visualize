import csv
import copy

f1=open("../rawdata/2022_SGG_TFR_utf8.csv",'r',encoding='utf-8-sig')
f2=open("../rawdata/2022_SGG_TFR_merge.csv",'w',encoding='utf-8',newline='')
reader=csv.reader(f1)
writer=csv.writer(f2)
writer.writerow(["Sgis_code","birth","TFR"])
for line in reader:
	templine=copy.deepcopy(line)
	templine[0]=(str(templine[0]).split(" ")[0])
	writer.writerow(templine)
f1.close()
f2.close()