import lab3


print("-----------------------")
words = "Would you like to change properties? "
words2 = "Would you like to add or to remove properties? "
answer = lab3.get_valid_input(words, ("yes", "no")).lower()
agent = lab3.Agent()
while True:
    if answer == "yes":
        answer_yes = lab3.get_valid_input(words2, ("add", "remove")).lower()
        if answer_yes == "add":
            agent.adding_property()
        else:
            agent.removing_property()
    else:
        break
print("The end of changes")