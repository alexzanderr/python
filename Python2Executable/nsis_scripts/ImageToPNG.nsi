

!define APP_NAME "ImageToPNG"
!define COMP_NAME "ImageToPNG"
!define WEB_SITE "https://alexzander.tech"
!define VERSION "1.00.00.00"
!define COPYRIGHT "alexzander's software"
!define DESCRIPTION "ImageToPNG is made using python and this nsis script is generated from python"
!define INSTALLER_NAME "D:\Alexzander__\PythonApplications\ImageToPNG\install_ImageToPNG.exe"
!define MAIN_APP_EXE "ImageToPNG.exe"
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
InstallDir "$PROGRAMFILES64\ImageToPNG"


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
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "ImageToPNG"
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
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-console-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-datetime-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-debug-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-errorhandling-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-file-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-file-l1-2-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-file-l2-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-handle-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-heap-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-interlocked-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-libraryloader-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-localization-l1-2-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-memory-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-namedpipe-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-processenvironment-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-processthreads-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-processthreads-l1-1-1.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-profile-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-rtlsupport-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-string-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-synch-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-synch-l1-2-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-sysinfo-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-timezone-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-core-util-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-conio-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-convert-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-environment-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-filesystem-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-heap-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-locale-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-math-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-multibyte-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-process-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-runtime-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-stdio-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-string-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-time-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\api-ms-win-crt-utility-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\base_library.zip"
File "D:\Alexzander__\PythonApplications\ImageToPNG\ImageToPNG.exe"
File "D:\Alexzander__\PythonApplications\ImageToPNG\ImageToPNG.exe.manifest"
File "D:\Alexzander__\PythonApplications\ImageToPNG\ImageToPNG.py"
File "D:\Alexzander__\PythonApplications\ImageToPNG\libcrypto-1_1-x64.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\libssl-1_1-x64.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\mfc140u.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\pyexpat.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\python3.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\python37.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\pythoncom37.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\pywintypes37.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\recents.json"
File "D:\Alexzander__\PythonApplications\ImageToPNG\select.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\ucrtbase.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\unicodedata.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\VCRUNTIME140.dll"
File "D:\Alexzander__\PythonApplications\ImageToPNG\win32api.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\win32gui.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\win32trace.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\win32ui.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\win32wnet.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_bz2.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_cffi_backend.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_contextvars.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_ctypes.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_curses.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_decimal.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_elementtree.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_hashlib.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_lzma.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_multiprocessing.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_queue.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_socket.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_ssl.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\_win32sysloader.pyd"
SetOutPath "$INSTDIR\build_logs"
File "D:\Alexzander__\PythonApplications\ImageToPNG\build_logs\build_27.02.2021__17_09_47.log"
SetOutPath "$INSTDIR\certifi"
File "D:\Alexzander__\PythonApplications\ImageToPNG\certifi\cacert.pem"
SetOutPath "$INSTDIR\cryptography\hazmat\bindings"
File "D:\Alexzander__\PythonApplications\ImageToPNG\cryptography\hazmat\bindings\_openssl.pyd"
SetOutPath "$INSTDIR\cryptography-3.4.6-py3.7.egg-info"
File "D:\Alexzander__\PythonApplications\ImageToPNG\cryptography-3.4.6-py3.7.egg-info\INSTALLER"
File "D:\Alexzander__\PythonApplications\ImageToPNG\cryptography-3.4.6-py3.7.egg-info\LICENSE"
File "D:\Alexzander__\PythonApplications\ImageToPNG\cryptography-3.4.6-py3.7.egg-info\LICENSE.APACHE"
File "D:\Alexzander__\PythonApplications\ImageToPNG\cryptography-3.4.6-py3.7.egg-info\LICENSE.BSD"
File "D:\Alexzander__\PythonApplications\ImageToPNG\cryptography-3.4.6-py3.7.egg-info\LICENSE.PSF"
File "D:\Alexzander__\PythonApplications\ImageToPNG\cryptography-3.4.6-py3.7.egg-info\METADATA"
File "D:\Alexzander__\PythonApplications\ImageToPNG\cryptography-3.4.6-py3.7.egg-info\RECORD"
File "D:\Alexzander__\PythonApplications\ImageToPNG\cryptography-3.4.6-py3.7.egg-info\top_level.txt"
File "D:\Alexzander__\PythonApplications\ImageToPNG\cryptography-3.4.6-py3.7.egg-info\WHEEL"
SetOutPath "$INSTDIR\icons"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\app.png"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\app2.png"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\asdasd123123.ico"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\asdopabndasbndujioas.png"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\avon.png"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\exec.ico"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\exece.ico"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\exe_c.ico"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\suc.ico"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\suc2.ico"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\suc2.png"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\success.ico"
File "D:\Alexzander__\PythonApplications\ImageToPNG\icons\success.png"
SetOutPath "$INSTDIR\Include"
File "D:\Alexzander__\PythonApplications\ImageToPNG\Include\pyconfig.h"
SetOutPath "$INSTDIR\PIL"
File "D:\Alexzander__\PythonApplications\ImageToPNG\PIL\_imaging.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\PIL\_imagingft.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\PIL\_imagingtk.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\ImageToPNG\PIL\_webp.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\win32com\shell"
File "D:\Alexzander__\PythonApplications\ImageToPNG\win32com\shell\shell.pyd"

