# Task 1:
# Convert the "Hello, World!" string into a list of characters.
string = "Hello, World!"
char_list = list(string)    
print("1. Convert the 'Hello, World!' string into a list of characters.")
print("List of characters:", char_list)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Task 2:
# Convert the 'Python is easy to learn' sentence into a list of words.
sentence = "Python is easy to learn"
word_list = sentence.split()
print("2. Convert the 'Python is easy to learn' sentence into a list of words.")
print("List of words:", word_list)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# Task 3:
#Convert the ' ["I", "love", "Python"]' list into a single string.
words = ["I", "love", "Python"]
single_string = " ".join(words)
print('3. Convert the \'["I", "love", "Python"]\' list into a single string.')
print("Single string:", single_string)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# Task 4:
#Count the number of vowels in the given word 'education' using string and list methods only.
word = "education"
count = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')
print("4. Count the number of vowels in the given word 'education' using string and list methods only.")
print("Number of vowels in the word:", count)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# Task 5:
# Count the frequency of the word "python" in the given string 'python is easy and python is powerful' 
text = "python is easy and python is powerful"
word_to_count = "python"
frequency = text.count(word_to_count)
print("5. Count the frequency of the word 'python' in the given string 'python is easy and python is powerful'.")
print(f"The word '{word_to_count}' appears {frequency} times in the text.")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Task 6:
# Convert all names '["jyoti", "rahul", "sneha"] into Title Case using list methods.
names = ["jyoti", "rahul", "sneha"]
title_case_names = [name.title() for name in names]
print('6. Convert all names \'["jyoti", "rahul", "sneha"]\' into Title Case using list methods.')
print("Names in Title Case:", title_case_names)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Task 7:
# Create a list with 4 elements '["data", "science", "is", "fun"]', replace the second element, and convert the final list into a string.
items = ["data", "science", "is", "fun"]
items[1] = "analytics"
final_string = " ".join(items)
print('7. Create a list with 4 elements \'["data", "science", "is", "fun"]\', replace the second element, and convert the final list into a string.')
print("Final string:", final_string)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Task 8:
# Replace the word "Java" with "Python" and print the output as a string in this given string ' ["I", "love", "Java"]'.
languages = ["I", "love", "Java"]
languages[2] = "Python"
final_string = " ".join(languages)
print('8. Replace the word \'Java\' with \'Python\' and print the output as a string in this given string \'["I", "love", "Java"]\'.')
print("Final string:", final_string)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Task 9:
# Join the list elements using a comma ( , ) and print as a string '["Delhi", "Mumbai", "Chennai", "Kolkata"]'.
cities = ["Delhi", "Mumbai", "Chennai", "Kolkata"]
joined_string = ", ".join(cities)
print('9. Join the list elements using a comma ( , ) and print as a string \'["Delhi", "Mumbai", "Chennai", "Kolkata"]\'.')
print("Joined string:", joined_string)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Task 10:
# Write a Python program to reverse the given string "Python" by:
# a. Converting the string into a list of characters
# b. Reversing the list
# c. Converting the list back into a string
text = "Python"
print('10. Write a Python program to reverse the given string "Python" by:')
print("Text:", text)
char_list = list(text)
print("10(A). List of characters:", char_list)
char_list.reverse()
print("10(B). Reversed list of characters:", char_list)
reversed_string = "".join(char_list)
print("10(C). Reversed string:", reversed_string)
print("-----------------------------------------------------------------------------------")

