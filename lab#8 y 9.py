# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Ingresa una palabra :")
user_word = user_word.upper()

pal = ["A","E","I","O","U",]
for letter in user_word:
    if letter in pal :
        continue
    else:
     print(letter)

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Ingresa una palabra :")
user_word = user_word.upper()
word_without_vowels = ""
pal = ["A","E","I","O","U",]
for letter in user_word:
    if letter in pal :
        continue
    else:
     word_without_vowels = word_without_vowels  + letter  
        #print(letter)
print(word_without_vowels)