SectionEnd


######################################################################


Section -Icons_Reg
SetOutPath "$INSTDIR"
WriteUninstaller "$INSTDIR\uninstall_ImageToPNG.exe"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
CreateDirectory "$SMPROGRAMS\$SM_Folder"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall_ImageToPNG.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!insertmacro MUI_STARTMENU_WRITE_END
!endif

!ifndef REG_START_MENU
CreateDirectory "$SMPROGRAMS\ImageToPNG"
CreateShortCut "$SMPROGRAMS\ImageToPNG\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\ImageToPNG\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall_ImageToPNG.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\ImageToPNG\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!endif

WriteRegStr ${REG_ROOT} "${REG_APP_PATH}" "" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayName" "${APP_NAME}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "UninstallString" "$INSTDIR\uninstall_ImageToPNG.exe"
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
Delete "$INSTDIR\build_logs\build_27.02.2021__17_09_47.log"
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
Delete "$INSTDIR\icons\app.png"
Delete "$INSTDIR\icons\app2.png"
Delete "$INSTDIR\icons\asdasd123123.ico"
Delete "$INSTDIR\icons\asdopabndasbndujioas.png"
Delete "$INSTDIR\icons\avon.png"
Delete "$INSTDIR\icons\exec.ico"
Delete "$INSTDIR\icons\exece.ico"
Delete "$INSTDIR\icons\exe_c.ico"
Delete "$INSTDIR\icons\suc.ico"
Delete "$INSTDIR\icons\suc2.ico"
Delete "$INSTDIR\icons\suc2.png"
Delete "$INSTDIR\icons\success.ico"
Delete "$INSTDIR\icons\success.png"
Delete "$INSTDIR\ImageToPNG.exe"
Delete "$INSTDIR\ImageToPNG.exe.manifest"
Delete "$INSTDIR\ImageToPNG.py"
Delete "$INSTDIR\Include\pyconfig.h"
Delete "$INSTDIR\libcrypto-1_1-x64.dll"
Delete "$INSTDIR\libssl-1_1-x64.dll"
Delete "$INSTDIR\mfc140u.dll"
Delete "$INSTDIR\PIL\_imaging.cp37-win_amd64.pyd"
Delete "$INSTDIR\PIL\_imagingft.cp37-win_amd64.pyd"
Delete "$INSTDIR\PIL\_imagingtk.cp37-win_amd64.pyd"
Delete "$INSTDIR\PIL\_webp.cp37-win_amd64.pyd"
Delete "$INSTDIR\pyexpat.pyd"
Delete "$INSTDIR\python3.dll"
Delete "$INSTDIR\python37.dll"
Delete "$INSTDIR\pythoncom37.dll"
Delete "$INSTDIR\pywintypes37.dll"
Delete "$INSTDIR\recents.json"
Delete "$INSTDIR\select.pyd"
Delete "$INSTDIR\ucrtbase.dll"
Delete "$INSTDIR\unicodedata.pyd"
Delete "$INSTDIR\VCRUNTIME140.dll"
Delete "$INSTDIR\win32api.pyd"
Delete "$INSTDIR\win32com\shell\shell.pyd"
Delete "$INSTDIR\win32gui.pyd"
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
Delete "$INSTDIR\_queue.pyd"
Delete "$INSTDIR\_socket.pyd"
Delete "$INSTDIR\_ssl.pyd"
Delete "$INSTDIR\_win32sysloader.pyd"


RmDir "$INSTDIR\cryptography\hazmat\bindings"
RmDir "$INSTDIR\cryptography\hazmat"
RmDir "$INSTDIR\win32com\shell"
RmDir "$INSTDIR\build_logs"
RmDir "$INSTDIR\certifi"
RmDir "$INSTDIR\cryptography"
RmDir "$INSTDIR\cryptography-3.4.6-py3.7.egg-info"
RmDir "$INSTDIR\icons"
RmDir "$INSTDIR\Include"
RmDir "$INSTDIR\PIL"
RmDir "$INSTDIR\win32com"



Delete "$INSTDIR\uninstall_ImageToPNG.exe"
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
Delete "$SMPROGRAMS\ImageToPNG\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\ImageToPNG\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\ImageToPNG\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\ImageToPNG"
!endif

DeleteRegKey ${REG_ROOT} "${REG_APP_PATH}"
DeleteRegKey ${REG_ROOT} "${UNINSTALL_PATH}"
SectionEnd