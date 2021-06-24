

!define APP_NAME "Python2Executable"
!define COMP_NAME "Python2Executable"
!define WEB_SITE "https://alexzander.tech"
!define VERSION "1.00.00.00"
!define COPYRIGHT "alexzander's software"
!define DESCRIPTION "Python2Executable is made using python and this nsis script is generated from python"
!define INSTALLER_NAME "D:\Alexzander__\PythonApplications\Python2Executable\install_Python2Executable.exe"
!define MAIN_APP_EXE "Python2Executable.exe"
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
InstallDir "$PROGRAMFILES64\Python2Executable"


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
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "Python2Executable"
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
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-console-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-datetime-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-debug-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-errorhandling-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-file-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-file-l1-2-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-file-l2-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-handle-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-heap-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-interlocked-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-libraryloader-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-localization-l1-2-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-memory-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-namedpipe-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-processenvironment-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-processthreads-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-processthreads-l1-1-1.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-profile-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-rtlsupport-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-string-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-synch-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-synch-l1-2-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-sysinfo-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-timezone-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-core-util-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-conio-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-convert-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-environment-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-filesystem-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-heap-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-locale-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-math-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-multibyte-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-process-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-runtime-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-stdio-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-string-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-time-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\api-ms-win-crt-utility-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\base_library.zip"
File "D:\Alexzander__\PythonApplications\Python2Executable\build.py"
File "D:\Alexzander__\PythonApplications\Python2Executable\history.py"
File "D:\Alexzander__\PythonApplications\Python2Executable\imports.py"
File "D:\Alexzander__\PythonApplications\Python2Executable\install_Python2Executable.exe"
File "D:\Alexzander__\PythonApplications\Python2Executable\libcrypto-1_1-x64.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\libssl-1_1-x64.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\mfc140u.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\nsis.py"
File "D:\Alexzander__\PythonApplications\Python2Executable\pyexpat.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\Python2Executable.exe"
File "D:\Alexzander__\PythonApplications\Python2Executable\Python2Executable.exe.manifest"
File "D:\Alexzander__\PythonApplications\Python2Executable\python3.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\python37.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\pythoncom37.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\pywintypes37.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\select.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\transfer.py"
File "D:\Alexzander__\PythonApplications\Python2Executable\ucrtbase.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\unicodedata.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\validation.py"
File "D:\Alexzander__\PythonApplications\Python2Executable\VCRUNTIME140.dll"
File "D:\Alexzander__\PythonApplications\Python2Executable\win32api.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\win32trace.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\win32ui.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\win32wnet.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_bz2.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_cffi_backend.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_contextvars.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_ctypes.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_curses.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_decimal.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_elementtree.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_hashlib.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_lzma.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_multiprocessing.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_Python2Executable.py"
File "D:\Alexzander__\PythonApplications\Python2Executable\_queue.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_socket.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_ssl.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\_win32sysloader.pyd"
SetOutPath "$INSTDIR\certifi"
File "D:\Alexzander__\PythonApplications\Python2Executable\certifi\cacert.pem"
SetOutPath "$INSTDIR\cryptography\hazmat\bindings"
File "D:\Alexzander__\PythonApplications\Python2Executable\cryptography\hazmat\bindings\_openssl.pyd"
SetOutPath "$INSTDIR\cryptography-3.4.6-py3.7.egg-info"
File "D:\Alexzander__\PythonApplications\Python2Executable\cryptography-3.4.6-py3.7.egg-info\INSTALLER"
File "D:\Alexzander__\PythonApplications\Python2Executable\cryptography-3.4.6-py3.7.egg-info\LICENSE"
File "D:\Alexzander__\PythonApplications\Python2Executable\cryptography-3.4.6-py3.7.egg-info\LICENSE.APACHE"
File "D:\Alexzander__\PythonApplications\Python2Executable\cryptography-3.4.6-py3.7.egg-info\LICENSE.BSD"
File "D:\Alexzander__\PythonApplications\Python2Executable\cryptography-3.4.6-py3.7.egg-info\LICENSE.PSF"
File "D:\Alexzander__\PythonApplications\Python2Executable\cryptography-3.4.6-py3.7.egg-info\METADATA"
File "D:\Alexzander__\PythonApplications\Python2Executable\cryptography-3.4.6-py3.7.egg-info\RECORD"
File "D:\Alexzander__\PythonApplications\Python2Executable\cryptography-3.4.6-py3.7.egg-info\top_level.txt"
File "D:\Alexzander__\PythonApplications\Python2Executable\cryptography-3.4.6-py3.7.egg-info\WHEEL"
SetOutPath "$INSTDIR\icons"
File "D:\Alexzander__\PythonApplications\Python2Executable\icons\app.png"
File "D:\Alexzander__\PythonApplications\Python2Executable\icons\asd1o23ibnju.ico"
File "D:\Alexzander__\PythonApplications\Python2Executable\icons\asduobob12ji3b123bih123.png"
File "D:\Alexzander__\PythonApplications\Python2Executable\icons\exec.ico"
File "D:\Alexzander__\PythonApplications\Python2Executable\icons\exec.png"
File "D:\Alexzander__\PythonApplications\Python2Executable\icons\exec123.ico"
File "D:\Alexzander__\PythonApplications\Python2Executable\icons\exec2.jpg"
File "D:\Alexzander__\PythonApplications\Python2Executable\icons\exec3.ico"
File "D:\Alexzander__\PythonApplications\Python2Executable\icons\exec__.ico"
File "D:\Alexzander__\PythonApplications\Python2Executable\icons\test.png"
SetOutPath "$INSTDIR\Include"
File "D:\Alexzander__\PythonApplications\Python2Executable\Include\pyconfig.h"
SetOutPath "$INSTDIR\logs"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\build_25.02.2021__16_10_31.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\build_26.02.2021__14_46_31.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\build_27.02.2021__11_55_19.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_25.02.2021__13_14_38.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_25.02.2021__13_19_25.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_25.02.2021__16_10_09.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_26.02.2021__14_45_22.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_26.02.2021__14_46_29.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_26.02.2021__14_47_58.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_26.02.2021__14_48_03.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_26.02.2021__14_48_08.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_26.02.2021__15_16_37.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_26.02.2021__15_16_38.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_27.02.2021__10_53_57.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_27.02.2021__11_42_41.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_27.02.2021__11_55_13.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\logs\py2exe_27.02.2021__11_55_43.log"
SetOutPath "$INSTDIR\nsis_scripts"
File "D:\Alexzander__\PythonApplications\Python2Executable\nsis_scripts\202020_order.nsi"
File "D:\Alexzander__\PythonApplications\Python2Executable\nsis_scripts\CorruptionTester.nsi"
File "D:\Alexzander__\PythonApplications\Python2Executable\nsis_scripts\FileHunter.nsi"
File "D:\Alexzander__\PythonApplications\Python2Executable\nsis_scripts\PDFCreator.nsi"
File "D:\Alexzander__\PythonApplications\Python2Executable\nsis_scripts\Python2Executable.nsi"
File "D:\Alexzander__\PythonApplications\Python2Executable\nsis_scripts\simple_package.nsi"
File "D:\Alexzander__\PythonApplications\Python2Executable\nsis_scripts\SlashConverter.nsi"
File "D:\Alexzander__\PythonApplications\Python2Executable\nsis_scripts\template.nsi"
SetOutPath "$INSTDIR\PIL"
File "D:\Alexzander__\PythonApplications\Python2Executable\PIL\_imaging.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\PIL\_imagingft.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\PIL\_imagingtk.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\Python2Executable\PIL\_webp.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\projects_history"
File "D:\Alexzander__\PythonApplications\Python2Executable\projects_history\all_projects.json"
File "D:\Alexzander__\PythonApplications\Python2Executable\projects_history\last_project.json"
SetOutPath "$INSTDIR\simulate\simple_package\icons"
File "D:\Alexzander__\PythonApplications\Python2Executable\simulate\simple_package\icons\exec.ico"
SetOutPath "$INSTDIR\simulate\simple_package\logs"
File "D:\Alexzander__\PythonApplications\Python2Executable\simulate\simple_package\logs\build_25.02.2021__13_19_37.log"
File "D:\Alexzander__\PythonApplications\Python2Executable\simulate\simple_package\logs\build_25.02.2021__13_20_21.log"
SetOutPath "$INSTDIR\simulate\simple_package"
File "D:\Alexzander__\PythonApplications\Python2Executable\simulate\simple_package\main.py"
SetOutPath "$INSTDIR\tests"
File "D:\Alexzander__\PythonApplications\Python2Executable\tests\unittesting.py"
SetOutPath "$INSTDIR\win32"
File "D:\Alexzander__\PythonApplications\Python2Executable\win32\win32api.pyd"
SetOutPath "$INSTDIR\win32com\shell"
File "D:\Alexzander__\PythonApplications\Python2Executable\win32com\shell\shell.pyd"

