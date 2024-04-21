import argparse

parser = argparse.ArgumentParser(description='Описание вашей программы')
subparsers = parser.add_subparsers(help='Доступные подкоманды')

# Подкоманда 1
parser_cmd1 = subparsers.add_parser('cmd1', help='Описание команды 1')
parser_cmd1.add_argument('arg1', type=int, help='Описание аргумента для команды 1')
parser_cmd1.set_defaults(command='cmd1')

# Подкоманда 2
parser_cmd2 = subparsers.add_parser('cmd2', help='Описание команды 2')
parser_cmd2.add_argument('arg2', type=str, help='Описание аргумента для команды 2')
parser_cmd2.set_defaults(command='cmd2')

args = parser.parse_args()

if hasattr(args, 'command'):
    if args.command == 'cmd1':
        print("Вы вызвали команду 1 с аргументом:", args.arg1)
    elif args.command == 'cmd2':
        print("Вы вызвали команду 2 с аргументом:", args.arg2)
else:
    parser.print_help()
