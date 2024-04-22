
class ErrorPasswordEnter(Exception):
    pass

def file_read(file_name:str):
    
    try:
        file = open(file_name, 'a', encoding='utf-8')
        password = input(f'Введите пароль для изменения фала:\n')
        if password != '1q2w3e4r':
            raise ErrorPasswordEnter(f'Не верный пароль к файлу {file_name} \nперезайдите и проидите авторизацию с начало!')
        new_data = f"\n{input(f'Добавьте текст в файл:\n')}"
        file.write(new_data)
        
        file = open(file_name, 'r', encoding='utf-8')
        data = file.read()
        print(data)
        

    except FileNotFoundError:
        print(f'Файла с имянем {file_name} нет!!')
        file_name = input('Попробуйте другое имя файла: ')
        file_read(file_name)

    

    finally:
        if "file" in locals():
            file.close()

file_read(file_name = input('Введите имя файла: '))


    

