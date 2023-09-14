FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ get the todos list in the file"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_list, filepath=FILEPATH):
    """write the todo list to the file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_list)


def add_todos(todo_new, filepath=FILEPATH):
    todos_local = get_todos(FILEPATH)
    todos_local.append(todo_new+"\n")
    write_todos(todos_local,FILEPATH)
    return todos_local


def delete_todo_byindex(index, filepath=FILEPATH):
    todos_local = get_todos(FILEPATH)
    print(todos_local)
    todos_local.pop(index)
    print(todos_local)
    write_todos(todos_local, FILEPATH)
    return todos_local

if __name__ == "__main__":
    todos = get_todos()
    print(todos)
    add_todos("250")
    delete_todo_byindex(0)
