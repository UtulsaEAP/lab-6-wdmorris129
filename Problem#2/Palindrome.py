def check_palindrome(user_input):
    new_input = user_input[::-1]
    
    if new_input == user_input:
        print("palindrome: {a}".format(a = user_input))
    else:
        print("not a palindrome: {b}".format(b = user_input))





if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)


# def reverse(string):
#     string = string[::-1]
#     return string
 
# s = "Geeksforgeeks"
 
# print("The original string is : ", end="")
# print(s)
 
# print("The reversed string(using extended slice syntax) is : ", end="")
# print(reverse(s))