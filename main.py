"""
Multiplication Table
"""


def print_multiplication_table(times: int, rows: int):
    if times <= 0 or rows <= 0:
        print("Number and rows cannot be less than 1. \n")
        return

    else:
        i = 1
        while rows != 0:
            print(f"{i} * {times} = {i * times}")
            i = i+1
            rows = rows -1
        return

"""
Palindromes
"""


def is_palindrome(words: str) -> bool:
    words = words.lower()
    length = len(words)

# print (f"{length} words")
    while length != length / 2:
        a = 0
        if words[a] != words[length-1]:
            print(f" {words [a]}{ words[length-1]}")
            return False

        else:
            a = a + 1
            length = length - 1

    return True

"""
# Press the green button in the gutter to run the script.
"""
if __name__ == '__main__':
    text = input("Give me a palindrome. I will test it for you: ")
    is_palindrome(text)

    while True:
        times = int(input("Please tell me which number you want to be multiplied: "))
        rows = int(input("Please tell me how many times you want the first number multiplied: "))
        print_multiplication_table(times, rows)

# print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")
