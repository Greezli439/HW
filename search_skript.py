from models import Authors, Quotes
from db_connection import connect
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

COMMANDS = ['tag', 'name', 'exit']

command_completer = WordCompleter(COMMANDS)

def find_by_tags(tags):
    for tag in tags:
        data = Quotes.objects(tags=tag)
        for quote in data:
            print(quote.quote)



def find_by_name(name):
    author = Authors.objects(fullname=' '.join(name))
    data = Quotes.objects(author=author[0].id)
    for i in data:
        print(i.quote)


def get_command():
    command_with_args = prompt("chose name or tag to find data:  ", completer=command_completer).strip().split()
    return command_with_args[0], command_with_args[1:]

def main():
    while True:
        command, agrs = get_command()
        if command == 'exit':
            print('Good bye!')
            exit(0)
        elif command == 'name':
            find_by_name(agrs)
        elif command == 'tag':
            find_by_tags(agrs)


if __name__ == '__main__':
    main()
    search = input('chose name or tag to find data')
