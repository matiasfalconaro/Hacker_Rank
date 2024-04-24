#!/usr/bin/python3

def lists_methods(N: int) -> None:
    """
    Execute a series of list operations based on user input commands.
    """
    commands = []
    result_list = []

    for i in range(N):
        action = input()
        command = action.split()
        commands.append(command)

    for command in commands:
        method = command[0]

        if method == 'insert':
            index = int(command[1])
            value = int(command[2])
            result_list.insert(index, value)

        elif method == 'print':
            print(result_list)

        elif method == 'remove':
            value = int(command[1])
            if value in result_list:
                result_list.remove(value)

        elif method == 'append':
            value = int(command[1])
            result_list.append(value)

        elif method == 'sort':
            result_list.sort()

        elif method == 'pop':
            if result_list:
                result_list.pop()

        elif method == 'reverse':
            result_list.reverse()

        # The print statement after each command execution is optional


if __name__ == '__main__':
    N = int(input())
    lists_methods(N)
