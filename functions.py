FUNCTIONS = 'todos.txt'


def get_todos(filepath= FUNCTIONS):
    """
    Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FUNCTIONS):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print('Hello')
    print(get_todos())
