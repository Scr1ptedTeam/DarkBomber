import subprocess

from colorama import init, Fore

from colorama import Back

from colorama import Style



print(Fore.MAGENTA  + Style.BRIGHT +'''DarkBomber - Library Installer. 

///////////////////////////////////////////////

<| Установщик необходимых библиотек для DarkBomber

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

<| Когда это окно можно будет закрыть,

<Программа даст знать сама.

==============================================

''')
user_input = input("Введите 1 для установки, 0 для выхода: ")

if user_input == "1":

    subprocess.run(['pip', 'install', 'requests'])

    print(Fore.GREEN  + Style.BRIGHT + "Установка завершена!")
else:
  print(Fore.RED  + Style.BRIGHT +"Установка отменена.")
    
    



