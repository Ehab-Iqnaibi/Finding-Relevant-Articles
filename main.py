# irrelevant_words function
def iwords(text):
    irrelevant_words = {".", ",",  " \n ", " the ", " a ", " and ","\n",' how '," ",' be ',' as ',' could ',
                        " is ", " was ", " he ", " at ", " to ", " for ", " can ", " this ", " we ", " you "
                        ," or ", " i ", " an "," but ", " so ", " yes ", " no ", " of " , '!',' thought '}
    for iw in irrelevant_words:
        text = text.replace(iw, " ")
    print(500+i)
    print('-----------')


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
    print(600+i)            #extra
    print(word_histogram)
    return dict(list(sorted(word_histogram.items(), key=lambda kv: kv[1], reverse=True))[0:6])
#def relevont_articles(text):
    #    relevont_histogram = {

    #    }
    #      RW=0
    #     for Rlist in key_word:
    #         if word in Rlist:
    #           RW = RW+1
    #    if RW>=3
    #    relevont_histogram[relevont_histogram] = word_histogram[word] + 1

#  return dict(list(sorted(word_histogram.items(), key=lambda kv: kv[1], reverse=True))[0:6])


# Articles files
# files name
fNname=["story1","sport1",'sport2','sport3','sport4','sport5','sport5','sport7']
n=len(fNname)
fedit=[None]*n

i=0
while i < 1:
    F=str(fNname[i])+".txt"
    print(F) #extra
    fOpen=open(F, 'r',errors='ignore')
    print(fOpen.readable()) #extra
    fread=fOpen.read()
    fread=fread.lower()
    print(fread) #extra
    fedit[i]=iwords(fread)
    word_list = fedit[i].split(" ") #Split the paragraph into words
    print('*****')
    print(word_list) #extra
    whist=histogram(word_list)  # wlist fun.
    print(whist)
    print(400+i) #extra
    i=i+1


print(fedit) #extra


