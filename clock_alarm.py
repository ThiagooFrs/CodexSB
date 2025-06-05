import datetime
import time
from playsound import playsound
from colorama import init, Fore, Style

init(autoreset=True)


def get_alarm_time():
    while True:
        alarm_input = input('Defina o alarme (HH:MM): ')
        try:
            alarm_time = datetime.datetime.strptime(alarm_input, '%H:%M').time()
            return alarm_time
        except ValueError:
            print('Formato inválido. Use HH:MM.')


def clock_mode():
    alarm_time = get_alarm_time()
    print(f'Alarme definido para {alarm_time.strftime("%H:%M")}.')
    while True:
        now = datetime.datetime.now()
        current = now.strftime('%H:%M:%S')
        print(f'\r{Fore.CYAN}{current}{Style.RESET_ALL}', end='')
        if now.strftime('%H:%M') == alarm_time.strftime('%H:%M'):
            print(f"\n{Fore.RED}Alarme!{Style.RESET_ALL}")
            playsound('alarme.mp3')
            break
        time.sleep(1)


def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f'\r{Fore.CYAN}{timer}{Style.RESET_ALL}', end='')
        time.sleep(1)
        seconds -= 1
    print()


def pomodoro_mode():
    focus = 25 * 60
    pause = 5 * 60
    print(f'{Fore.YELLOW}Iniciando foco de 25 minutos...{Style.RESET_ALL}')
    countdown(focus)
    playsound('alarme.mp3')
    print(f'{Fore.GREEN}Hora do intervalo de 5 minutos!{Style.RESET_ALL}')
    countdown(pause)
    playsound('alarme.mp3')


def main():
    print('1 - Relógio com alarme')
    print('2 - Modo pomodoro')
    choice = input('Escolha o modo [1/2]: ')
    if choice == '2':
        pomodoro_mode()
    else:
        clock_mode()


if __name__ == '__main__':
    main()
