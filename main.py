# irrelevant_words function
def iwords(text):
    irrelevant_words = {".", ",",  " \n ", " the ", " a ", " and ","\n",' how '," ",' be ',' as ',' could ',' are ',
                        " is ", " was ", " he ", " at ", " to ", " for ", " can ", " this ", " we ", " you ",' it ','many'
                        ," or ", " i ", " an "," but ", " so ", " yes ", " no ", " of " , '!',' thought ',' that ',' him ',
                        ' its '}
    for iw in irrelevant_words:
        text = text.replace(iw, " ")
    #print('-----------1')

    return(text)

# The number of repetitions of the word in the article
def histogram(text):
    word_histogram = {

    }
    for word in word_list:
        if word not in word_histogram.keys():
            word_histogram[word] = 1
        else:
            word_histogram[word] = word_histogram[word] + 1

    try:
        word_histogram.pop("")
    except KeyError:
        pass
    #print('---------2')       #extra
    #print(word_histogram)
    return dict(list(sorted(word_histogram.items(), key=lambda kv: kv[1], reverse=True))[0:6])

# key words of the articles
def key_words(text):
    keySet.clear()
    for kw in text:
        keySet.add(kw)

    print(keySet)  # dict
    print('********5')
    return(keySet)

#Find most relevant” articles Two texts are relevant
def relevont_articles(text_list,text_set,title):
      relevont_histogram = {

        }
      j=0
      for kl in text_list:
          relevont_histogram[title[j]]=0
          for ks in kl:
              if ks in text_set:
                 relevont_histogram[title[j]]=relevont_histogram[title[j]]+1

          j=j+1

      return dict(list(sorted(relevont_histogram.items(), key=lambda kv: kv[1], reverse=True))[0:3])


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
    print(F) #extra 'title of articles
    fOpen=open(F, 'r',errors='ignore')
    #print(fOpen.readable()) #extra
    fread=fOpen.read()
    fread=fread.lower()
    #print(fread) #extra
    fedit[i]=iwords(fread)
    word_list = fedit[i].split(" ") #Split the paragraph into words
    #print(word_list) #extra
    whist=histogram(word_list)  # wlist fun.
    #print('********3')  # extra
    #print(whist)        # dict
    #print('********4')
    kwords=key_words(whist).copy()
    keyList[i]=kwords
    #    print(keyList[i])  # dict
    #    print('********6')
    i=i+1

print(keyList)
print(fedit) #extra

enter = 1
while enter:
    article=input('Enter your Article: ')
    print('\n')
    article=str(article).lower()
    aedit=iwords(article)
    aedit_list=aedit.split(" ")
    ahist = histogram(aedit_list)
    akeys=key_words(ahist).copy()
    #Find most relevant” articles Two texts are relevant if the 6 mostly
    #used words in each overlap at least for 3 words
    arelevent=relevont_articles(keyList,akeys,fNname)
    print(arelevent)
    enter=0
