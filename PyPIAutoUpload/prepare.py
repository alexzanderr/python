
import pigar


from PyPIAutoUpload.imports import *


logger_Prepare = Loggerr(
    name="prepare.py",
    file_handler=file_handler_PyPIAutoUpload,
    stream_handler=stream_handler_PyPIAutoUpload
)

pigar_command_template = Template(
    "pigar -p ${requirements_file} -P ${project_folder}"
)

def get_latest_version(version_path):
    """ gets the latest version from
        PyPI_Autoupload/versions/<package_name>_versions.json
    """
    sep = get_path_sep(version_path)
    folder = sep.join(version_path.split(sep)[:-1])
    if not exists(folder):
        os.makedirs(folder)

    if not exists(version_path):
        write_json_to_file(["0.0.1"], version_path)
        return "0.0.1"
    else:
        versions_json = read_json_from_file(version_path)
        v = versions_json[-1]
        if "." in v:
            x, y, z = v.split(".")
            z = int(z)
            z += 1
            if z == 10:
                y = int(y)
                y += 1
                if y == 10:
                    x = int(x) + 1
                    y = "0"
                else:
                    z = "0"
            else:
                z = str(z)

            x, y, z = str(x), str(y), str(z)

            latest_version = ".".join((x, y, z))
            versions_json.append(latest_version)
            write_json_to_file(versions_json, version_path)

            return latest_version

        return "0.0.1"


def check_readme_md(inside_package: str):
    for __item in os.listdir(inside_package):
        if __item.lower() == "readme.md":
            return os.path.join(inside_package, __item)
    return False


def check_install_requirements(inside_package: str):
    for __item in os.listdir(inside_package):
        if __item.lower() == "requirements.txt":
            return inside_package + "/" + __item
    return False


def extract_requirements(requirements_path: str):
    requirements_lines = open(requirements_path, "r+").readlines()

    requirements_list = []
    for rline in requirements_lines:
        if "==" in rline:
            requirements_list.append(rline.split("==")[0].strip())
        elif "@" in rline:
            requirements_list.append(rline.split("@")[0].strip())
    return requirements_list


def generate_setup_py(setup_py_txt: str, setup_credentials: dict,
                      requirements_list: list):
    requirements_str = ""
    for i, r in enumerate(requirements_list, start=1):
        if i == len(requirements_list):
            requirements_str += "\t\t\"{}\"".format(r)
        elif i == 1:
            requirements_str += "\"{}\",\n".format(r)
        else:
            requirements_str += "\t\t\"{}\",\n".format(r)

    setup_py_unformatted = open(setup_py_txt, "r+").read()

    setup_py = setup_py_unformatted.format(
        package_name=setup_credentials["name"],
        package_version=setup_credentials["version"],
        package_author=setup_credentials["author"],
        package_author_email=setup_credentials["author_email"],
        package_description=setup_credentials["description"],
        package_requirements=requirements_str
    )

    return setup_py


def generate_license(uploads_folder: str, inside_package: str):
    lic = inside_package + "/LICENSE"
    if exists(lic):
        copy_content(lic, uploads_folder + "/LICENSE")
    else:
        with open(uploads_folder + "/LICENSE", "w+", encoding="utf-8") as f:
            lic = choice(os.listdir(os.getcwd() + "/LICENSES")) # random license
            lic = open("LICENSES/" + lic, "r+", encoding="utf-8").read()
            f.write(lic)
    return True


