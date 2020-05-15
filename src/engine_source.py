# -*- coding: utf-8 -*-


class Engine:
    
    def __init__(self, path, language):
        self.path = path
        self.lang = language

    def to_list(self):
        file = open(self.path, 'r', encoding='utf-8')
        all_text = file.readlines()
        self.final_list = [line.replace('\n', '') for line in all_text]

    def play(self):
        next_str = 0
        while True:

            if 'next' in self.final_list[next_str]:
                print(self.final_list[next_str].split(
                    '--')[1].split(' next')[0])
                next_str = int(self.final_list[next_str].split(' next ')[1])
                
            elif 'exit' in self.final_list[next_str]:
                print(self.final_list[next_str].split(
                    '--')[1].split(' exit')[0])
                if self.lang == 'ru':
                    print('Выход из игры...')
                    input('Нажмите ENTER для Выхода: ')
                    exit(1)
                    
                elif self.lang == 'en':
                    print('Exit the game...')
                    input('Press ENTER to Exit: ')
                    exit(1)
            else:
                print(self.final_list[next_str].split(
                    '--')[1].split(' if')[0])
                if self.lang == 'ru':
                    while True:
                        try:
                            choose = int(input('Выберите действие: ')) - 1
                            break
                        except:
                            print('ОШИБКА: Это не число!\n')
                elif self.lang == 'en':
                    while True:
                        try:
                            choose = int(input('Select the action: ')) - 1
                            break
                        except:
                            print('ERROR: This is not a number!\n')
                variants_list = self.final_list[next_str].split('if ')[
                    1].split(' ')
                next_str = int(variants_list[choose])
