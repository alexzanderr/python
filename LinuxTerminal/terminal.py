
# project
from LinuxTerminal.functionality import *
from core.json__ import *
from core.system import *

cwd = os.getcwd()

while 1:
    prompt_message = f"{username}{ATSIGN}{computer_name}:{tilda}{left_bracket_blue}{greenQuotationMark}{ConsoleColored(cwd, 'yellow', bold=1, underlined=1)}{greenQuotationMark}{right_bracket_blue} {arrows} "
    try:
        command = input(prompt_message).strip()
        del prompt_message

        if command == "":
            continue

        # math in terminal
        elif MathExpression__(command):
            ComputeMathExpression__(command)

        # funny error remix
        elif command == "errormix":
            PlayWindows98ErrorRemix__()

        # tree
        elif command == "tree":
            if is_folder_empty(cwd):
                print(ConsoleColored("\tfolder is empty", "cyan", bold=1))
            else:
                PrintTree__(cwd)

        # tree --help
        elif command == "tree --help":
            cyan_tree = ConsoleColored("tree", "cyan")
            print(bold_effect("\n\tbuilt-in function \"{}\".\n".format(cyan_tree)))

        # tree root\\folder1\\folder2\\...
        elif CheckTree__(command):
            PrintTree__(command)

        # size
        elif command == "size":
            cyan_size = ConsoleColored("tree", "cyan")
            print(bold_effect("\n\tbuilt-in function \"{}\".\n".format(cyan_size)))
            print(ConsoleColored("4 more information type: \"size --help\"\n", "yellow"))

        # size help
        elif command == "size --help":
            print("\n\twith this function you can print the size in bytes for a folder or an absolute path.\n")
            print("usage:")
            print(ConsoleColored("\tsize root\\folder1\\folder2\\end_folder", "yellow"))
            print(ConsoleColored("\t\tor", "red"))
            print(ConsoleColored("\tsize root\\folder1\\folder2\\file.extension\n", "yellow"))

        # size in bytes function
        elif SizeBuiltIn(command):
            param = command.split()[1]
            dimension = get_size_in_bytes(param)
            short = get_size_on_disk(dimension)
            computation = "\n\t{} {}".format(short.size, short.units)
            print(ConsoleColored(computation, "yellow", bold=True))

        # reset-history
        elif command == "reset-history":
            prompt_message = ConsoleColored("\tare you sure you want to delete history of commands?", "yellow", bold=1)
            prompt_message += "\t({}) or ({}) ?\n".format(ConsoleColored("(y)es", "red", bold=1), ConsoleColored("(n)o", "green", bold=1))

            decision = input(prompt_message)
            if decision == "y":
                CommandsHistoryJSON.clear()
                write_json_to_file({}, commands_json_path)

        # quick description
        elif command == "description":
            print('\n\tThis is a custom linux type terminal built by Andrew Alexzander.\n')

        # cowsay presentation
        elif command == 'cowsay':
            print(ConsoleColored(cowsay, "random"), '\n')
            print(">> Hello young and passionate individual!")
            print(">> Im a virtual and very popular linux cow used for printing stuff on the screen.")
            print(">> To use me you have to say 'cowsay ${your message}'\n")

        # cowsay message
        elif command.startswith('cowsay'):
            items = command.split()
            if len(items) >= 2:
                message = " ".join(items[1 : len(items)])
                print(Cowsay(message), '\n')

        # terminal icon
        elif command == 'icon':
            print(icon, '\n')

        # ubuntu ascii
        elif command == 'ubuntu':
            print(ubuntu, '\n')

        # kali linux dragon
        elif command == 'dragonfire':
            print(kali_linux_dragon, '\n')

        # terminal icon colored
        elif command.startswith('icon'):
            items = command.split()
            if len(items) == 2:
                PrintColored(icon, items[1])

        # ubuntu ascii colored
        elif command.startswith('ubuntu'):
            items = command.split()
            if len(items) == 2:
                PrintColored(ubuntu, items[1])

        # kali linux dragon colored
        elif command.startswith('dragonfire'):
            items = command.split()
            if len(items) == 2:
                PrintColored(kali_linux_dragon, items[1])

        # ls or dir
        elif command == 'ls' or command == 'dir':
            ListDirectory__(cwd)

        # clearing the screen
        elif command == 'cls' or command == 'clear':
            clearscreen()

        # delete file or folder
        elif command.startswith("delete"):
            DeleteFunction__(command, cwd)

        # mkfile, creates a file
        elif command.startswith("mkfile"):
            items = command.split()

            # actual function in action
            if len(items) >= 2:
                MakeFile__(cwd, items)

            # help mode
            elif len(items) == 1:
                MakeFile__(__help=1)

        # mkdir
        elif command.startswith("mkdir"):
            items = command.split()

            # actual function in action
            if len(items) == 2:
                MakeDir__(cwd, items)

            # help mode
            elif len(items) == 1:
                MakeDir__(__help=1)

        # starts with cd
        elif command.startswith('cd'):
            if command == "cd":
                continue

            items = command.split()
            new_directory = ChangeDirectory__(cwd, items, command)
            if new_directory:
                cwd = new_directory
            del new_directory

        # current working directory
        elif command == 'pwd' or command == 'path':
            print('\n\t' + ConsoleColored(cwd, "cyan", bold=1, underlined=1) + "\n")

        # python
        elif command == "python":
            print(yellow)
            os.system(command)
            print(endc_effect)

        # exit
        elif command == 'exit' or \
                command == "EXIT" or \
                command == "close" or \
                command == "shutdown":
            # playaudio(SystemSounds["shutdown-windows98"])
            exit(0)

        # prints history of commands
        elif command == 'history':
            print()
            for com in CommandsHistoryJSON:
                print('\t' + com)
            print()

        # time
        elif command == 'time':
            PrintTime__(Datetime__())

        # timelive
        elif command == "timelive":
            print()
            while 1:
                PrintTime__(Datetime__(), loop=1)
                print(end="\r")
                sleep(1)

        # date
        elif command == 'date':
            PrintDate__(Datetime__())

        # datetime
        elif command == 'datetime':
            PrintDatetime__(Datetime__())

        # pc name
        elif command == 'pc':
            print("\n\t" + ConsoleColored('ASUS-ROG-GL553VD\n', 'red', bold=1, underlined=1))

        # help function
        elif command == "help":
            pretty_print(CommandsHistoryJSON)
            print()

        # nothing from above
        else:
            if command != '':
                if command.isdigit() or command.isnumeric() or command.isdecimal():
                    print("\t" + ConsoleColored(command, "random", bold=1, underlined=1))
                else:
                    from threading import Thread
                    thread = Thread(target=command_is_invalid, args=())
                    thread.start()

                    print()
                    os.system(command)
                    print()

        UpdateCommandsHistory(command)
    # interrupting manually other while loops in this script
    except KeyboardInterrupt:
        print(ConsoleColored("\n\n\tcurrent thread was keyboard interrupted.", "cyan", bold=1))
        print(ConsoleColored("\tterminal restored.\n", "cyan", bold=1))