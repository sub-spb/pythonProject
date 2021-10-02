# Шифр Цезаря
print('Программа шифровки / дешифровки текста по методу Цезаря')
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

language = input('Введите язык алфавита: русский (ru) или английский (en)')
text = input('Введите текст для шифрования / дешифрования')
k = int(input('Введите шаг сдвига для шифрования (k > 0) или дешифрования (k < 0) текста'))

if language == 'ru':
    lower_alphabet = rus_lower_alphabet
    upper_alphabet = rus_upper_alphabet
elif language == 'en':
    lower_alphabet = eng_lower_alphabet
    upper_alphabet = eng_upper_alphabet

