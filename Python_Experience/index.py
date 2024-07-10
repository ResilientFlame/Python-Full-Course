# 1.Multi brackets

# def validParenthes (text):
#     openingBrackets = ['[', '{', '(']
#     addedOpeningBracket = []
#     bracketKeys = {
#         ')': '(',
#         '}': '{',
#         ']': '['
#     }
#     for bracket in text: 
#         if bracket in openingBrackets:
#             addedOpeningBracket.append (bracket)
#         else:
#             if bracketKeys[bracket] == addedOpeningBracket[-1]:
#                 addedOpeningBracket.pop ()
#             else:
#                 return False
#     return len (addedOpeningBracket) == 0

# print (validParenthes ('[{(())}]'))

# 2.Rounded brackets

# def validParenthes (text):
#     openBrackets = []
#     for bracket in text:
#         if bracket == '(':
#             openBrackets.append (bracket)
#         else:
#             if len (openBrackets) > 0:
#                 openBrackets.pop ()
#             else:
#                 return False
#     return len (openBrackets) == 0
# print (validParenthes ('((()))'))