suffixes_COI=['yi','iyi','ak','am','as','aneɣ','aɣ','anteɣ','awen','awent','akent','aken','asen','asent','k','m','s','ɣ','wen','went','kent','ken','sen','sent']
suffixes_COD=['t','tt','ten','tent','it','itt','iten','itent']
suffix_dir=['id','d','in','n']

sentences=[]

def form_COI(word,suffixes_COI):
    list=[]
    for x in suffixes_COI:
        if x[0] !='y':
            list.append("ad "+x+"-"+word)
    return list

def form_COD(word,suffixes_COD):
    list=[]
    for x in suffixes_COD:
        if x[0] !='i':
            list.append("ad "+x+"-"+word)
    return list
def form_Dir(word,suffix_dir):
    list=[]
    for x in suffix_dir:
        if x[0] !='i':
             list.append("ad "+x+"-"+word)
    return list

def form_COI_COD(word,suffixes_COI,suffixes_COD):
    list=[]
    words=form_COI(word,suffixes_COI)
    #print(words)
    for i in words:
        x=i.split('-')
        for j in suffixes_COD:
            if j[0]!="i":
             list.append(x[0]+'-'+j+'-'+x[1])
    return list

def form_COI_Dir(word,suffixes_COI,suffix_dir):
    list=[]
    words=form_COI(word,suffixes_COI)
    #print(words)
    for i in words:
        x=i.split('-')
        for j in suffix_dir:
            #if j[0]!="i":
             list.append(x[0]+'-'+j+'-'+x[1])
    return list

def form_COD_Dir(word,suffixes_COD,suffix_dir):
    list=[]
    words=form_COI(word,suffixes_COD)
    #print(words)
    for i in words:
        x=i.split('-')
        for j in suffix_dir:
            y=x[0].split(" ")
            if y[1][0]!="i" and j[0]=='i':
             list.append(x[0]+'-'+j+'-'+x[1])
    return list

def form_COI_COD_Dir(word,suffixes_COI,suffixes_COD,suffix_dir):
    list=[]
    words=form_COI_COD(word,suffixes_COI,suffixes_COD)
    #print(words)
    for i in words:
        x=i.split('-')
        for j in suffix_dir:
            if j[0]=='i':
             list.append(x[0]+'-'+x[1]+'-'+j+'-'+x[2])

    return list


words=["ad yefk"]
##for i in words:
##    form_COI(i,suffixes_COI)
##for i in words:
##    form_COD(i,suffixes_COD)
sentences=[]
for i in words:
 i=i.split(" ")
 i=i[1]
 awalen=form_COI(i,suffixes_COI)
 sentences.append(awalen)
 awalen=form_COD(i,suffixes_COD)
 sentences.append(awalen)
 awalen=form_Dir(i,suffix_dir)
 sentences.append(awalen)
 awalen=form_COI_COD(i,suffixes_COI,suffixes_COD)
 sentences.append(awalen)
 awalen=form_COI_Dir(i,suffixes_COI,suffix_dir)
 sentences.append(awalen)
 awalen=form_COD_Dir(i,suffixes_COD,suffix_dir)
 sentences.append(awalen)
 awalen=form_COI_COD_Dir(i,suffixes_COI,suffixes_COD,suffix_dir)
 sentences.append(awalen)

for i in sentences:
    for j in i:
        print(j)
