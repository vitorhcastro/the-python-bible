original = input("Write a sentence to be translated:\n").strip().lower()

words = original.split()

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                break
        new_word = word[vowel_pos:] + word[:vowel_pos] + "ay"
        new_words.append(new_word)

output = " ".join(new_words)
print(output)
