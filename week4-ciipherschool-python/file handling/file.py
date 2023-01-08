file = open("random.txt", "w")
print(file.write("blah blah blah"))
print(file.write("\n new line"))

print(file.write("Antra Gupta"))

a = ("soumya","Antra","anjali")
print(file.writelines(a))



with open("random.txt", "r")as file:
    print(file.read())
