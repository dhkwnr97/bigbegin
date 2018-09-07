#input cuffcompare_tracking_file(spacebar)input gtf_file(spacebar)lots of typecode with comma:(u,x,i,j/like this)
import sys
trcfile=open(sys.argv[1],'r')
inputgtf=open(sys.argv[2],'r')
newname=sys.argv[2].replace('.gtf','_'+sys.argv[3]+'_types.gtf')
final_file=open(newname,'w')

findtype_list=list(sys.argv[3].split(','))#make input type code list:	[u,x,i,j]

def serch(trcfile):
        target_gtname_list = []
        while True:
                trc_oneline = trcfile.readline()
                if not trc_oneline:
                        break #at the end of file, we break out while loop
                noenter = trc_oneline.strip('\n')
                sptab = noenter.split('\t')
                if sptab[3] in findtype_list:
                        spbar = (sptab[-1]).split('|')
                        target_gtname_list.append(spbar[0][3:]+'-'+spbar[1])
						#if matching typecode save in target_gtname_list['gene_name-transcript_name', ...]
        return target_gtname_list

def findNwrite(gtffile, target_gtname_list):
        while True:
                oneline = gtffile.readline()
                
				if not oneline:
                        break#if end of file, break the while loop
                
				if '#' in oneline:
                        continue#if there is description in file, ignore them
						
                sptab = oneline.split('\t')
                spdaom = sptab[-1].split('"')
                matchcheck = spdaom[1]+'-'+spdaom[3]
                if matchcheck in target_gtname_list:
                        final_file.write(oneline)

search_in_tracking = serch(trcfile)
findNwrite(inputgtf, search_in_tracking)

trcfile.close()
inputgtf.close()
final_file.close()