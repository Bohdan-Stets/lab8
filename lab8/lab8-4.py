def words_above_average_length(text):
    words = text.split()
    average_length = sum(len(word) for word in words) / len(words)
    return [word for word in words if len(word) > average_length]

input_text = input("Введіть текстовий рядок: ")
result = words_above_average_length(input_text)
print("Слова, кількість літер в яких більша за середню:", result)