SectionEnd


######################################################################


Section -Icons_Reg
SetOutPath "$INSTDIR"
WriteUninstaller "$INSTDIR\uninstall_Python2Executable.exe"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
CreateDirectory "$SMPROGRAMS\$SM_Folder"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall_Python2Executable.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!insertmacro MUI_STARTMENU_WRITE_END
!endif

!ifndef REG_START_MENU
CreateDirectory "$SMPROGRAMS\Python2Executable"
CreateShortCut "$SMPROGRAMS\Python2Executable\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\Python2Executable\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall_Python2Executable.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\Python2Executable\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!endif

WriteRegStr ${REG_ROOT} "${REG_APP_PATH}" "" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayName" "${APP_NAME}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "UninstallString" "$INSTDIR\uninstall_Python2Executable.exe"
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

Delete "$INSTDIR\api-ms-win-core-console-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-datetime-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-debug-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-errorhandling-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-file-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-file-l1-2-0.dll"
Delete "$INSTDIR\api-ms-win-core-file-l2-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-handle-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-heap-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-interlocked-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-libraryloader-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-localization-l1-2-0.dll"
Delete "$INSTDIR\api-ms-win-core-memory-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-namedpipe-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-processenvironment-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-processthreads-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-processthreads-l1-1-1.dll"
Delete "$INSTDIR\api-ms-win-core-profile-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-rtlsupport-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-string-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-synch-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-synch-l1-2-0.dll"
Delete "$INSTDIR\api-ms-win-core-sysinfo-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-timezone-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-util-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-conio-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-convert-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-environment-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-filesystem-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-heap-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-locale-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-math-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-multibyte-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-process-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-runtime-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-stdio-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-string-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-time-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-utility-l1-1-0.dll"
Delete "$INSTDIR\base_library.zip"
Delete "$INSTDIR\build.py"
Delete "$INSTDIR\certifi\cacert.pem"
Delete "$INSTDIR\cryptography\hazmat\bindings\_openssl.pyd"
Delete "$INSTDIR\cryptography-3.4.6-py3.7.egg-info\INSTALLER"
Delete "$INSTDIR\cryptography-3.4.6-py3.7.egg-info\LICENSE"
Delete "$INSTDIR\cryptography-3.4.6-py3.7.egg-info\LICENSE.APACHE"
Delete "$INSTDIR\cryptography-3.4.6-py3.7.egg-info\LICENSE.BSD"
Delete "$INSTDIR\cryptography-3.4.6-py3.7.egg-info\LICENSE.PSF"
Delete "$INSTDIR\cryptography-3.4.6-py3.7.egg-info\METADATA"
Delete "$INSTDIR\cryptography-3.4.6-py3.7.egg-info\RECORD"
Delete "$INSTDIR\cryptography-3.4.6-py3.7.egg-info\top_level.txt"
Delete "$INSTDIR\cryptography-3.4.6-py3.7.egg-info\WHEEL"
Delete "$INSTDIR\history.py"
Delete "$INSTDIR\icons\app.png"
Delete "$INSTDIR\icons\asd1o23ibnju.ico"
Delete "$INSTDIR\icons\asduobob12ji3b123bih123.png"
Delete "$INSTDIR\icons\exec.ico"
Delete "$INSTDIR\icons\exec.png"
Delete "$INSTDIR\icons\exec123.ico"
Delete "$INSTDIR\icons\exec2.jpg"
Delete "$INSTDIR\icons\exec3.ico"
Delete "$INSTDIR\icons\exec__.ico"
Delete "$INSTDIR\icons\test.png"
Delete "$INSTDIR\imports.py"
Delete "$INSTDIR\Include\pyconfig.h"
Delete "$INSTDIR\install_Python2Executable.exe"
Delete "$INSTDIR\libcrypto-1_1-x64.dll"
Delete "$INSTDIR\libssl-1_1-x64.dll"
Delete "$INSTDIR\logs\build_25.02.2021__16_10_31.log"
Delete "$INSTDIR\logs\build_26.02.2021__14_46_31.log"
Delete "$INSTDIR\logs\build_27.02.2021__11_55_19.log"
Delete "$INSTDIR\logs\py2exe_25.02.2021__13_14_38.log"
Delete "$INSTDIR\logs\py2exe_25.02.2021__13_19_25.log"
Delete "$INSTDIR\logs\py2exe_25.02.2021__16_10_09.log"
Delete "$INSTDIR\logs\py2exe_26.02.2021__14_45_22.log"
Delete "$INSTDIR\logs\py2exe_26.02.2021__14_46_29.log"
Delete "$INSTDIR\logs\py2exe_26.02.2021__14_47_58.log"
Delete "$INSTDIR\logs\py2exe_26.02.2021__14_48_03.log"
Delete "$INSTDIR\logs\py2exe_26.02.2021__14_48_08.log"
Delete "$INSTDIR\logs\py2exe_26.02.2021__15_16_37.log"
Delete "$INSTDIR\logs\py2exe_26.02.2021__15_16_38.log"
Delete "$INSTDIR\logs\py2exe_27.02.2021__10_53_57.log"
Delete "$INSTDIR\logs\py2exe_27.02.2021__11_42_41.log"
Delete "$INSTDIR\logs\py2exe_27.02.2021__11_55_13.log"
Delete "$INSTDIR\logs\py2exe_27.02.2021__11_55_43.log"
Delete "$INSTDIR\mfc140u.dll"
Delete "$INSTDIR\nsis.py"
Delete "$INSTDIR\nsis_scripts\202020_order.nsi"
Delete "$INSTDIR\nsis_scripts\CorruptionTester.nsi"
Delete "$INSTDIR\nsis_scripts\FileHunter.nsi"
Delete "$INSTDIR\nsis_scripts\PDFCreator.nsi"
Delete "$INSTDIR\nsis_scripts\Python2Executable.nsi"
Delete "$INSTDIR\nsis_scripts\simple_package.nsi"
Delete "$INSTDIR\nsis_scripts\SlashConverter.nsi"
Delete "$INSTDIR\nsis_scripts\template.nsi"
Delete "$INSTDIR\PIL\_imaging.cp37-win_amd64.pyd"
Delete "$INSTDIR\PIL\_imagingft.cp37-win_amd64.pyd"
Delete "$INSTDIR\PIL\_imagingtk.cp37-win_amd64.pyd"
Delete "$INSTDIR\PIL\_webp.cp37-win_amd64.pyd"
Delete "$INSTDIR\projects_history\all_projects.json"
Delete "$INSTDIR\projects_history\last_project.json"
Delete "$INSTDIR\pyexpat.pyd"
Delete "$INSTDIR\Python2Executable.exe"
Delete "$INSTDIR\Python2Executable.exe.manifest"
Delete "$INSTDIR\python3.dll"
Delete "$INSTDIR\python37.dll"
Delete "$INSTDIR\pythoncom37.dll"
Delete "$INSTDIR\pywintypes37.dll"
Delete "$INSTDIR\select.pyd"
Delete "$INSTDIR\simulate\simple_package\icons\exec.ico"
Delete "$INSTDIR\simulate\simple_package\logs\build_25.02.2021__13_19_37.log"
Delete "$INSTDIR\simulate\simple_package\logs\build_25.02.2021__13_20_21.log"
Delete "$INSTDIR\simulate\simple_package\main.py"
Delete "$INSTDIR\tests\unittesting.py"
Delete "$INSTDIR\transfer.py"
Delete "$INSTDIR\ucrtbase.dll"
Delete "$INSTDIR\unicodedata.pyd"
Delete "$INSTDIR\validation.py"
Delete "$INSTDIR\VCRUNTIME140.dll"
Delete "$INSTDIR\win32\win32api.pyd"
Delete "$INSTDIR\win32api.pyd"
Delete "$INSTDIR\win32com\shell\shell.pyd"
Delete "$INSTDIR\win32trace.pyd"
Delete "$INSTDIR\win32ui.pyd"
Delete "$INSTDIR\win32wnet.pyd"
Delete "$INSTDIR\_bz2.pyd"
Delete "$INSTDIR\_cffi_backend.cp37-win_amd64.pyd"
Delete "$INSTDIR\_contextvars.pyd"
Delete "$INSTDIR\_ctypes.pyd"
Delete "$INSTDIR\_curses.cp37-win_amd64.pyd"
Delete "$INSTDIR\_decimal.pyd"
Delete "$INSTDIR\_elementtree.pyd"
Delete "$INSTDIR\_hashlib.pyd"
Delete "$INSTDIR\_lzma.pyd"
Delete "$INSTDIR\_multiprocessing.pyd"
Delete "$INSTDIR\_Python2Executable.py"
Delete "$INSTDIR\_queue.pyd"
Delete "$INSTDIR\_socket.pyd"
Delete "$INSTDIR\_ssl.pyd"
Delete "$INSTDIR\_win32sysloader.pyd"


