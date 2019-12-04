
def reverseString(mesz):
    #splits messge in the form of list
    inputword = mesz.split(" ")
    #strat from last and steps having -1
    inputword = inputword[-1::-1]
    #join those list into string again
    output = ' '.join(inputword)
    return output


#input message from user
Message = input("Enter a String Here:\n")
print(reverseString(Message))

