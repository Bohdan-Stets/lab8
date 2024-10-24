#Працює на введення англійської бувки X чи x
def contains_more_than_four_x(text):
    count_x = text.count('X') + text.count('x')
    return count_x > 4

input_text = input("Введіть текстовий рядок: ")
if contains_more_than_four_x(input_text):
    print("Рядок містить більше ніж чотири літери 'X' або 'x'.")
else:
    print("Рядок містить чотири або менше літер 'X' або 'x'.")
