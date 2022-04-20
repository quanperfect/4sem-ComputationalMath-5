import functions
import graph
import lagrange as lagrange
import printer as printer
import computator

def work():
    printer.print_welcome()
    x0 = 0
    y0 = 0
    id = 0
    isGraphNeeded = 0
    isXYinputted = 0
    isHNinputted = 0

    while 1:
        inp = input()

        input_split = inp.split()

        if (len(input_split) == 2):

            if (isNumber(input_split[0]) and isNumber(input_split[1])):
                x0 = float(input_split[0])
                y0 = float(input_split[1])
                isXYinputted = 1
                if (isHNinputted):
                    print("X and Y inputted. You can now solve equation.")
                else:
                    print("X and Y inputted. Set h, n and then you can solve equation.")
            elif (input_split[0] == "solve" and input_split[1].isnumeric()):
                if (isXYinputted and isHNinputted):
                    equationId = int(input_split[1])
                    if (equationId >= 1 and equationId <= 2):
                        function = functions.getFunction(equationId)
                        points = computator.solve_equation(x0, y0, function, h, n)
                        graph.plot(equationId, points, isGraphNeeded)
                    else:
                        print("Wrong equation id. Type \"help\" for more information.")


                else:
                    if (not isXYinputted and  not isHNinputted):
                        print("You need to input x, y and set h, n. Type \"help\" for more information.")
                    elif (isXYinputted):
                        print("You need to set h, n. Type \"help\" for more information.")
                    else:
                        print("You need to input x, y. Type \"help\" for more information.")
            elif (input_split[0] == "graph" and input_split[1].isnumeric()):
                #graph with id
                id = int(input_split[1])
                if (id != 0):
                    isGraphNeeded = 1
                    print("You've selected to graph a function.")
                else:
                    isGraphNeeded = 0
                    print("You've selected NOT to graph a function.")

        elif (len(input_split) == 1):
            if (input_split[0] == "quit"):
                print("Me quit, okay...")
                exit(0)
            elif (input_split[0] == "help"):
                printer.print_help()
            else:
                print("Command does not exist.")
        elif (len(input_split) == 3):
            if (input_split[0] == "set" and isNumber(input_split[1]) and isNumber(input_split[2])):
                h = float(input_split[1])
                n = int(input_split[2])
                print("H and n inputted.")
                isHNinputted = 1


def isNumber(input: str):
    input = input.replace('.','',1)
    input = input.replace('-','',1)

    if (input.isnumeric()):
        return 1
    return 0
