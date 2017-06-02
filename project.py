from random import shuffle

def my_funct():
    my_list = []
    for i in range(text1):
        text = input("What is your %dst? " % (i + 1))
        my_list.append(text)
    shuffle(my_list)
    return my_list
text1 = int(input("How many do you want to choose between? "))

list_2 = my_funct()
print(list_2[0])