def PreparePackage(
    package_name: str,
    package_folder: str,
    custom_name: str,
    __supress_warnings: bool
):

    tr = tree_representation(package_folder)
    print(tr)
    logger_Prepare.info(f"this is the tree representation of your package:\n{yellow_bold(package_folder)}")

    # the path for this package but located in PyPIAutoUpload
    uploaded_package_folder = os.path.join(os.getcwd(), "uploaded", f"package_{package_name}")
    logger_Prepare.info(f"uploaded package folder:\n{yellow_bold(uploaded_package_folder)}")

    if not os.path.exists(uploaded_package_folder):
        os.makedirs(uploaded_package_folder)
        logger_Prepare.info(f"made dirs:\n{uploaded_package_folder}")
    else:
        logger_Prepare.info(f"deleting... contents from:\n{uploaded_package_folder}")
        delete_folder_contents(uploaded_package_folder, __print=True)
        logger_Prepare.info(f"DELETED contents from:\n{uploaded_package_folder}")


    inside_package = os.path.join(uploaded_package_folder, package_name)
    logger_Prepare.info(f"inside package folder:\n{inside_package}")

    if not os.path.exists(inside_package):
        os.makedirs(inside_package)
        logger_Prepare.info(f"made dirs:\n{inside_package}")
    else:
        logger_Prepare.info(f"deleting... contents from:\n{inside_package}")
        delete_folder_contents(inside_package, __print=True)
        logger_Prepare.info(f"\nDELETED contents from:\n{inside_package}")


    copy_content(package_folder, inside_package, __print=True)
    logger_Prepare.info(f"content copied from:\n{package_folder}\nto\n{inside_package}")

    tests = os.path.join(uploaded_package_folder, "tests")
    if not os.path.exists(tests):
        os.makedirs(tests)
    else:
        delete_folder_contents(tests, __print=True)


    readme_md_path = check_readme_md(inside_package)
    if readme_md_path:
        # copying existing readme to uploaded folder
        copy_content(readme_md_path, os.path.join(uploaded_package_folder, "README.md"))
    else:
        # creating the readme for the first time
        with open(os.path.join(uploaded_package_folder, "README.md"), "w+", encoding="utf-8") as f:
            f.write("### package {}\n".format(package_name))
            f.write("```\n")
            f.write("there is no description available for this package\n")
            f.write("sorry for the inconvenience\n")
            f.write("```\n")


    if not os.path.exists(pypirc_path):
        os.makedirs(os.path.dirname(pypirc_path))
        with open(pypirc_path, "w+", encoding="utf-8") as f:
            f.write("[pypi]\n")
            f.write("  username = __token__\n")
            with open("api-token", "r+", encoding="utf-8") as token:
                f.write("  password = {}".format(token.read()))
    else:
        # check if they are correct
        with open(pypirc_path, "r+", encoding="utf-8") as f:
            password = re.match("password = [\w\-\d_]+", f.read())
            with open("api-token", "r+", encoding="utf-8") as ff:
                api_token = ff.read()
                if password != api_token:
                    with open(pypirc_path, "w+", encoding="utf-8") as fff:
                        fff.truncate(0)
                        fff.write("[pypi]\n")
                        fff.write("  username = __token__\n")
                        fff.write(f"  password = {api_token}")


    with open(os.path.join(uploaded_package_folder, "MANIFEST.in"), "w+", encoding="utf-8") as f:
        f.write("recursive-include {} *.json *.wav *.txt *.md".format(package_name))


    latest_version = get_latest_version(os.path.join("versions", f"{package_name}_versions.json"))


    uploaded_requirements = os.path.join(
        uploaded_package_folder,
        "requirements.txt"
    )

    requirements_path = check_install_requirements(inside_package)
    if requirements_path:
        copy_content(
            requirements_path,
            uploaded_requirements,
            __print=True
        )

        requirements_list = extract_requirements(requirements_path)
    else:
        # generate with pigar
        logger_Prepare.info(yellow_bold("calling `pigar` tool to generate requirements for this package"))
        pigar_command = pigar_command_template.safe_substitute(
            requirements_file=uploaded_requirements,
            project_folder=package_folder
        )
        logger_Prepare.info("executing command:\n" + green(pigar_command))
        os.system(pigar_command)

        requirements_list = extract_requirements(uploaded_requirements)


    # name and email
    author_credentials_json = read_json_from_file(author_credentials_json_path)

    if custom_name:
        pkg_name = custom_name
    else:
        pkg_name = package_name

    setup_credentials = {
        "name": pkg_name,
        "version": latest_version,
        "author": author_credentials_json["name"],
        "author_email": author_credentials_json["email"],
        "description": "quick description",
    }

    setup_py = generate_setup_py(
        "setup.py.txt",
        setup_credentials,
        requirements_list
    )
    with open(os.path.join(uploaded_package_folder, "setup.py"), "w+", encoding="utf-8") as f:
        f.write(setup_py)

    generate_license(uploaded_package_folder, inside_package)

    tr = tree_representation(uploaded_package_folder)
    print("\n" + tr)
    logger_Prepare.info("tree represenation of what will be uploaded on PyPI")

    if not __supress_warnings:
        e = green_bold("<enter>")
        y = green_bold("y")
        n = red_bold("n")
        choice = input(f"pypi-package: {blue_bold(p)}\nversion: {latest_version}\nproceed to package upload^ ? [{y}(es) and {e} | {n}(o)]:\n{left_arrow_3_green_bold} ")
        if choice == "y" or choice == "":
            return uploaded_package_folder, latest_version
        else:
            return False, False

    return uploaded_package_folder, latest_version



if __name__ == '__main__':
    p = r"D:\Alexzander__\programming\python\bitcoin"
    n = "bitcoin"
    custom = "python-bitcoin-test"
    try:
        PreparePackage(n, p, custom, False)
    except Exception as error:
        logger_Prepare.exception("here")
