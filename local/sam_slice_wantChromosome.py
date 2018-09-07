#input_SAM_file(must sorted like: chr1, chr2 ...)"/spbar"want_chromosome(like:chr1, chrM ...)
import sys

input_sam=open(sys.argv[1],'r')
newfName=sys.argv[1].replace('.sam','.'+sys.argv[2]+'.sam')
output_sam=open(newfName,'w')

write_signal=False
line_List=input_sam.readlines()
indexN=0
for l in line_List:
        if l.startswith('@'):
                output_sam.write(l)
                indexN+=1
                continue

        sptl=l.split('\t')
        if sptl[2]==sys.argv[2]:
                output_sam.write(l)
                if str(line_List[indexN+1].split('\t')[2]) != str(sys.argv[2]):
                        print("lastline="+line_List[indexN])
                        print("NextLine ="+line_List[indexN+1]+"= so end search and write")
                        break#if next search line is different chromosome => end write
        indexN+=1

input_sam.close()
output_sam.close()