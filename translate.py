
dictionary=[]
myfile=open('translate-data.txt','r')
data=myfile.read().split('\n')
for i in range (len(data)):
    detail=data[i].split('=')
    mydict={}
    dictionary.append({'english':detail[0], 'persian':detail[1]})
myfile.close()


for i in range (len(dictionary)):
    print(dictionary[i])


def show_menu():
    print('1_ add new word ')
    print('2_ translation english to persian')
    print('3_ translation persian to english')
    print('4_ exit')

def Add():
    english_word=input('enter english_word:')
    persian_word=input('enter persian_word:')
    dictionary.append({'english':english_word, 'persian':persian_word})

def translation_E_to_P():
    enterace= input('please enter your english words:')
    enterace=enterace.split(".")
    for i in range(len(enterace)):
        translate=enterace[i].split(' ')
        for j in range(len(translate)):
            for n in range(len(dictionary)):
                if translate[j]==dictionary[n]['english']:
                    print(dictionary[n]['persian'],end=' ')
        print('.',end='')                              
                

def translation_P_to_E():
    enterace= input('please enter your persian words:')
    enterace=enterace.split(".")
    for i in range(len(enterace)):
        translate=enterace[i].split(' ')
        for j in range(len(translate)):
            for n in range(len(dictionary)):
                if translate[j]==dictionary[n]['persian']:
                    print(dictionary[n]['english'],end=' ')
        print('.',end='')            


def Save():
    myfile=open('translate-data.txt','w')
    for i in range (len(dictionary)):
        myfile.write(dictionary[i]['english']+"="+dictionary[i]['persian'])
        myfile.write('\n')
    myfile.close()


show_menu()
choice= int(input('Please choose a number of menu:'))


while True:
    if choice==1:
        Add()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==2:
        translation_E_to_P()
        print()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==3:
        translation_P_to_E()
        print()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==4:
        Save()
        exit()        



 