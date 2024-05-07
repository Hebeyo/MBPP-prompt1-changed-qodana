def previous_palindrome(num):
    while True:
        num -= 1
        if str(num) == str(num)[::-1]:
            return num
