import lab3


print("-----------------------")
words = "Would you like to add new property and it's option"
answer = lab3.get_valid_input(words, ("yes", "no")).lower()
agent = lab3.Agent()
if answer == "yes":
    pass
else:
    pass