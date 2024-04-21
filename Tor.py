import argparse
import time

def start_interface():
    print("Запуск интерфейса...")
    time.gmtime(1.5)
    print("иди нах")
def main():
    parser = argparse.ArgumentParser(description='Описание вашей программы')
    subparsers = parser.add_subparsers(help='Доступные подкоманды')

    # Подкоманда для интерфейса
    parser_start = subparsers.add_parser('start', help='Запуск интерфейса')
    parser_start.set_defaults(command='start')

    args = parser.parse_args()

    if hasattr(args, 'command'):
        if args.command == 'start':
            start_interface()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
