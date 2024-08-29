sentence = input("Введіть речення: ")

words = sentence.split()

if len(words) < 2:
    print("Введіть хоча б два слова")
else:
    longest_word = ""
    max_length = 0

    for word in words:
        if len(word) > max_length:
              longest_word = word
              max_length = len(word)

print("Найдовше слово:", longest_word,"\nЙого довжина:", max_length)