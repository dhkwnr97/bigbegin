import sys

f_sam=open(sys.argv[1],'r')
s_sam=open(sys.argv[2],'r')

f_lineList=f_sam.readlines()
s_lineList=s_sam.readlines()

indexN=0
for l in f_lineList:
	if not (l in s_lineList[indexN]):
		print(l)
		print(s_lineList[indexN])
		print("diff!_lineNumber :"+str(indexN+1))
		break
	indexN+=1

f_sam.close()
s_sam.close()
