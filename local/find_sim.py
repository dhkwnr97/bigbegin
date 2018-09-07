import sys

def mknkey(tbytab):
    lines = tbytab.readlines()[1:]
    dickeys = {}
    for i in lines:
        t = i.strip('\n')
        dickeys[(t.split('\t')[1])] = ''
    return dickeys

def mkid_val(gtfbytab):
        lines = gtfbytab.readlines()
        idval = {}
        for j in lines:
                t = j.strip('\n')
                tspt = t.split('\t')[-1]
                tspt2 = (tspt.split(';')[3]).split('"')
                if len(tspt2) > 2 :
                        idval[(tspt.split(';')[1]).split('"')[1]]=(tspt.split(';')[3]).split('"')[1]
        return idval

f = open(sys.argv[1],'r')
gtf = open(sys.argv[2],'r')

df = mknkey(f)
dgtf = mkid_val(gtf)
dfklst = df.keys()

for x in dfklst:
        if dgtf.has_key(x):
                df[x] = dgtf[x]
        else:
                df[x] = 'No reference'

fnew = open('/home/hanjg/Ogol_by_chic_less.txt','w')
for z in df:
        fnew.write(z+'\t'+df[z]+'\n')

f.close()
gtf.close()
fnew.close()