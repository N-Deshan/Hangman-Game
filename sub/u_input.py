
import random

# importing the function

def beginning():
    "This function is to take the user name and the random word"
    user_input=' '
    user_name=''
    global word
    word=' '
    
    
    word=word_list[random.randrange(20)]
    



def middle(info_list, error_list, length_list):
    info_list.append(word)
    length_list.append(len(word))
    "This function is to display the word and guess the choices"
    allowed_errors=len(word)
    my_list=[]
    letter=''
    print("_ " * len(word))
    print()
    
    
    for count in range (len(word.upper())):
        my_list.append("_")
    print("Hint :",hint_list[word_list.index(word)])
    print()


    while allowed_errors != 0:

        if (''.join(my_list)) == word:
            print("You found the word!!!Hooray")
            print("The word was :","*",word.upper(),"*")
            break
 
        print("number of errors remaining",allowed_errors)
        letter=str(input("Guess : "))
        letter=letter.lower()
        print()
        if letter in word:
            
            for x in range(len(word)):
                if word[x]==letter:
                    my_list[x]=letter
                    
            for i in my_list:
                print(i.upper(),end=" ")
            print("\n")
        else:
            for i in my_list:
                print(i.upper(),end=" ")
            print("\n")
            allowed_errors -= 1
    error_list.append(len(word)-allowed_errors)
    

    return allowed_errors, word, hint_list, info_list, error_list, length_list
    
        
    
    
            

word_list=['laptop','mouse','keyboard','memory','monitor',
           'school','tablet','smartphone','speakers','banana',
           'charger','book','chair','router','desk',
           'umbrella','shoes','ups','teacher','dictionary']

hint_list=['A Device which is portable and large in size.',
           'Small, connected with a USB and can control the computer.',
           'Used to type something.',
           'The main component of the CPU.',
           'Can be used to get the computer output',
           'A place where childrens most visit.',
           'a handheld electronic device.',
           'Popular among everyone and most used device.',
           'We can hear the sounds.',
           'A yellow colour fruit.',
           'Used to power up the smart devices.',
           'Used as a backup in studying purposes.',
           'Helps to get comfortable.',
           'A device which helps to connect to internet',
           'Helps to hold or keep something.',
           'Helps when rainy days.',
           'Can prevent from the damages caused to foot.',
           'Used as a backup power supply to the computer.',
           'Person who helps to do our studies.',
           'The resource which can be used to find unknown or difficult words']





