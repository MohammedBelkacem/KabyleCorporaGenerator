suffixes_COI=['yi','iyi','ak','am','as','aneɣ','aɣ','anteɣ','awen','awent','akent','aken','asen','asent','yak','yam','yas','yaneɣ','yaɣ','yantneɣ','yawen','yawent','yakent','yaken','yasen','yasent']
suffixes_COD=['t','tt','ten','tent','it','itt','iten','itent']
suffix_dir=['id','d','in','n']

sentences=[]

def form_COI(word,suffixes_COI):
    list=[]
    for x in suffixes_COI:
        if word[len(word)-1] not in ['i','a','u'] and x[0]!='y':
            list.append(word+'-'+x)
        else:
            if word[len(word)-1] in ['i','a','u'] and x!='iyi':
             list.append(word+'-'+x)
    return list

def form_COD(word,suffixes_COD):
    list=[]
    for x in suffixes_COD:
        if word[len(word)-1] not in ['i','a','u'] and x[0]=='i':
            list.append(word+'-'+x)
        else:
            if word[len(word)-1] in ['i','a','u'] and x[0]!='i':
               list.append(word+'-'+x)
    return list
def form_Dir(word,suffix_dir):
    list=[]
    for x in suffix_dir:
        if x[0] !='i':
            list.append(word+'-'+x)
    return list

def form_COI_COD(word,suffixes_COI,suffixes_COD):
    list=[]
    words=form_COI(word,suffixes_COI)
    #print(words)
    for i in words:
        for j in suffixes_COD:
            if i[len(i)-1] not in ["a","i","u"] and j[0]!="i":
             list.append(i+'-'+j)
    return list

def form_COI_Dir(word,suffixes_COI,suffix_dir):
    list=[]
    words=form_COI(word,suffixes_COI)
    #print(words)
    for i in words:
        for j in suffix_dir:
            if i[len(i)-1] not in ["a","i","u"]:
             list.append(i+'-'+j)
            else:
                if i[len(i)-1]  in ["a","i","u"] and j[0]!="i":
                    list.append(i+'-'+j)
    return list

def form_COD_Dir(word,suffixes_COD,suffix_dir):
    list=[]
    words=form_COI(word,suffixes_COD)
    #print(words)
    for i in words:
        for j in suffix_dir:
            if i[len(i)-1] not in ["a","i","u"]  and j[0]=="i":
             list.append(i+'-'+j)

    return list

def form_COI_COD_Dir(word,suffixes_COI,suffixes_COD,suffix_dir):
    list=[]
    words=form_COI_COD(word,suffixes_COI,suffixes_COD)
    #print(words)
    for i in words:
        for j in suffix_dir:
            if i[len(i)-1] not in ["a","i","u"] and j[0]=="i":
             list.append(i+'-'+j)
    return list


words=["ifka","ttaken","ttakent","fkan","efk"]
##for i in words:
##    form_COI(i,suffixes_COI)
##for i in words:
##    form_COD(i,suffixes_COD)
sentences=[]
for i in words:
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
