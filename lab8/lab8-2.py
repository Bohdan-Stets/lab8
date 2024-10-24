def words_without_a(text):
    words = text.split()
    return [word for word in words if 'а' not in word.lower()]

input_text = input("Введіть текстовий рядок: ")
result = words_without_a(input_text)
print("Слова, що не містять літери 'а':", result)
