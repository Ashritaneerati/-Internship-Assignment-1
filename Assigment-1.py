"""
Chandana Ashritha
22BTRCL036
CSE - AIML, Section A
juug22btech57756@gmail.com

"""

print("-------------------------------------------------------------------------------------------------------")

"""
1.  Create a Python script that takes a student's score (0-100) as input and prints their grade based on the following criteria:
    Above 90: "Grade: A"
    80 to 90: "Grade: B"
    70 to 79: "Grade: C"
    60 to 69: "Grade: D"
    Below 60: "Grade: F
"""

def calculate_grade(score):
    if score > 90:
        grade = "Grade: A"
    elif score >= 80:
        grade = "Grade: B"
    elif score >= 70:
        grade = "Grade: C"
    elif score >= 60:
        grade = "Grade: D"
    else:
        grade = "Grade: F"
    return grade

def main():
    try:
        score = float(input("Enter student's score (0-100): "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(grade)
        else:
            print("Invalid score. Score must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()

print("-------------------------------------------------------------------------------------------------------")

"""
2.  Create a Python program that applies a discount to a purchase based on the amount spent. The
    program asks for the total amount and applies the following discount rates:
    Spend over $500: 20% discount
    Spend $200 - $500: 10% discount
    Spend below $200: No discount
    The program should print the original amount, the discount applied, and the final amount after
    the discount.
"""

def apply_discount(amount):
    if amount > 500:
        discount_rate = 0.20
    elif 200 <= amount <= 500:
        discount_rate = 0.10
    else:
        discount_rate = 0
    
    discount = amount * discount_rate
    final_amount = amount - discount
    
    return discount, final_amount

def main():
    try:
        total_amount = float(input("Enter the total amount spent: $"))
        if total_amount >= 0:
            discount, final_amount = apply_discount(total_amount)
            print(f"Original amount: ${total_amount:.2f}")
            print(f"Discount applied: ${discount:.2f}")
            print(f"Final amount after discount: ${final_amount:.2f}")
        else:
            print("Invalid amount. Amount must be a positive number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()

print("-------------------------------------------------------------------------------------------------------")

"""
3.  Create a program that asks for the user's birth month and day and then tells them their zodiac
    sign. For simplicity, you can use the following date ranges:
    Aries: March 21 - April 19
    Taurus: April 20 - May 20
    Gemini: May 21 - June 20
    Cancer: June 21 - July 22
    Leo: July 23 - August 22
    Virgo: August 23 - September 22
    Libra: September 23 - October 22
    Scorpio: October 23 - November 21
    Sagittarius: November 22 - December 21
    Capricorn: December 22 - January 19
    Aquarius: January 20 - February 18
    Pisces: February 19 - March 20
    Make sure to handle invalid inputs gracefully.
"""

def find_zodiac_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    else:
        return "Invalid date"

def main():
    try:
        month = int(input("Enter your birth month (1-12): "))
        day = int(input("Enter your birth day (1-31): "))
        
        if 1 <= month <= 12 and 1 <= day <= 31:
            zodiac_sign = find_zodiac_sign(month, day)
            print("Your zodiac sign is:", zodiac_sign)
        else:
            print("Invalid input. Month should be between 1 and 12, and day should be between 1 and 31.")
    except ValueError:
        print("Invalid input. Please enter numeric values for month and day.")

if __name__ == "__main__":
    main()

print("-------------------------------------------------------------------------------------------------------")

"""
4.  Write a Python program to check the validity of a password entered by the user. The password
    is considered valid if it meets the following criteria:
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length of 6 characters.
    Maximum length of 16 characters.
    The program should print whether the password is valid or not based on these criteria.
"""

import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    
    if not re.search("[a-z]", password):
        return False
    
    if not re.search("[A-Z]", password):
        return False
    
    if not re.search("[0-9]", password):
        return False
    
    if not re.search("[$#@]", password):
        return False
    
    return True

def main():
    password = input("Enter your password: ")
    if is_valid_password(password):
        print("Valid password.")
    else:
        print("Invalid password.")

if __name__ == "__main__":
    main()

print("-------------------------------------------------------------------------------------------------------")

"""
5.  Implement a simple number guessing game. First, set a target number within a certain range
    (e.g., 1 to 100). Then, using a while loop, ask the user to guess the number. Provide feedback for
    each guess ("too high" or "too low"). The game ends when the user guesses the number
    correctly. Use a break statement to exit the loop once the correct number is guessed.
"""

import random

def number_guessing_game(min_num, max_num):
    target_number = random.randint(min_num, max_num)
    
    while True:
        guess = int(input(f"Guess the number between {min_num} and {max_num}: "))
        
        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the correct number.")
            break

def main():
    min_num = 1
    max_num = 100
    number_guessing_game(min_num, max_num)

if __name__ == "__main__":
    main()

print("-------------------------------------------------------------------------------------------------------")

"""
6.  Write a Python program that asks the user to enter a range (start and end numbers). Use a for
    loop to iterate through this range, and for each number, check if it is a prime number. If it is,
    print the number. Use the continue statement to skip non-prime numbers efficiently.
"""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    try:
        start = int(input("Enter the start number of the range: "))
        end = int(input("Enter the end number of the range: "))
        
        print("Prime numbers in the range:")
        for num in range(start, end + 1):
            if is_prime(num):
                print(num)
    except ValueError:
        print("Invalid input. Please enter numeric values for the range.")

if __name__ == "__main__":
    main()

print("-------------------------------------------------------------------------------------------------------")

"""
7.  Create a Python program that iterates through a list of numbers (you can define the list in the
    code) and calculates the sum of the numbers. However, if the program encounters a number
    that is negative, it should stop adding any further numbers (i.e., break out of the loop) and print
    the current sum up to that point.
"""

def calculate_sum(numbers):
    total_sum = 0
    for num in numbers:
        if num < 0:
            break
        total_sum += num
    return total_sum

def main():
    numbers = [10, 20, 30, -5, 40, 50]  
    total_sum = calculate_sum(numbers)
    print("Sum of numbers up to the first negative number:", total_sum)

if __name__ == "__main__":
    main()

print("-------------------------------------------------------------------------------------------------------")

"""
8.  Write a Python program to print the following patterns
 a.
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
"""
def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for i in range(rows - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    rows = 5  
    print_pattern(rows)

if __name__ == "__main__":
    main()

print("-------------------------------------------------------------------------------------------------------")

"""
 b.
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15 
    16 17 18 18 19 20 21
"""

def print_pattern(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

def main():
    rows = 6 
    print_pattern(rows)

if __name__ == "__main__":
    main()

print("-------------------------------------------------------------------------------------------------------")

"""
9.  Create a program that asks for two numbers and prints all the numbers between them that are
    ivisible by a third number asked from the user.
"""

def print_divisible_numbers(start, end, divisor):
    print(f"Numbers between {start} and {end} divisible by {divisor}:")
    for num in range(start, end + 1):
        if num % divisor == 0:
            print(num)

def main():
    try:
        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))
        divisor = int(input("Enter the divisor: "))
        
        if start <= end:
            print_divisible_numbers(start, end, divisor)
        else:
            print("Invalid input. End number should be greater than or equal to start number.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()

print("-------------------------------------------------------------------------------------------------------")

"""
10.     Write a recursive function named reverse_string that takes a string as input and returns
    its reverse. The function must use recursion to accomplish this task and should not use
    any loops or slicing ([::-1]).
    Example Usage:
    print(reverse_string("hello"))
    Expected Output:
    "olleh"
"""

def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))

print("-------------------------------------------------------------------------------------------------------")

"""
11. Create a function longest_word(sentence) that finds and returns the longest word in the
    given string sentence. If there are multiple words of the same length, return the first one
    encountered.
    Example: longest_word("I love programming") should return "programming"
"""

def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("I love programming"))

print("-------------------------------------------------------------------------------------------------------")

"""
12. Create a Python function named custom_sort that takes a list of tuples where each tuple
    contains a name and a score. The function should return a new list sorted by scores in
    descending order. If two tuples have the same score, they should be sorted
    alphabetically by name in ascending order. Test your function with a predefined list of
    tuples and print the sorted list.
    Sample Input: [('Alice', 88), ('Bob', 95), ('Charlie', 88), ('Dave', 95)]
    Sample Output: [('Bob', 95), ('Dave', 95), ('Alice', 88), ('Charlie', 88)]
"""

def custom_sort(scores):
    sorted_scores = sorted(scores, key=lambda x: (-x[1], x[0]))
    return sorted_scores

sample_input = [('Alice', 88), ('Bob', 95), ('Charlie', 88), ('Dave', 95)]
sorted_output = custom_sort(sample_input)
print(sorted_output)

print("-------------------------------------------------------------------------------------------------------")

"""
13. Develop a Python function named transform_string that takes a string and performs the
    following transformations: it capitalizes every other letter starting with the first character
    (ignoring non-letter characters for the alternation pattern), and it replaces spaces with
    hyphens (-). For example, hello world becomes HeLlO-WoRlD. After defining the
    function, ask the user for a string and print its transformation.
    Sample Input: hello world
    Sample Output: HeLlO-WoRlD
"""

def transform_string(s):
    transformed = ""
    capitalize = True
    for char in s:
        if char.isalpha():
            if capitalize:
                transformed += char.upper()
            else:
                transformed += char.lower()
            capitalize = not capitalize
        elif char.isspace():
            transformed += "-"
    return transformed

def main():
    user_input = input("Enter a string: ")
    result = transform_string(user_input)
    print("Transformed string:", result)

if __name__ == "__main__":
    main()

print("-------------------------------------------------------------------------------------------------------")

"""
14. Create a function named simulate_file_renaming that takes two parameters: a list of
    filenames (as strings) and a new name template (a string containing a placeholder for a
    number, e.g., image_##). The function should return a list of strings representing the
    new filenames where the placeholder is replaced by an incremental number, starting
    from 1 and formatted to have leading zeros if necessary, according to the placeholder's
    length. For instance, renaming ['a.jpg', 'b.jpg', 'c.jpg'] with the template photo_### would
    result in ['photo_001.jpg', 'photo_002.jpg', 'photo_003.jpg']. This exercise simulates the
    renaming process, so you should only return the renamed list without actually renaming
    any files.
    Sample Input: ['a.jpg', 'b.jpg', 'c.jpg'], photo_###
    Sample Output: ['photo_001.jpg', 'photo_002.jpg', 'photo_003.jpg']
"""

def simulate_file_renaming(filenames, template):
    renamed_files = []
    placeholder_length = template.count("#")
    for i, filename in enumerate(filenames, start=1):
        new_filename = template.replace("#" * placeholder_length, str(i).zfill(placeholder_length))
        renamed_files.append(new_filename)
    return renamed_files

filenames = ['a.jpg', 'b.jpg', 'c.jpg']
template = "photo_###"
result = simulate_file_renaming(filenames, template)
print(result)

print("-------------------------------------------------------------------------------------------------------")

"""
15. You are given a list of words. Write a Python function called group_anagrams that groups all
    anagrams together and returns them as a list of lists.
    Two words are considered anagrams if they contain the same characters but in a different order.
    Examples:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    Input: ["listen", "silent", "top", "pot", "hello", "world"]
    Output: [["listen", "silent"], ["top", "pot"], ["hello"], ["world"]]
"""

from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
output1 = group_anagrams(input1)
print(output1)

input2 = ["listen", "silent", "top", "pot", "hello", "world"]
output2 = group_anagrams(input2)
print(output2)

print("-------------------------------------------------------------------------------------------------------")

"""
16. You are given a list of integers. Write a Python function called max_subarray_sum to find the
    contiguous subarray within the list that has the largest sum and return that sum.
    For example, given the list [-2, 1, -3, 4, -1, 2, 1, 5, 4], the contiguous subarray with the largest
    sum is [4, -1, 2, 1], and the maximum sum is 6.
    Examples:
        Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        Output: 6 (corresponding to the subarray [4, -1, 2, 1])
        Input: [1, 2, 3, 4, 5]
        Output: 15 (corresponding to the subarray [1, 2, 3, 4, 5])
"""

def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    start_index = end_index = 0
    temp_start_index = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start_index = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_start_index
            end_index = i

    return max_sum, nums[start_index:end_index + 1]

input1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output1, subarray1 = max_subarray_sum(input1)
print("Output:", output1, "(corresponding to the subarray", subarray1, ")")

input2 = [1, 2, 3, 4, 5]
output2, subarray2 = max_subarray_sum(input2)
print("Output:", output2, "(corresponding to the subarray", subarray2, ")")

print("-------------------------------------------------------------------------------------------------------")

"""
17. Implement a function that performs a sequential search through a list for a specified target value.
    The function should return the index of the target if found, and -1 if the target is not in the list.
    Sample Input: ([5, 3, 7, 1, 9], 7)
    Sample Output: 2
"""

def sequential_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

input_list = [5, 3, 7, 1, 9]
target_value = 7
output = sequential_search(input_list, target_value)
print("Output:", output)

print("-------------------------------------------------------------------------------------------------------")

"""
18. Design a method to encode a list of strings to a single string and another method to decode it
    back to a list of strings.
    The encoded string should be concise and easily decodable. Assume there are no character
    restrictions for individual strings.
    Examples:

    19. Input: ["hello", "world"]
    Encoded Output: "5#hello5#world" (or another unique format of your choice)
    Decoded Output: ["hello", "world"]

    20. Input: ["abc", "def", "ghi"]
    Encoded Output: "3#abc3#def3#ghi"
    Decoded Output: ["abc", "def", "ghi"]
"""

def encode(strings):
    encoded_string = ""
    for string in strings:
        encoded_string += f"{len(string)}#{string}"
    return encoded_string

def decode(encoded_string):
    decoded_strings = []
    i = 0
    while i < len(encoded_string):
        delimiter_index = encoded_string.find("#", i)
        string_length = int(encoded_string[i:delimiter_index])
        string = encoded_string[delimiter_index + 1:delimiter_index + 1 + string_length]
        decoded_strings.append(string)
        i = delimiter_index + 1 + string_length
    return decoded_strings

# Test the functions
input1 = ["hello", "world"]
encoded_output1 = encode(input1)
decoded_output1 = decode(encoded_output1)
print("Encoded Output:", encoded_output1)
print("Decoded Output:", decoded_output1)

input2 = ["abc", "def", "ghi"]
encoded_output2 = encode(input2)
decoded_output2 = decode(encoded_output2)
print("Encoded Output:", encoded_output2)
print("Decoded Output:", decoded_output2)

print("-------------------------------------------------------------------------------------------------------")

