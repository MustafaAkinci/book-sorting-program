import string
from copy import deepcopy

stopwords = open("stop_words_english.txt", "r",encoding="utf-8").read()
stopwords = stopwords.split("\n")
stopwords.append("")
def Concordance(Book, Word_Order):

#If the code doesn't work, make sure the .py files and stop_words_english.txt files are on the desktop.
#The code runs in 5 seconds like this, but when I embed the stop_word_english.txt file in it, this time increases to 1 minute, so I did not embed the stop_word_english.txt file into the program.
    text1 = open(Book, "r",encoding="utf-8").read()
    words = [i.lower().strip(string.punctuation) for j in text1.split("\n") for i in j.split(" ") if i.lower().strip(string.punctuation) not in stopwords]

    if Word_Order == 2:
        for i in range(1, len(words), 2):
            words[i - 1] = words[i - 1] + " " + words[i]

        x = 0
        for j in range(1, len(words), 2):
            words.pop(j - x)
            x += 1
    concordance = {}

    for wword in words:
        if wword in ["", " "]:
            continue
        # If the word is not in stop_words, we will take it to concordance.
        if wword not in stopwords:
            # If it's not in our concordance dictionary before.
            if wword not in concordance:
                # Our key word in our Concordance dictionary should be a list if value.
                concordance[wword] = 1
            else:
                # If it's already in our dictionary
                # We increase the number of repetitions for this word by one.
                concordance[wword] = concordance[wword] + 1
    return concordance

def Word_Order_Frequency_One_Book (Book, Word_Order, File_Output):

    concordance = Concordance(Book,Word_Order)

    concordance = {k: v for k, v in sorted(concordance.items(),reverse=True, key=lambda item: item[1])}

    output = open(File_Output,"w",encoding="utf-8")
    for wword in concordance:
        output.write(f"{concordance[wword]} | {wword}\n")

    output.close()

def Word_Order_Frequency_Two_Book (Book1, Book2, Word_Order, File_Output):
    concordance1 = Concordance(Book1,Word_Order)
    concordance2 = Concordance(Book2,Word_Order)

    # concordance1 = {k: v for k, v in sorted(concordance1.items(),reverse=True, key=lambda item: item[1])}
    # concordance2 = {k: v for k, v in sorted(concordance2.items(),reverse=True, key=lambda item: item[1])}

    output = open(File_Output,"w",encoding="utf-8")
    output.write("TOTAL | BOOK 1 | BOOK 2 | WORD |\n")
    output.write("--------------------------------\n")
    union = deepcopy(concordance1)
    for i in concordance2:
        try:
            union[i] = concordance2[i] + union[i]
        except KeyError:
            union[i] = concordance2[i]
            concordance1[i] = 0

    union = {k: v for k, v in sorted(union.items(),reverse=True, key=lambda item: item[1])}
    for i in union:
        try:
            output.write(f"{union[i]} | {concordance1[i]} | {concordance2[i]} | {i}\n")
        except:
            output.write(f"{union[i]} | {concordance1[i]} | {0} | {i}\n")


    output.close()
#typing 2 instead of 1 here prints binary word groups
Word_Order_Frequency_One_Book("book_1.txt",1,"text1_frequency.txt")
Word_Order_Frequency_Two_Book("book_1.txt","book_2.txt",1,"text2_frequency.txt")
