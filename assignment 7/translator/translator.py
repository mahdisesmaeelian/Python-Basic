try:
    read_dict=open('words.txt', 'r')
    mywords = read_dict.read()
    words=[]  
    wordslist=mywords.split('\n')

    for i in range (0,len(wordslist),2):
        words.append({"english":wordslist[i], "persian":wordslist[i+1]})   

    read_dict.close()      
except:
    print('File not found!')

def translatetoenglish():
    sentence = input('Enter your sentence: ')
    persianword = sentence.split(' ')

    for i in range(len(persianword)):
        for j in range(len(words)):
            if words[j]['persian'] ==persianword[i]:
                print(words[j]['english'], end=' ')
                break
        else:
            print(persianword[i], end=' ')

def translatetopersian():
    sentence =input("Enter your sentence : ")
    enwords= sentence.split(' ')
    for i in range(len(enwords)):
        for j in range(len(words)):
            if words[j]['english'] ==enwords[i]:
                print(words[j]['persian'], end=' ')
                break
        else:
            print(enwords[i], end=' ')           


def AddNewWord():
    English=input("Enter an English word that you wanna add to doc: ")
    Persian=input("Enter it's translation:")
    words.append({'english': English,'persian': Persian})
    print('\nThis word successfully added to doc \n')
    open_dict = open('words.txt', 'a')
    open_dict.write('\n'+English)
    open_dict.write('\n'+Persian)
    open_dict.close()
 
while True:
    print("\n 1-add new word\n 2-translation english to persian\n 3- translation persian to english\n 4- exit")
    choice =input("Choose one of the options above: ") 

    if choice=='1':
        AddNewWord()

    elif choice=='2':
        translatetopersian()

    elif choice=='3':
        translatetoenglish()

    elif choice=='4':
        exit()
