def words_with_max_r(text):
    words = text.split()
    max_r_count = 0
    result_words = []

    for word in words:
        r_count = word.upper().count('R')
        if r_count > max_r_count:
            max_r_count = r_count
            result_words = [word]
        elif r_count == max_r_count and r_count > 0:
            result_words.append(word)

    return result_words

input_text = input("Введіть текстовий рядок: ")
result = words_with_max_r(input_text)
print("Слова, що містять максимальну кількість літер 'R':", result)
