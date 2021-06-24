

from Python2Executable.imports import *

logger_NSI = logging.getLogger("nsis.py")
logger_NSI.setLevel(logging.INFO)
logger_NSI.addHandler(file_handler_Python2Executable)
logger_NSI.addHandler(stream_handler_Python2Executable)

nsis_script_path_template = Template("nsis_scripts${sep}${project_name}.nsi")
nsis_script_path_template = Template(nsis_script_path_template.safe_substitute(sep=os.path.sep))


nsi_script_template = \
Template(r"""

!define APP_NAME "${project_name}"
!define COMP_NAME "${project_name}"
!define WEB_SITE "https://alexzander.tech"
!define VERSION "1.00.00.00"
!define COPYRIGHT "alexzander's software"
!define DESCRIPTION "${project_name} is made using python and this nsis script is generated from python"
!define INSTALLER_NAME "${remote_location}\install_${project_name}.exe"
!define MAIN_APP_EXE "${project_name}.exe"
!define INSTALL_TYPE "SetShellVarContext current"
!define REG_ROOT "HKCU"
!define REG_APP_PATH "Software\Microsoft\Windows\CurrentVersion\App Paths\${MAIN_APP_EXE}"
!define UNINSTALL_PATH "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"

!define REG_START_MENU "Start Menu Folder"

var SM_Folder

######################################################################


VIProductVersion  "${VERSION}"
VIAddVersionKey "ProductName"  "${APP_NAME}"
VIAddVersionKey "CompanyName"  "${COMP_NAME}"
VIAddVersionKey "LegalCopyright"  "${COPYRIGHT}"
VIAddVersionKey "FileDescription"  "${DESCRIPTION}"
VIAddVersionKey "FileVersion"  "${VERSION}"


######################################################################


SetCompressor ZLIB
Name "${APP_NAME}"
Caption "${APP_NAME}"
OutFile "${INSTALLER_NAME}"
BrandingText "${APP_NAME}"
XPStyle on
InstallDirRegKey "${REG_ROOT}" "${REG_APP_PATH}" ""
InstallDir "$PROGRAMFILES\${project_name}"


######################################################################


!include "MUI.nsh"

!define MUI_ABORTWARNING
!define MUI_UNABORTWARNING

!insertmacro MUI_PAGE_WELCOME

!ifdef LICENSE_TXT
!insertmacro MUI_PAGE_LICENSE "${LICENSE_TXT}"
!endif

!insertmacro MUI_PAGE_DIRECTORY

!ifdef REG_START_MENU
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "${project_name}"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${REG_ROOT}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${UNINSTALL_PATH}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${REG_START_MENU}"
!insertmacro MUI_PAGE_STARTMENU Application $SM_Folder
!endif

!insertmacro MUI_PAGE_INSTFILES

!define MUI_FINISHPAGE_RUN "$INSTDIR\${MAIN_APP_EXE}"
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM

!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "English"


######################################################################


Section -MainProgram
${INSTALL_TYPE}
SetOverwrite ifnewer
SetOutPath "$INSTDIR"
${project_files_paths_section}
SectionEnd


######################################################################


Section -Icons_Reg
SetOutPath "$INSTDIR"
WriteUninstaller "$INSTDIR\uninstall_${project_name}.exe"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
CreateDirectory "$SMPROGRAMS\$SM_Folder"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall_${project_name}.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!insertmacro MUI_STARTMENU_WRITE_END
!endif

!ifndef REG_START_MENU
CreateDirectory "$SMPROGRAMS\${project_name}"
CreateShortCut "$SMPROGRAMS\${project_name}\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\${project_name}\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall_${project_name}.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\${project_name}\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!endif

WriteRegStr ${REG_ROOT} "${REG_APP_PATH}" "" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayName" "${APP_NAME}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "UninstallString" "$INSTDIR\uninstall_${project_name}.exe"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayIcon" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayVersion" "${VERSION}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "Publisher" "${COMP_NAME}"

!ifdef WEB_SITE
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "URLInfoAbout" "${WEB_SITE}"
!endif
SectionEnd


######################################################################


Section Uninstall
${INSTALL_TYPE}

${delete_project_files_section}

${delete_project_folders_section}


Delete "$INSTDIR\uninstall_${project_name}.exe"
!ifdef WEB_SITE
Delete "$INSTDIR\${APP_NAME} website.url"
!endif

RmDir "$INSTDIR"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_GETFOLDER "Application" $SM_Folder
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\$SM_Folder"
!endif

!ifndef REG_START_MENU
Delete "$SMPROGRAMS\${project_name}\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\${project_name}\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\${project_name}\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\${project_name}"
!endif

DeleteRegKey ${REG_ROOT} "${REG_APP_PATH}"
DeleteRegKey ${REG_ROOT} "${UNINSTALL_PATH}"
SectionEnd""")

nsi_script_template = Template(
    nsi_script_template.template.replace("$PROGRAMFILES", "$PROGRAMFILES64")
)
logger_NSI.info("nsis script template created")


