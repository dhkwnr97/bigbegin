#input gtffile(spacebar)Sigle exon FPKM Threshold(spacebar)Multy exon FPKM Thresholdimport sys

gtf = open(sys.argv[1],'r')
rename=sys.argv[1].replace('.gtf','_SigMulFPKMcut.gtf')
SMcut_gtf = open(rename,'w')
sigTreshold=float(sys.argv[2])
mulTreshold=float(sys.argv[3])

imsi_list=[]
gtf_linelist=gtf.readlines()
for oneline in gtf_linelist: 
    if oneline.split('\t')[2] == 'transcript':#it`s transcript information line
        if len(imsi_list) > 2:#if transcript has multiple exon
            if float(imsi_list[0].split('"')[5]) >= float(mulTreshold):#it`s FPKM value >= mulTreshold
                for i in imsi_list:
                    SMcut_gtf.write(i)
        elif len(imsi_list) == 2:#if transcript has single exon
            if float(imsi_list[0].split('"')[5]) >= float(sigTreshold):
                for i in imsi_list:
                    SMcut_gtf.write(i)
        imsi_list=[]#transcript imsi_list initialization
    imsi_list.append(oneline)#transcript and exon just putin imsi_list and checking code 17~

#####################################################################################
if len(imsi_list) > 2:#if transcript has multiple exon
    if float(imsi_list[0].split('"')[5]) >= float(mulTreshold):#it`s FPKM value >= mulTreshold
        for i in imsi_list:
            SMcut_gtf.write(i)
elif len(imsi_list) == 2:
    if float(imsi_list[0].split('"')[5]) >= float(sigTreshold):
        for i in imsi_list:
            SMcut_gtf.write(i)
#check for the last trascript
#####################################################################################
gtf.close()
SMcut_gtf.close()