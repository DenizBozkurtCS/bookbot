book_path = "books/frankenstein.txt"

with open(book_path) as f:
    file_contents = f.read()


def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count


def count_letters(text):
    text = text.lower()
    letter_count = {}
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    sorted_list = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    letters_only = []
    for i in range(len(sorted_list)):
        if sorted_list[i][0].isalpha():
            letters_only.append(sorted_list[i])
    return letters_only


def report(word_count, letter_count):
    report_string = f"--- Begin report of {book_path} ---\n"
    report_string += f"{word_count} words found in the document \n\n"
    for i in range(len(letter_count)):
        report_string += f"The '{letter_count[i][0]}' character was found {letter_count[i][1]} times\n"
    report_string += "--- End report ---"
    return report_string


word_count = count_words(file_contents)
letter_count = count_letters(file_contents)
report = report(word_count, letter_count)
print(report)
