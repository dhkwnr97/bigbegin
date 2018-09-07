#input_samFile
import sys

input_sam=open(sys.argv[1],'r')
newName=sys.argv[1].replace(".sam","_OnlyJ.sam")
output_sam=open(newName,'w')

while True:
	oneL=input_sam.readline()
	
	if not oneL:
		break#if end of file, finish loop
	if oneL.startswith('@'):
		output_sam.write(oneL)#if @tag line, just write it!
		continue
	spline=oneL.split('\t')
	juncP_code=spline[5]#if juncPossible_code include N, write new sam file
	if 'N' in juncP_code:
		output_sam.write(oneL)
		
input_sam.close()
output_sam.close()