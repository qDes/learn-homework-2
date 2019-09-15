"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding = 'utf-8') as file_read:
        text = file_read.read()
        print('Value of words in text:',len(text.split()))

    with open('referat2.txt', 'w', encoding='utf-8') as file_write:
        file_write.write(text.replace('.','!'))

if __name__ == "__main__":
    main()
