suffixes_COI=['iyi','ak','am','as','aneɣ','aɣ','antneɣ','awen','awent','akent','aken','asen','asent']
suffixes_COD=['t','tt','ten','tent','ken','kent','k','kem']
suffix_dir=['id','d']
words=["efk"]
sentences=[]
for word in words:
    for i in suffixes_COI:
        word1=word+'-'+i
        if word1 not in sentences:
            sentences.append(word1)
        for j in suffixes_COD:
            word2=word+'-'+j
            if word2 not in sentences:
             sentences.append(word2)
            word3=word1+'-'+j
            if word3 not in sentences:
             sentences.append(word3)
            for k in suffix_dir:
                if k[0] not in ['i']:
                 word4=word+'-'+k
                 if word4 not in sentences:
                    sentences.append(word4)
                if i[len(i)-1] in ['i'] and k[0] not in ['i']:
                 word5=word1+'-'+k
                 #print(word5)
                 if word5 not in sentences:
                    sentences.append(word5)
                if k[0] in ['i']:
                 word6=word2+'-'+k
                 if word6 not in sentences:
                   sentences.append(word6)
                if k[0] in ['i']:
                  word7=word3+'-'+k
                  if word7 not in sentences:
                     sentences.append(word7)

for i in sentences:
    print (i)