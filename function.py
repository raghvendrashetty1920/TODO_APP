def get_todo():
    with open('todo.txt','r') as file_local:
        todos_local=file_local.readlines()
    return todos_local

def write_todo(todos_arg):
   with open('todo.txt','w') as file:
        file.writelines(todos_arg)