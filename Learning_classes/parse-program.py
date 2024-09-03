##extract desired string from a given string
str_var = input("input your string:")
temp_var = ""
for alpha in str_var:
    if alpha.isalpha() or alpha == " ":
        temp_var = temp_var + alpha

print(temp_var)
