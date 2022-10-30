#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open("Day 10, Files + Vanity Project 1/Mail Merge/Input/Names/invited_names.txt") as file:
    names = file.read().split("\n")
    
print(names)

with open("Day 10, Files + Vanity Project 1/Mail Merge/Input/Letters/starting_letter.txt") as file:
    letter = file.read()


for i in names:
    
    letterPer = letter.replace("[name]", i)
    
    filename = "letter_for_" + i
    
    with open("Day 10, Files + Vanity Project 1/Mail Merge/Output/ReadyToSend/" + filename, "w") as file:
        file.write(letterPer)
        
    