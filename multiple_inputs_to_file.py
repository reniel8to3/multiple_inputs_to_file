#Name: MALABO, RENIEL A.            #Section: BSCPE 1-5
#Subject: Object Oriented Programming
print ("This program is created to ask a user for a specific input and that input will be added to a text file.")
#def function
def line():   
#create empty function
    text_lines=[]
#ask user what to write
    while True:
        text_input=input('What is/are your favorite song/s?')
#add user input to text file
        text_lines.append(text_input)
#ask user if they want to add more or no
        more_text=input('Do you want to list more of your favorite songs? Please type yes if YES and no if NO. ')
        if more_text == "yes":
            continue
        elif more_text == "no":
            print ("Thank you for listing your favorite songs!")
            break
        else:
            print ("Invalid input.")
#create text file
    with open("mylife.txt", "w") as lines_file:
        lines_file.write("\n".join(text_lines))
line()