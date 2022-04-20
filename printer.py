import functions

def print_welcome():
    print("/--------------------------\\")
    print("Adams method, differential equations solver.")
    print("Type \"help\" to get help, type \"quit\" to quit.")
    print_divider()
    return

def print_divider():
    print("--------------------------")


def print_help():
    print_divider()
    print(
        "USER MANUAL\n"
        "[x] [y]   -   set a starting point (x;y);\n"
        "set [h] [n]  -   set h (step) and n (count);\n"
        "graph [1/0]   -   show analytical graph (1) or not (0);\n"
        "solve [id]  -   solve equation with this id:")
    print_functions()
    print(
        "help   -   display this message;\n"
        "quit   -   quit")
    print_divider()

def print_functions():
    for i in range(1,3):
        print("   " + functions.function_to_string(i))
