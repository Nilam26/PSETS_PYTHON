#Write a python script that reads the first and last name of a person and concatenates them to form a full name. Also, write a script such that a space character is added post concatenation by detecting the casing of the strings.

first_name = input("Enter the first name \n")
last_name = input("Enter the first name \n")
last_name_concat = first_name+last_name

print("Printing full_name with concatanate operation :", last_name_concat)

print("full name of a person is using concatanation operation with space:",last_name_concat[0:len(first_name)],"",last_name_concat[len(first_name): len(last_name_concat)+1])



