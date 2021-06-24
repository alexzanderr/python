

!define APP_NAME "ImageToICO"
!define COMP_NAME "ImageToICO"
!define WEB_SITE "https://alexzander.tech"
!define VERSION "1.00.00.00"
!define COPYRIGHT "alexzander's software"
!define DESCRIPTION "ImageToICO is made using python and this nsis script is generated from python"
!define INSTALLER_NAME "D:\Alexzander__\PythonApplications\ImageToICO\install_ImageToICO.exe"
!define MAIN_APP_EXE "ImageToICO.exe"
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
InstallDir "$PROGRAMFILES64\ImageToICO"


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
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "ImageToICO"
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
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-console-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-datetime-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-debug-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-errorhandling-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-file-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-file-l1-2-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-file-l2-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-handle-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-heap-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-interlocked-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-libraryloader-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-localization-l1-2-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-memory-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-namedpipe-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-processenvironment-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-processthreads-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-processthreads-l1-1-1.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-profile-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-rtlsupport-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-string-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-synch-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-synch-l1-2-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-sysinfo-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-timezone-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-core-util-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-conio-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-convert-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-environment-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-filesystem-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-heap-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-locale-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-math-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-multibyte-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-process-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-runtime-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-stdio-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-string-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-time-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\api-ms-win-crt-utility-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\base_library.zip"
File "D:\Alexzander__\PythonApplications\ImageToICO\ImageToICO.exe"
File "D:\Alexzander__\PythonApplications\ImageToICO\ImageToICO.exe.manifest"
File "D:\Alexzander__\PythonApplications\ImageToICO\ImageToICO.py"
File "D:\Alexzander__\PythonApplications\ImageToICO\libcrypto-1_1-x64.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\libssl-1_1-x64.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\mfc140u.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\pyexpat.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\python3.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\python37.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\pythoncom37.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\pywintypes37.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\select.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\ucrtbase.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\unicodedata.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\VCRUNTIME140.dll"
File "D:\Alexzander__\PythonApplications\ImageToICO\win32api.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\win32gui.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\win32trace.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\win32ui.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\win32wnet.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_bz2.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_cffi_backend.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_contextvars.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_ctypes.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_curses.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_decimal.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_elementtree.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_hashlib.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_lzma.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_multiprocessing.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_queue.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_socket.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_ssl.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\_win32sysloader.pyd"
SetOutPath "$INSTDIR\build_logs"
File "D:\Alexzander__\PythonApplications\ImageToICO\build_logs\build_27.02.2021__17_28_39.log"
SetOutPath "$INSTDIR\certifi"
File "D:\Alexzander__\PythonApplications\ImageToICO\certifi\cacert.pem"
SetOutPath "$INSTDIR\cryptography\hazmat\bindings"
File "D:\Alexzander__\PythonApplications\ImageToICO\cryptography\hazmat\bindings\_openssl.pyd"
SetOutPath "$INSTDIR\cryptography-3.4.6-py3.7.egg-info"
File "D:\Alexzander__\PythonApplications\ImageToICO\cryptography-3.4.6-py3.7.egg-info\INSTALLER"
File "D:\Alexzander__\PythonApplications\ImageToICO\cryptography-3.4.6-py3.7.egg-info\LICENSE"
File "D:\Alexzander__\PythonApplications\ImageToICO\cryptography-3.4.6-py3.7.egg-info\LICENSE.APACHE"
File "D:\Alexzander__\PythonApplications\ImageToICO\cryptography-3.4.6-py3.7.egg-info\LICENSE.BSD"
File "D:\Alexzander__\PythonApplications\ImageToICO\cryptography-3.4.6-py3.7.egg-info\LICENSE.PSF"
File "D:\Alexzander__\PythonApplications\ImageToICO\cryptography-3.4.6-py3.7.egg-info\METADATA"
File "D:\Alexzander__\PythonApplications\ImageToICO\cryptography-3.4.6-py3.7.egg-info\RECORD"
File "D:\Alexzander__\PythonApplications\ImageToICO\cryptography-3.4.6-py3.7.egg-info\top_level.txt"
File "D:\Alexzander__\PythonApplications\ImageToICO\cryptography-3.4.6-py3.7.egg-info\WHEEL"
SetOutPath "$INSTDIR\icons"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\1.ico"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\1.png"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\123123.ico"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\asd1234123.ico"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\asdasd.ico"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\asjiodbasjibdasjid.png"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\exec.ico"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\green_suc.png"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\green_suc_converted.ico"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\iconnn'.png"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\succ.png"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\success_icon.ico"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\succ_big.png"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\succ_big_converted.ico"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\succ_converted.ico"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\testing.png"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\testing2.png"
File "D:\Alexzander__\PythonApplications\ImageToICO\icons\testing3.png"
SetOutPath "$INSTDIR\Include"
File "D:\Alexzander__\PythonApplications\ImageToICO\Include\pyconfig.h"
SetOutPath "$INSTDIR\PIL"
File "D:\Alexzander__\PythonApplications\ImageToICO\PIL\_imaging.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\PIL\_imagingft.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\PIL\_imagingtk.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\ImageToICO\PIL\_webp.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\win32"
File "D:\Alexzander__\PythonApplications\ImageToICO\win32\win32api.pyd"
SetOutPath "$INSTDIR\win32com\shell"
File "D:\Alexzander__\PythonApplications\ImageToICO\win32com\shell\shell.pyd"