def generate_project_files_paths_section(remote_location: str):
    """ """
    project_files_paths_section = ""
    relative_paths = gather_relatives(remote_location)

    # files first (thats the patterns of nsi script)
    for rel_path in relative_paths:
        full_path = remote_location + rel_path
        result = os.path.dirname(rel_path)

        if result == os.path.sep:
            project_files_paths_section += f'File "{full_path}"\n'

    # then folders (thats the patterns of nsi script)
    last_call = None
    for rel_path in relative_paths:
        full_path = remote_location + rel_path
        result = os.path.dirname(rel_path)

        if result != os.path.sep:
            if result != last_call:
                project_files_paths_section += f'SetOutPath "$INSTDIR{result}"\n'

            last_call = result
            project_files_paths_section += f'File "{full_path}"\n'

    logger_NSI.info("files paths lines for nsis script generated.")

    return project_files_paths_section


def generate_delete_project_files_section(remote_location: str):
    """
        Delete "$INSTDIR\" aici vom pune every relative
            path from the project (only files!!!)"
    """

    delete_project_files_section = ""
    relative_paths = gather_relatives(remote_location)

    for rel_path in relative_paths:
        full_path = remote_location + rel_path
        delete_project_files_section += f'Delete "$INSTDIR{rel_path}"\n'

    logger_NSI.info("delete files paths lines for in nsis script generated")
    return delete_project_files_section


def generate_delete_project_folders_section(remote_location: str):
    """ RmDir "$INSTDIR\" aici foldere from project """

    relative_paths = gather_relatives(remote_location)

    # last_call helps the program
    # to avoid repeating deleting lines
    # of folders in nsis script
    used_folders = []
    to_delete_folders_list = []
    for rel_path in relative_paths:
        full_path = remote_location + rel_path
        result = os.path.dirname(rel_path)

        while result != os.path.sep:
            if result not in used_folders:
                used_folders.append(result)
                line = f'RmDir "$INSTDIR{result}"\n'
                to_delete_folders_list.append((line, len(line.split(os.path.sep))))
                # delete_project_folders_section += line

            result = os.path.dirname(result)


    to_delete_folders_list = sorted(to_delete_folders_list, key=lambda elem: -elem[1])

    delete_project_folders_section = ""
    for todelete in to_delete_folders_list:
        delete_project_folders_section += todelete[0]

    logger_NSI.info("delete folders paths lines for in nsis script generated")
    return delete_project_folders_section


def GenerateNSIScript(remote_location: str, project_name: str):
    """
        gets project name
        formats nsis cript path
        opens nsis script path and writes
            nsis script from template
                formatting:
                    project name
                    project folder
                    list with files paths
                    list with to delete files paths
                    list with to delete folders paths

        opens nsis script with code
        return -> nsis script path
    """
    nsis_script_path = nsis_script_path_template.safe_substitute(project_name=project_name)
    logger_NSI.info("nsis script path created")
    # opening the file and writing everything

    nsis_script = nsi_script_template.safe_substitute(
        project_name = project_name,
        remote_location = remote_location,
        project_files_paths_section = generate_project_files_paths_section(remote_location),
        delete_project_files_section = generate_delete_project_files_section(remote_location),
        delete_project_folders_section = generate_delete_project_folders_section(remote_location)
    )
    logger_NSI.info("nsis script generated")
    logger_NSI.info("\nthe nsis script:\n" + nsis_script)

    logger_NSI.info(f"opening...\n{nsis_script_path}")
    with open(nsis_script_path, "w+", encoding="utf-8") as file:
        file.truncate(0)
        file.write(nsis_script)
        logger_NSI.info(f"nsis script written to:\n{nsis_script_path}")

    # opening in vs code
    # os.system(f"code {nsis_script_path}")

    return nsis_script_path


def CompileNSIScript(nsi_script: str, remote_location: str):
    try:
        logger_NSI.info("compiling nsis script...")
        make_nsis = ["makensis", nsi_script]
        logger_NSI.info(" ".join(make_nsis))

        process = subprocess.Popen(
            make_nsis,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        err, process_output = process.communicate()
        logger_NSI.info(err.decode("utf-8"))
        logger_NSI.info(process_output.decode("utf-8"))

        logger_NSI.info("nsis script compiled successfully")
        # open_folder(remote_location)
        # logger_NSI.info("location of nsis script opened")
        logger_NSI.info("nsis.py worked")

    except BaseException as exception:
        logger_NSI.exception(str(exception))


if __name__ == '__main__':
    # remote_location = r"D:\Alexzander__\PythonApplications\PDFCreator"
    # project_name = os.path.basename(remote_location)
    # path = GenerateNSIScript(remote_location, project_name)
    # CompileNSIScript(r"D:\Alexzander__\programming\python\Python2Executable\nsis_scripts\PDFCreator.nsi", remote_location)
    # x = generate_delete_project_folders_section(remote_location)
    # print(x)
    pass