#input:refernce gtf file(spacebar)need cutting gtf file include single exon transcript(spacebar)how many basepair
import sys datetime
import FindLessNum_byTree as ftree

ref_gtf_f=open(sys.argv[1],'r')
checking_gtf_f=open(sys.argv[2],'r')
newname=sys.argv[1].replace('.gtf','_refNearSigEcut.gtf')
final_file=open(newname,'w')
bp_value=int(sys.argv[3])

nowtime=datetime.datetime.now()

print("starting job clock"+nowtime)
dzp_list=[]#list in only pluse strands
dzm_list=[]#list in only minus strands
ref_lines=ref_gtf_f.readlines()
for oneline in ref_lines:
	
	if oneline.startswith('#'):
		continue#ignore discripttion in file
	
	spt=oneline.split('\t')
	if spt[2] == 'exon':
		if spt[6]=='+':
			dzp=(int(spt[3])-bp_value,int(spt[4])+bp_value)#dzp=[dz_minimum,dz_maximum,]
			dzp_list.append(dzp)
		else:
			dzm=(int(spt[3])-bp_value,int(spt[4])+bp_value)#dzm=[dz_minimum,dz_maximum,]
			dzm_list.append(dzm)
dzp_list.sort()
dzm_list.sort()
#dzp or dzm_list form: [[18246,19752],[421574,422487], ...]
print("making sorted darkzone_list done"+nowtime)

def MkIntegList(list_input):
	new_dz_list=[]
	i=0#end while loop standard value
	j=0#new_list counter
	while i < len(list_input):#end of darkzone list, escape while loop
		if list_input[i][0] in range(new_dz_list[j][0],new_dz_list[j][1]):
			new_dz_list[j][1]=list_input[i][1]
		else:
			new_dz_list.append(list_input[i])
			j=j+1
		i=i+1
	return new_dz_list
'''
for example,
[[1,12], [4,16], [19,21]]
-> make one  [[1,16], [19,21]]
just integrate overlapping region
'''
intg_dzp_list=MkIntegList(dzp_list)
intg_dzm_list=MkIntegList(dzm_list)
print("making integrate! sorted darkzone_list done"+nowtime)
#dzp or dzm_list form: [[18246,19752],[421574,422487], ...] also whole integrated

def Findmiddle_dz(inputL):
	indexN=int(len(inputL)/2)
	middle_dz=inputL[indexN]
	return middle_dz
m_p_dz=Findmiddle_dz(intg_dzp_list)
m_m_dz=Findmiddle_dz(intg_dzm_list)

p_serchT=ftree.BinarySearchTree()
p_serchT.put(m_p_dz[0], m_p_dz)#Plus strand dz mid point into tree
m_serchT=ftree.BinarySearchTree()
m_serchT.put(m_m_dz[0], m_m_dz)#Minus strand dz mid point into tree
withoutM_p_list=intg_dzp_list.remove(m_p_dz)
withoutM_m_list=intg_dzm_list.remove(m_m_dz)

for wholeP_dz in withoutM_p_list:
	p_serchT.put(wholeP_dz[0], wholeP_dz)
for wholeM_dz in withoutM_m_list:
	m_serchT.put(wholeM_dz[0], wholeM_dz)
print("complete make darkzone tree"+nowtime)


'''
def MkSearchTree(list_input):
	midatomN=int(len(list_input)/2)+1
	node_value=list_input[midatomN-1]
	Binary_Surch_Tree_dic{node_value[0]:[node_value]}
	left_list=[:midatomN-2]#half of left
	right_list=[midatomN:]#half of right	
	if len(left_list)==1:#left node calculate
		left_node=left_list[0]
		Binary_Surch_Tree_dic[node_value[0]].insert(0,left_node)
	elif len(left_list)==0:
		Binary_Surch_Tree_dic[node_value[0]].insert(0,'null')
	else:
		midatomN=int(len(left_list)/2)+1
		left_node=left_list[midatomN-1][0]
		Binary_Surch_Tree_dic[node_value[0]].insert(0,left_node)
	if len(right_list)==1:#right node calculate
		right_node=right_list[0]
		Binary_Surch_Tree_dic[node_value[0]].insert(2,right_node)
	elif len(left_list)==0:
		Binary_Surch_Tree_dic[node_value[0]].insert(2,'null')
	else:
		midatomN=int(len(right_list)/2)+1
		right_node=right_list[midatomN-1][0]
		Binary_Surch_Tree_dic[node_value[0]].insert(2,right_node)
	
	MkSearchTree(left_list)
	MkSearchTree(right_list)
	return Binary_Surch_Tree_dic
'''


imsi=[]
check_right=True
while True:
	cut_oneline=checking_gtf_f.readline()
	
	if not cut_oneline:
		break#if end of file, escape while loop
	
	spt=cut_oneline.split('\t')
	if spt[2] == 'transcript':
		if len(imsi) > 2:#if imsi in multiple exon transcript
			check_right=True
		elif len(imsi) == 2:#if imsi in single exon transcript
			if imsi[0].split('\t')[6] == '+':#checking only '+' library
				darkZone=p_serchT.getlessN(imsi[0].split('\t')[3])#most left near darkZone
				if imsi[0].split('\t')[4] in darkZone:#single transcript not in darkzone
					check_right=False
			elif imsi[0].split('\t')[6] == '-':#checking only '-' library
				darkZone=m_serchT.getlessN(imsi[0].split('\t')[3])#most left near darkZone
				if imsi[0].split('\t')[4] in darkZone:#single transcript in darkzone
					check_right=False
			if check_right==True:
				final_file.writelines(imsi)#no problem data write
			print("one_data_done")
		check_right=True#initializtion for check other transcript
		imsi=[]#initializtion for check other transcript
	imsi.append(cut_oneline)#trc or exon whatever just put in imsi box

###########################################################################
if len(imsi) > 2:#if imsi in multiple exon transcript
	check_right=True
elif len(imsi) == 2:#if imsi in single exon transcript
	if imsi[0].split('\t')[6] == '+':#checking only '+' library
		darkZone=p_serchT.getlessN(imsi[0].split('\t')[3])#most left near darkZone
		if imsi[0].split('\t')[4] in darkZone:#single transcript not in darkzone
			check_right=False
	elif imsi[0].split('\t')[6] == '-':#checking only '-' library
		darkZone=m_serchT.getlessN(imsi[0].split('\t')[3])#most left near darkZone
		if imsi[0].split('\t')[4] in darkZone:#single transcript in darkzone
			check_right=False
	if check_right==True:
		final_file.writelines(imsi)#no problem data write
	print("one_data_done")
#check the last transcript
###########################################################################

ref_gtf_f.close()
checking_gtf_f.close()
final_file.close()