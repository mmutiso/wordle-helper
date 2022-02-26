f = open("words_alpha.txt")

d = open("five_letter_words.txt", "w+")

for line in f.readlines():
    if len(line.strip()) == 5:
        d.write(line.strip() + "\n")

f.close()
d.close()
