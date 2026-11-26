# # # # # # # # # # # # name = input("Enter your name: ")
# # # # # # # # # # # # print("Your name is:", name)
# # # # # # # # # # # text = input("Enter a string: ")
# # # # # # # # # # # length = len(text)
# # # # # # # # # # # print("Length of the string:", length)
# # # # # # # # # # text = input("Enter a string: ")
# # # # # # # # # # print("First character:", text[0])
# # # # # # # # # # print("Last character:", text[-1])
# # # # # # # # # text = input("Enter a string: ")
# # # # # # # # # start = int(input("Enter starting index: "))
# # # # # # # # # end = int(input("Enter ending index: "))
# # # # # # # # # print("Extracted string:", text[start:end])
# # # # # # # # text = input("Enter a string: ")
# # # # # # # # reverse = text[::-1]
# # # # # # # # print("Reversed string:", reverse)
# # # # # # # first = input("Enter first string: ")
# # # # # # # second = input("Enter second string: ")
# # # # # # # result = first + " " + second
# # # # # # # print("Combined string:", result)
# # # # # # text = input("Enter a string: ")
# # # # # # print("Repeated string:", text * 5)
# # # # # word = input("Enter a word: ")
# # # # # if word.lower() == word.lower()[::-1]:
# # # # #     print("Palindrome")
# # # # # else:
# # # # #     print("Not a palindrome")
# # # # text = input("Enter a string: ")
# # # # print("First character:", text[0])
# # # # print("Second character:", text[1])
# # # # print("Last character:", text[-1])
# # # # print("Second last character:", text[-2])
# # # text = input("Enter a string: ")
# # # print("Original string:", text)
# # # new_text = "J" + text[1:]
# # # print("Updated string:", new_text)
# # text = input("Enter a string: ")

# # vowels = 0
# # consonants = 0

# # for ch in text:
# #     if ch.isalpha():
# #         if ch.lower() in "aeiou":
# #             vowels += 1
# #         else:
# #             consonants += 1

# # print("Vowels:", vowels)
# # print("Consonants:", consonants)
# text = input("Enter a string: ")

# uppercase = 0
# lowercase = 0
# digits = 0
# special = 0

# for ch in text:
#     if ch.isupper():
#         uppercase += 1
#     elif ch.islower():
#         lowercase += 1
#     elif ch.isdigit():
#         digits += 1
#     else:
#         special += 1

# print("Uppercase letters:", uppercase)
# print("Lowercase letters:", lowercase)
# print("Digits:", digits)
# print("Special characters:", special)