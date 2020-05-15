# -*- coding: utf-8 -*-


from src.engine_source import Engine


language = ''


def choose_lang():
    global language
    
    file_with_lang = open('language.txt', 'r', encoding='utf-8')
    lang = file_with_lang.readline().split('= ')[1].split(' ')[0]
    
    if lang == 'en':
        language = 'en'

    elif lang == 'ru':
        language = 'ru'

    else:
        print('ERROR: Wrong Language in "language.txt"!')
        input('Press ENTER to Exit: ')
        exit(1)


def main():
    global language
    choose_lang()
    
    file_with_path = open('path.txt', 'r', encoding='utf-8')
    path = file_with_path.readline().strip()
    try:
        file = open(path, 'r', encoding='utf-8')
    except:
        if language == 'ru':
            print(f'ОШИБКА: Файла "{path.split("/")[1]}" нет в директории "{path.split("/")[0]}"')
            input('Нажмите ENTER для Выхода: ')
            exit(1)

        elif language == 'en':
            print(f'ERROR: The file "{path.split("/")[1]}" is not in the directory "{path.split("/")[0]}"')
            input('Press ENTER to Exit: ')
            exit(1)
    file.close()

    game = Engine(path, language)
    game.to_list()
    game.play()


if __name__ == '__main__':
    main()