RmDir "$INSTDIR\cryptography\hazmat\bindings"
RmDir "$INSTDIR\simulate\simple_package\icons"
RmDir "$INSTDIR\simulate\simple_package\logs"
RmDir "$INSTDIR\cryptography\hazmat"
RmDir "$INSTDIR\simulate\simple_package"
RmDir "$INSTDIR\win32com\shell"
RmDir "$INSTDIR\certifi"
RmDir "$INSTDIR\cryptography"
RmDir "$INSTDIR\cryptography-3.4.6-py3.7.egg-info"
RmDir "$INSTDIR\icons"
RmDir "$INSTDIR\Include"
RmDir "$INSTDIR\logs"
RmDir "$INSTDIR\nsis_scripts"
RmDir "$INSTDIR\PIL"
RmDir "$INSTDIR\projects_history"
RmDir "$INSTDIR\simulate"
RmDir "$INSTDIR\tests"
RmDir "$INSTDIR\win32"
RmDir "$INSTDIR\win32com"



Delete "$INSTDIR\uninstall_Python2Executable.exe"
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
Delete "$SMPROGRAMS\Python2Executable\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\Python2Executable\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\Python2Executable\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\Python2Executable"
!endif

DeleteRegKey ${REG_ROOT} "${REG_APP_PATH}"
DeleteRegKey ${REG_ROOT} "${UNINSTALL_PATH}"
SectionEnd