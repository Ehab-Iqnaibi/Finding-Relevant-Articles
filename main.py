def words_histogram(text):
    # irrelevant_words function
    # remove irrelevant words, the, a, is, was,...
    irrelevant_words = {".", ",",  " \n ", " the ", " a ", " and ","\n",' how '," ",' be ',' as ',' could ',' are ',' its ',
                         " is ", " was ", " he ", " at ", " to ", " for ", " can ", " this ", " we ", " you ",' it '
                        ," or ", " i ", " an "," but ", " so ", " yes ", " no ", " of " , '!',' that ',' him ','"','--'}
    for iw in irrelevant_words:
        text = text.replace(iw, " ")
    # words_histogram
    word_list = text.split(" ")  # Split the paragraph into words
    word_histogram = {
       }
    # The number of repetitions of the word in the article
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

# key words of the articles
def key_words(text):
    keySet.clear()
    for kw in text:
        keySet.add(kw)

    return(keySet)

#Find most relevant” articles Two texts are relevant if the 6 mostly
#used words in each overlap at least for 3 words
def relevont_articles(text_list,text_set,title,article_no):
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
      k,o,l=0,0,1
      for y in RA:     #at least for 3 words
          if RA[y]>=3 and title[article_no]!= y :
              if o<1:
                    print('Related articles: ')
                    o=o+1
              print(str(l+k)+'. '+y)
              r_articles.append(y)
              k=k+1
      if k == 0:
          print('No related article found')
      return r_articles

# Titles
fName=["sport1",'Russian1','sport2','sport3','Curtain lifts on another historic Supreme','sport4','sport5','Biden2','sport6','sport7','Biden1',
       'Ukraine1','National Archives alerted lawyers','Russia2','Biden3','Human rights advocates from Russia','Saudi Arabia','Saudi Arabia1',
       'production','Lionel Messi','Ronaldo','John Mikel Obi','Adam Walker','Elon Musk','Elon Musk1','Elon Musk2','Elizabeth Holmes','Elizabeth Holmes1',
       'Theranos scandal','Covid','Covid infections']
n=len(fName)
keySet=set()
keyList=[None]*n
f,k=0,1
while f < n:
     fn = f + 1
     if k <4:
        print(str(fn)+'.'+fName[f],end=',     ')
        k=k+1
     else:
        print(str(fn)+'.'+fName[f])
        k=1
     f=f+1

i=0
while i < n:
    F=str(fName[i])+".txt"
    fOpen=open(F, 'r',errors='ignore')
    #print(fOpen.readable())
    fread=(fOpen.read()).lower()
    word_hist=words_histogram(fread)
    kwords=key_words(word_hist).copy()
    keyList[i]=kwords
    i=i+1

enter = 1
while enter:
    print('\n')
    article_number =int (input('Enter Article number: '))
    article_number=article_number-1
    print('The title of the article: '+fName[article_number])
    akeys=keyList[article_number]
    arelevent=relevont_articles(keyList,akeys,fName,article_number)
    user_input = input('Do you want to choose another Article (yes/no): ')
    if user_input.lower() == 'yes' :
            enter = 1
    elif user_input.lower() == 'no' :
            enter = 0


