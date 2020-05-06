suffixes_COI=['iyi','ak','am','as','aneɣ','aɣ','antneɣ','awen','awent','akent','aken','asen','asent']
suffixes_COD=['t','tt','ten','tent']
suffix_dir=['id','d']
words=["ur fkiɣ ara"]
sentences=[]
for p in words:
    word=p[3:len(p)-4]
    for i in suffixes_COI:
        word1=i+'-'+word
        if word1 not in sentences:
            sentences.append(word1)
        for j in suffixes_COD:
            word2=j+'-'+word
            if word2 not in sentences:
             sentences.append(word2)
            word3=i+'-'+j+'-'+word
            if word3 not in sentences:
             sentences.append(word3)
            for k in suffix_dir:

                word4=k+'-'+word
                if word4 not in sentences:
                    sentences.append(word4)
                word5=i+'-'+k+'-'+word
                if word5 not in sentences:
                    sentences.append(word5)

                word6=j+'-'+k+'-'+word
                if word6 not in sentences:
                   sentences.append(word6)
                word7=i+'-'+j+'-'+k+'-'+word
                if word7 not in sentences:
                     sentences.append(word7)

for i in sentences:
    print ('ur '+i+' ara')