#function to get user input
def get_user_input():
    return input("enter your word: ")


#function to check if the string is palindrome
def check_palindrome(user_input):
    user_input_rev = ''.join(reversed(user_input))
    if user_input == user_input_rev:
        print("your word is palindrome")
    else:
        print("your word is not palindrome")


#run the app
check_palindrome(get_user_input())