#-*- coding:utf-8 -*-
#from mymethod import *
import re
todo_list = ['GSM1093506methration.txt',  'GSM1093512methration.txt',
'GSM1093507methration.txt',  'GSM1093513methration.txt'
]
def fileSelect01(a,b,chr,pos,ratio,f_CG,f_CHG,f_CHH):
	if a == 'G':
		x = 'CG_' + chr
		if dic[x] == 1:
			file_CG.write("variableStep chrom=" + chr + " span=1\n")
			dic[x] = 0
		file_CG.write(pos+"   "+ratio+"\n")
	elif a == 'C' or a == 'A' or a == 'T':
			if b == 'G':
				y = 'CHG_' + chr
				if dic[y] == 1:
					file_CHG.write("variableStep chrom=" + chr + " span=1\n")
					dic[y] = 0
				file_CHG.write(pos+"   "+ratio+"\n")	
			else:
				z = 'CHH_' + chr
				if dic[z] == 1:
					file_CHH.write("variableStep chrom=" + chr + " span=1\n")
					dic[z] = 0
				file_CHH.write(pos+"   "+ratio+"\n")
	else:
		z = 'CHH_' + chr
		if dic[z] == 1:
					file_CHH.write("variableStep chrom=" + chr + " span=1\n")
					dic[z] = 0
		file_CHH.write(pos+"   "+ratio+"\n")

def fileSelect02(a,b,chr,pos,ratio,f_CG,f_CHG,f_CHH):
	if a == 'C':
		x = 'CG_' + chr
		if dic[x] == 1:
			file_CG.write("variableStep chrom=" + chr + " span=1\n")
			dic[x] = 0
		file_CG.write(pos+"   "+ratio+"\n")
	elif a == 'G' or a == 'A' or a == 'T':
			if b == 'C':
				y = 'CHG_' + chr
				if dic[y] == 1:
					file_CHG.write("variableStep chrom=" + chr + " span=1\n")
					dic[y] = 0
				file_CHG.write(pos+"   "+ratio+"\n")	
			else:
				z = 'CHH_' + chr
				if dic[z] == 1:
					file_CHH.write("variableStep chrom=" + chr + " span=1\n")
					dic[z] = 0
				file_CHH.write(pos+"   "+ratio+"\n")
	else:
		z = 'CHH_' + chr
		if dic[z] == 1:
					file_CHH.write("variableStep chrom=" + chr + " span=1\n")
					dic[z] = 0
		file_CHH.write(pos+"   "+ratio+"\n")
for item in todo_list:
	dic = {"CG_Chr1":1,"CHG_Chr1":1,"CHH_Chr1":1,"CG_Chr2":1,"CHG_Chr2":1,"CHH_Chr2":1
       ,"CG_Chr3":1,"CHG_Chr3":1,"CHH_Chr3":1,"CG_Chr4":1,"CHG_Chr4":1,"CHH_Chr4":1
       ,"CG_Chr5":1,"CHG_Chr5":1,"CHH_Chr5":1,"CG_Chr6":1,"CHG_Chr6":1,"CHH_Chr6":1
       ,"CG_Chr7":1,"CHG_Chr7":1,"CHH_Chr7":1,"CG_Chr8":1,"CHG_Chr8":1,"CHH_Chr8":1
       ,"CG_Chr9":1,"CHG_Chr9":1,"CHH_Chr9":1,"CG_Chr10":1,"CHG_Chr10":1,"CHH_Chr10":1
       ,"CG_Chr11":1,"CHG_Chr11":1,"CHH_Chr11":1,"CG_Chr12":1,"CHG_Chr12":1,"CHH_Chr12":1
       ,"CG_ChrSy":1,"CHG_ChrSy":1,"CHH_ChrSy":1,"CG_ChrUn":1,"CHG_ChrUn":1,"CHH_ChrUn":1
       }
	file_GSM = open(item,'r')
	fcg = item[0:10] + '_CG.wig'
	fchg = item[0:10] + '_CHG.wig'
	fchh = item[0:10] + '_CHH.wig'
	file_CG = open(fcg,'w')
	file_CHG = open(fchg,'w')
	file_CHH = open(fchh,'w')
	pattern = re.compile(r'\s+')
	file_GSM.readline()
	for line in file_GSM:
		l = pattern.split(line)
		if l[2] == '+' and l[4] != 'NA':
			fileSelect01(l[3][3],l[3][4],l[0],l[1],l[4],file_CG,file_CHG,file_CHH)
		elif l[2] == '-' and l[4] != 'NA':
			fileSelect02(l[3][3],l[3][4],l[0],l[1],l[4],file_CG,file_CHG,file_CHH)
	file_GSM.close()
	file_CG.close()
	file_CHG.close()
	file_CHH.close()



