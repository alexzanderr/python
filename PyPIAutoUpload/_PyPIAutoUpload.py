

from PyPIAutoUpload.imports import *
from PyPIAutoUpload.history import *
from PyPIAutoUpload.upload import *
from PyPIAutoUpload.prepare import *


logger_PyPIAutoUpload = Loggerr(
    name="_PyPIAutoUpload.py",
    file_handler=file_handler_PyPIAutoUpload,
    stream_handler=stream_handler_PyPIAutoUpload
)

__appname__ = "PyPI Package Auto Upload"

logger_PyPIAutoUpload.info(f"application {__appname__} loaded.")

auto_prompt_message = f"""choose your package:
[<enter> ({enter_symbol}) activates {red_bold('manual')} mode]
{left_arrow_3_green_bold} """

manual_prompt_message = f"""[enter your {yellow_bold('package_folder')}] or [drag and drop]:
[<enter> ({enter_symbol}) activates {red_bold('auto')} mode]
{left_arrow_3_green_bold} """


def app_title():
    print_green_bold(__appname__)
    print_green_bold("=" * len(__appname__))
    print()


def exited_from_interrupt():
    print("\n")
    logger_PyPIAutoUpload.info(f"{yellow_bold(__appname__)}\napplication {red_bold('closed')} from [ {red_bold(KeyboardInterrupt.__name__)} ]")


def FailSafeSystem():
    _enter_ = green_bold("<enter>")
    _yes_ = green_bold("y")
    _no_ = red_bold("n")
    proceed = input(f"\nproceed to {yellow_bold('BUILD')}?\n[{_yes_}(es) and {_enter_} | {_no_}(o)]:\n{left_arrow_3_green_bold} ")
    if proceed != "y" and proceed != "":
        return False

    if proceed == "":
        proceed = input(f"\npress {_enter_} again to confirm\n[anything alse will {red_bold('cancel')} the build]\n[in case you pressed by mistake]:\n{left_arrow_3_green_bold} ")
        if proceed != "":
            return False

    return True


def PrintSelected(index):
    print(f"\npackage number [ {red_bold(index)} ] {yellow('selected')}:")
    print(f"\tname: {yellow(all_packages[index - 1].name)}")
    print(f"\tlocation: {cyan_underlined(all_packages[index - 1].folder)}")
    print(f"\tcustom-name: {green_underlined(all_packages[index - 1].custom_name)}")


def get_specs(index):
    # package name
    package_name = all_packages[index - 1].name
    # project folder path (where python file is located)
    package_folder = all_packages[index - 1].folder
    # package custom name
    package_custom_name = all_packages[index - 1].custom_name
    # tuple
    return package_name, package_folder, package_custom_name



def prompt_custom_name(original_name):
    e = green_bold("<enter>")
    y = green_bold("y")
    n = red_bold("n")
    choice = input(f"\ndo you want [{yellow_bold('custom_name')}] 4 your package?\n[{y}(es) and {e} | {n}(o)]:\n{left_arrow_3_green_bold} ")
    if choice != "y" and choice != "":
        return original_name

    while True:
        custom_name = input(f"\nenter [{yellow_bold('custom_name')}] 4 your package:\n{left_arrow_3_green_bold} ")
        if custom_name == "":
            print(f"custom name cant be [ {blue_bold('empty')} ]")
            print_yellow_bold('again')
            continue

        print(f"custom name: {yellow_bold(custom_name)}\n")

        choice = input(f"are you sure about this? [{y}(es) and {e} | {n}(o)]:\n{left_arrow_3_green_bold} ")
        if choice == "y" or choice == "":
            return custom_name


def SupressWarnings():
    e = green_bold("<enter>")
    y = green_bold("y")
    n = red_bold("n")
    choice = input(f"\nsupress warnings? [{y}(es) and {e} | {n}(o)]:\n{left_arrow_3_green_bold} ")
    if choice == "y" or choice == "":
        print(f"warnings are [ {yellow_bold('SUPRESSED')} ]")
        return True
    else:
        print(f"warnings are [ {red_bold('NOT')} {yellow_bold('SUPRESSED')} ]")
        return False


def Upload(
    package_name: str,
    package_folder: str,
    custom_name: str,
    __supress_warnings: bool
):
    # prepare package
    uploaded_package_folder, version = PreparePackage(
        package_name,
        package_folder,
        custom_name,
        __supress_warnings
    )
    if uploaded_package_folder == False and version == False:
        logger_PyPIAutoUpload.info(red_bold("upload canceled"))
        return

    # upload package
    UploadPackageToPyPI(
        package_name,
        uploaded_package_folder,
        version
    )



def PyPIAutoUpload():
    auto = True
    while True:
        try:
            clearscreen()
            app_title()

            # automatic mode
            if auto == True:
                PrintPackagesHistory()
                choice = input(auto_prompt_message)
                if choice == "":
                    auto = False
                    continue
                try:
                    choice = int(choice)
                except ValueError:
                    continue
                else:
                    if 1 <= choice <= len(all_packages):
                        PrintSelected(choice)
                        supress_warnings = SupressWarnings()

                        action = FailSafeSystem()
                        if action == False:
                            continue

                        # starting point in time
                        before = time.time()

                        package_name, package_folder, package_custom_name = get_specs(choice)

                        Upload(
                            package_name,
                            package_folder,
                            package_custom_name,
                            supress_warnings
                        )

                        duration = time.time() - before
                        duration = fixed_set_precision_str(duration, 2)
                        print(f"\nexecution time: [ {yellow_bold(duration)} ] second(s)\n")

                    else:
                        continue

            # manual mode
            else:
                auto = True
                package_folder = input(manual_prompt_message)
                if package_folder == "":
                    continue

                if not os.path.isdir(package_folder):
                    auto = False
                    continue

                # name
                package_name = os.path.basename(package_folder)
                package_custom_name = prompt_custom_name(package_name)

                print("\nyour package specs:")
                print(f"\tname: {yellow(package_name)}")
                print(f"\tlocation: {cyan_underlined(package_folder)}")
                print(f"\tcustom-name: {green_underlined(package_custom_name)}")

                supress_warnings = SupressWarnings()

                action = FailSafeSystem()
                if action == False:
                    continue

                del choice



                # starting point in time
                before = time.time()

                Upload(
                    package_name,
                    package_folder,
                    package_custom_name,
                    supress_warnings
                )


                duration = time.time() - before
                duration = fixed_set_precision_str(duration, 2)
                print(f"\nexecution time: [ {yellow_bold(duration)} ] second(s)")

                del duration

                # delete dist, build

                sleep(0.1)
                delete_folder_contents("uploaded", __print=True)


        except KeyboardInterrupt:
            exited_from_interrupt()
            break

        except Exception as exception:
            logger_PyPIAutoUpload.info(red_bold(exception) + "\n" + yellow_bold(type(exception)))
            logger_PyPIAutoUpload.exception(f"error in {logger_PyPIAutoUpload.name}")

            try:
                pauseprogram(f"{red_bold('error')} occured in function {PyPIAutoUpload.__name__}() [{yellow_bold('program paused')}]\n")

            except KeyboardInterrupt:
                exited_from_interrupt()
                break


        else:
            try:
                logger_PyPIAutoUpload.info(green_bold(f"no errors, {PyPIAutoUpload.__name__}() was successful"))
                pauseprogram()

            except KeyboardInterrupt:
                exited_from_interrupt()
                break



if __name__ == '__main__':
    PyPIAutoUpload()