SectionEnd


######################################################################


Section -Icons_Reg
SetOutPath "$INSTDIR"
WriteUninstaller "$INSTDIR\uninstall_ImageToICO.exe"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
CreateDirectory "$SMPROGRAMS\$SM_Folder"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall_ImageToICO.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!insertmacro MUI_STARTMENU_WRITE_END
!endif

!ifndef REG_START_MENU
CreateDirectory "$SMPROGRAMS\ImageToICO"
CreateShortCut "$SMPROGRAMS\ImageToICO\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\ImageToICO\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall_ImageToICO.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\ImageToICO\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!endif

WriteRegStr ${REG_ROOT} "${REG_APP_PATH}" "" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayName" "${APP_NAME}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "UninstallString" "$INSTDIR\uninstall_ImageToICO.exe"
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
Delete "$INSTDIR\build_logs\build_27.02.2021__17_28_39.log"
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
Delete "$INSTDIR\icons\1.ico"
Delete "$INSTDIR\icons\1.png"
Delete "$INSTDIR\icons\123123.ico"
Delete "$INSTDIR\icons\asd1234123.ico"
Delete "$INSTDIR\icons\asdasd.ico"
Delete "$INSTDIR\icons\asjiodbasjibdasjid.png"
Delete "$INSTDIR\icons\exec.ico"
Delete "$INSTDIR\icons\green_suc.png"
Delete "$INSTDIR\icons\green_suc_converted.ico"
Delete "$INSTDIR\icons\iconnn'.png"
Delete "$INSTDIR\icons\succ.png"
Delete "$INSTDIR\icons\success_icon.ico"
Delete "$INSTDIR\icons\succ_big.png"
Delete "$INSTDIR\icons\succ_big_converted.ico"
Delete "$INSTDIR\icons\succ_converted.ico"
Delete "$INSTDIR\icons\testing.png"
Delete "$INSTDIR\icons\testing2.png"
Delete "$INSTDIR\icons\testing3.png"
Delete "$INSTDIR\ImageToICO.exe"
Delete "$INSTDIR\ImageToICO.exe.manifest"
Delete "$INSTDIR\ImageToICO.py"
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
Delete "$INSTDIR\select.pyd"
Delete "$INSTDIR\ucrtbase.dll"
Delete "$INSTDIR\unicodedata.pyd"
Delete "$INSTDIR\VCRUNTIME140.dll"
Delete "$INSTDIR\win32\win32api.pyd"
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
RmDir "$INSTDIR\win32"
RmDir "$INSTDIR\win32com"



Delete "$INSTDIR\uninstall_ImageToICO.exe"
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
Delete "$SMPROGRAMS\ImageToICO\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\ImageToICO\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\ImageToICO\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\ImageToICO"
!endif

DeleteRegKey ${REG_ROOT} "${REG_APP_PATH}"
DeleteRegKey ${REG_ROOT} "${UNINSTALL_PATH}"
SectionEnd