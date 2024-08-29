word1 = input("Введіть задане слово: ")
word2 = input("Запрпонуйте своє слово: ")

if word1.isalpha() and word2.isalpha():

    set1 = set(word1)
    set2 = set(word2)

    if set2.issubset(set1):
        print("Усі букви з другого слова є у першому слові.")
    else:
        print("Не всі букви з другого слова є у першому слові.")
else:
    print("Обидва слова мають містити лише літери.")




