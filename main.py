# irrelevant_words function
def words_histogram(text):
    irrelevant_words = {".", ",",  " \n ", " the ", " a ", " and ","\n",' how '," ",' be ',' as ',' could ',' are ',' its ',
                         " is ", " was ", " he ", " at ", " to ", " for ", " can ", " this ", " we ", " you ",' it ','many'
                        ," or ", " i ", " an "," but ", " so ", " yes ", " no ", " of " , '!',' thought ',' that ',' him '}
    for iw in irrelevant_words:
        text = text.replace(iw, " ")

    word_list = text.split(" ")  # Split the paragraph into words
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

    return dict(list(sorted(word_histogram.items(), key=lambda kv: kv[1], reverse=True))[0:6])

    #return(text)
# The number of repetitions of the word in the article

# key words of the articles
def key_words(text):
    keySet.clear()
    for kw in text:
        keySet.add(kw)

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
      for y in RA:     #at least for 3 words
          if RA[y]>=3:
              print(y)
              r_articles.append(y)
              k=k+1
      if k == 0:
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
    fOpen=open(F, 'r',errors='ignore')
    #print(fOpen.readable())
    fread=(fOpen.read()).lower()
    #fread=fread.lower()
    fedit[i]=iwords(fread)          #iwords fun.
    #word_list = fedit[i].split(" ") #Split the paragraph into words
    whist=histogram(word_list)      #histogram fun.
    kwords=key_words(whist).copy()
    keyList[i]=kwords
    i=i+1

print(fedit)   #extra
print(keyList) #extra

enter = 1
while enter:
    article=str(input('Enter your Article: ')).lower()
    print('\n')
    aedit=iwords(article)
    word_list = aedit.split(" ")
    #print(word_list)#extra
    ahist = histogram(word_list)
    #print(ahist)#extra
    akeys=key_words(ahist).copy()
    print(akeys) #extra
    arelevent=relevont_articles(keyList,akeys,fNname)
    #print(arelevent)  #extra
    user_input = input('Do you want enter another Article (yes/no): ')
    if user_input.lower() == 'yes' :
            enter = 1
    elif user_input.lower() == 'no' :
            enter = 0


