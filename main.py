# irrelevant_words function
def iwords(text):
    irrelevant_words = {".", ",",  " \n ", " the ", " a ", " and ","\n",' how '," ",' be ',' as ',' could ',' are ',
                        " is ", " was ", " he ", " at ", " to ", " for ", " can ", " this ", " we ", " you ",' it ','many'
                        ," or ", " i ", " an "," but ", " so ", " yes ", " no ", " of " , '!',' thought ',' that ',' him ',
                        ' its '}
    for iw in irrelevant_words:
        text = text.replace(iw, " ")


    return(text)

# The number of repetitions of the word in the article
def histogram(text):
    word_histogram = {

      }

    #print('word_list')
    #print(text)

    for word in word_list:
        if word not in word_histogram.keys():
            word_histogram[word] = 1
        else:
            word_histogram[word] = word_histogram[word] + 1

    try:
        word_histogram.pop("")
    except KeyError:
        pass
    #if enter:
        #print('---------2')       #extra
        #print(word_histogram)     #extra
    return dict(list(sorted(word_histogram.items(), key=lambda kv: kv[1], reverse=True))[0:6])

# key words of the articles
def key_words(text):
    keySet.clear()
    for kw in text:
        keySet.add(kw)

    print(keySet)  # dict#extra
    print('********5')#extra
    return(keySet)

#Find most relevant” articles Two texts are relevant if the 6 mostly
#used words in each overlap at least for 3 words
def relevont_articles(text_list,text_set,title):
      relevont_histogram = {
            }
      r_articles=[ ]
      j=0
      for kl in text_list:
          relevont_histogram[title[j]]=0
          for ks in kl:
              if ks in text_set:
                 relevont_histogram[title[j]]=relevont_histogram[title[j]]+1
          j=j+1
      RA=dict(list(sorted(relevont_histogram.items(), key=lambda kv: kv[1], reverse=True))[0:3])
      k=0
      for y in RA:
          if RA[y]>=3:
              print(y)
              r_articles.append(y)
              k=k+1
          elif k == 0:
              print('No related article found')
      return r_articles


# Articles files
# files name
fNname=["story1","sport1",'sport2','sport3','sport4','sport5','sport5','sport7']
n=len(fNname)
fedit=[None]*n
keySet=set()
keyList=[None]*n

i=0
while i < n:
    F=str(fNname[i])+".txt"
    #print(F) #extra 'title of articles
    fOpen=open(F, 'r',errors='ignore')
    #print(fOpen.readable()) #extra
    fread=fOpen.read()
    fread=fread.lower()
    #print(fread) #extra
    fedit[i]=iwords(fread)
    word_list = fedit[i].split(" ") #Split the paragraph into words
    #print(word_list) #extra
    whist=histogram(word_list)  # wlist fun.
    kwords=key_words(whist).copy()
    keyList[i]=kwords
    i=i+1

print(keyList) #extra
print(fedit)   #extra

enter = 1
while enter:
    article=str(input('Enter your Article: ')).lower()
    print('\n')
    #article=str(article).lower()
    aedit=iwords(article)
    #print(aedit)#extra
    word_list = aedit.split(" ")
    #print(word_list)#extra
    ahist = histogram(word_list)
    #print(ahist)#extra
    akeys=key_words(ahist).copy()
    #print(akeys)#extra
    arelevent=relevont_articles(keyList,akeys,fNname)
    print(arelevent)#extra
    enter=0
