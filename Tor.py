import argparse

def start_interface():
    print("Запуск интерфейса..")
def main():
    parser = argparse.ArgumentParser(description='Завтра может будет (:')
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
