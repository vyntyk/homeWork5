# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in # Number of words: 10# out # авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
#
# in Number of words: 6 out  ваб вба абв ваб бва абв
# ваб вба ваб бва
# in Number of words: -1
# out The data is incorrect

with open('text.txt', 'r', encoding="utf-8") as data:
    str = data.read()
    if len(str) == 0:
        print("Number of words: -1\nThe data is incorrect")
    else:
        list = ' '.join(filter(lambda x: not 'абв' in x, str.split()))
        print("Number of words: ", len(list.strip().split(" ")))
        print(list)