

!define APP_NAME "PDFCreator"
!define COMP_NAME "PDFCreator"
!define WEB_SITE "https://alexzander.tech"
!define VERSION "1.00.00.00"
!define COPYRIGHT "alexzander's software"
!define DESCRIPTION "PDFCreator is made using python and this nsis script is generated from python"
!define INSTALLER_NAME "D:\Alexzander__\PythonApplications\PDFCreator\install_PDFCreator.exe"
!define MAIN_APP_EXE "PDFCreator.exe"
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
InstallDir "$PROGRAMFILES64\PDFCreator"


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
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "PDFCreator"
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
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-console-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-datetime-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-debug-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-errorhandling-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-file-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-file-l1-2-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-file-l2-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-handle-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-heap-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-interlocked-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-libraryloader-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-localization-l1-2-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-memory-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-namedpipe-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-processenvironment-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-processthreads-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-processthreads-l1-1-1.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-profile-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-rtlsupport-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-string-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-synch-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-synch-l1-2-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-sysinfo-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-timezone-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-core-util-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-conio-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-convert-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-environment-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-filesystem-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-heap-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-locale-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-math-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-multibyte-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-process-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-runtime-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-stdio-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-string-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-time-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\api-ms-win-crt-utility-l1-1-0.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\base_library.zip"
File "D:\Alexzander__\PythonApplications\PDFCreator\install_PDFCreator.exe"
File "D:\Alexzander__\PythonApplications\PDFCreator\libansari.R6EA3HQP5KZ6TAXU4Y4ZVTRPT7UVA53Z.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libbanded5x.ESF6LBN6R5UJFVJPSFF43URXBMGC3QEN.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libbispeu.7AH3PCQ2E2NGLC3AQD7FFAH73KGJTZCJ.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libblkdta00.4WSITLJKIDKQOUHFTTKLQEGVSSFMMZS7.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libchkder.G7WSOGIYYQO3UWFVEZ3PPXCXR53ADVPA.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libcobyla2.25EVUSEBAW7VKISARB7LO3UGZPN2HXE3.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libcrypto-1_1-x64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libdcsrch.I2AOPDCXAPDRFNPWY55H5UE7XZSU5CVN.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libdet.ZR5WBP5EE4H6A2LANGYSEUMRZX2FURDL.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libdfft.M3WGVBMYA2L7GTSQSBCA5QKI6BDRF2IU.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libdfitpack.TCSQXP62XZEF2TJFDUO4ZNU2JINJ5MPX.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libdgamln.HZLYI765YOFRVQOCNKFL5RM2SXIDZ2F6.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libdqag.Y76S4TW6JPXNBNXUTVXLMXJ7XT6OMWLT.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libd_odr.THQQ64REMK7ZMZRF2IS7Z5IEON7RSLK5.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libgetbreak.YQM3SI6KRD7DFG7DL7B6RJEWQS4O6YW3.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\liblbfgsb.KB47UAMDWJMP5C4XWQK5Y34RR3LKHELH.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\liblsoda-f2.FIRRCAPSEZOIP3OLBLML4456LCBTH74K.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libmvndst.5VXNIPAPINAF5NIHXAFNA4OTHOPNDEWG.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libnnls.4HUTGAJQTI623WTX372VAIIWXRLC62YU.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libopenblas.3HBPCJB5BPQGKWVZAVEBXNNJ2Q2G3TUP.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libopenblas.NOIJJG62EMASZI6NYURL6JBKM4EVBGM7.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libslsqp_op.RGGN6ZOFD2K47X7YRNDYCM7JFP4AGLER.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libspecfun.LQCTHMCYNULEOOGKIO6AGREE6D6V37RU.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libssl-1_1-x64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libvode-f2p.6FM2HIVOTF5QYRFPB7NAXVUGSWK7BJAT.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libwrap_dum.E2DMRP662KYHKE5OXJQOLMJBUYPRL4WK.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\libwrap_dum.PULJDUMZZKIM7OUS2TIYPZE4PPPRMQA2.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\lib_arpack-.7TQXDBTMUFOO5AB4ZKS2WPRZAGXNAPTE.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\lib_blas_su.X3MTOIZ5PXAH5LOTFDAJVXR3245XHGNP.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\lib_dop-f2p.H5ICLGM4NKU5EDEIUJIKVMQ6YNOF7IZ6.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\lib_test_fo.JF5HTWMUPBXWGAYEBVEJU3OZAHTSVKCT.gfortran-win_amd64.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\mfc140u.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\msvcp140.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\PDFCreator.exe"
File "D:\Alexzander__\PythonApplications\PDFCreator\PDFCreator.exe.manifest"
File "D:\Alexzander__\PythonApplications\PDFCreator\PDFCreator.nsi"
File "D:\Alexzander__\PythonApplications\PDFCreator\PDFCreator.py"
File "D:\Alexzander__\PythonApplications\PDFCreator\pyexpat.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\python3.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\python37.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\pythoncom37.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\pywintypes37.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\recents.json"
File "D:\Alexzander__\PythonApplications\PDFCreator\select.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\ucrtbase.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\unicodedata.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\VCRUNTIME140.dll"
File "D:\Alexzander__\PythonApplications\PDFCreator\win32api.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\win32pdh.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\win32trace.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\win32ui.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\win32wnet.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_asyncio.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_bz2.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_cffi_backend.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_contextvars.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_ctypes.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_curses.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_decimal.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_elementtree.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_hashlib.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_lzma.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_multiprocessing.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_overlapped.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_queue.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_socket.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_ssl.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\_win32sysloader.pyd"
SetOutPath "$INSTDIR\aiohttp"
File "D:\Alexzander__\PythonApplications\PDFCreator\aiohttp\_frozenlist.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\aiohttp\_helpers.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\aiohttp\_http_parser.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\aiohttp\_http_writer.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\aiohttp\_websocket.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\certifi"
File "D:\Alexzander__\PythonApplications\PDFCreator\certifi\cacert.pem"
SetOutPath "$INSTDIR\cryptography\hazmat\bindings"
File "D:\Alexzander__\PythonApplications\PDFCreator\cryptography\hazmat\bindings\_openssl.pyd"
SetOutPath "$INSTDIR\cryptography-3.4.6-py3.7.egg-info"
File "D:\Alexzander__\PythonApplications\PDFCreator\cryptography-3.4.6-py3.7.egg-info\INSTALLER"
File "D:\Alexzander__\PythonApplications\PDFCreator\cryptography-3.4.6-py3.7.egg-info\LICENSE"
File "D:\Alexzander__\PythonApplications\PDFCreator\cryptography-3.4.6-py3.7.egg-info\LICENSE.APACHE"
File "D:\Alexzander__\PythonApplications\PDFCreator\cryptography-3.4.6-py3.7.egg-info\LICENSE.BSD"
File "D:\Alexzander__\PythonApplications\PDFCreator\cryptography-3.4.6-py3.7.egg-info\LICENSE.PSF"
File "D:\Alexzander__\PythonApplications\PDFCreator\cryptography-3.4.6-py3.7.egg-info\METADATA"
File "D:\Alexzander__\PythonApplications\PDFCreator\cryptography-3.4.6-py3.7.egg-info\RECORD"
File "D:\Alexzander__\PythonApplications\PDFCreator\cryptography-3.4.6-py3.7.egg-info\top_level.txt"
File "D:\Alexzander__\PythonApplications\PDFCreator\cryptography-3.4.6-py3.7.egg-info\WHEEL"
SetOutPath "$INSTDIR\cv2"
File "D:\Alexzander__\PythonApplications\PDFCreator\cv2\cv2.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\cv2\opencv_videoio_ffmpeg440_64.dll"
SetOutPath "$INSTDIR\icons"
File "D:\Alexzander__\PythonApplications\PDFCreator\icons\aopsdnjaosjbndajsidasjd.png"
File "D:\Alexzander__\PythonApplications\PDFCreator\icons\exec.ico"
File "D:\Alexzander__\PythonApplications\PDFCreator\icons\pdf1.ico"
File "D:\Alexzander__\PythonApplications\PDFCreator\icons\pdf1.png"
File "D:\Alexzander__\PythonApplications\PDFCreator\icons\pdf2.ico"
File "D:\Alexzander__\PythonApplications\PDFCreator\icons\pdf2.png"
File "D:\Alexzander__\PythonApplications\PDFCreator\icons\pdf3.ico"
File "D:\Alexzander__\PythonApplications\PDFCreator\icons\pdf3.png"
File "D:\Alexzander__\PythonApplications\PDFCreator\icons\pdf4.ico"
File "D:\Alexzander__\PythonApplications\PDFCreator\icons\pdf4.png"
File "D:\Alexzander__\PythonApplications\PDFCreator\icons\scripticon.ico"
File "D:\Alexzander__\PythonApplications\PDFCreator\icons\scripticon.png"
SetOutPath "$INSTDIR\Include"
File "D:\Alexzander__\PythonApplications\PDFCreator\Include\pyconfig.h"
SetOutPath "$INSTDIR\logs"
File "D:\Alexzander__\PythonApplications\PDFCreator\logs\build_27.02.2021__12_54_16.log"
SetOutPath "$INSTDIR\multidict"
File "D:\Alexzander__\PythonApplications\PDFCreator\multidict\_multidict.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\numpy\core"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\core\_multiarray_tests.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\core\_multiarray_umath.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\numpy\fft"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\fft\_pocketfft_internal.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\numpy\linalg"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\linalg\lapack_lite.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\linalg\_umath_linalg.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\numpy\random"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\random\bit_generator.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\random\mtrand.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\random\_bounded_integers.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\random\_common.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\random\_generator.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\random\_mt19937.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\random\_pcg64.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\random\_philox.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\numpy\random\_sfc64.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\PIL"
File "D:\Alexzander__\PythonApplications\PDFCreator\PIL\_imaging.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\PIL\_imagingft.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\PIL\_imagingtk.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\PIL\_webp.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\scipy\fft\_pocketfft"
File "D:\Alexzander__\PythonApplications\PDFCreator\scipy\fft\_pocketfft\pypocketfft.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\scipy\_lib"
File "D:\Alexzander__\PythonApplications\PDFCreator\scipy\_lib\messagestream.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\scipy\_lib\_ccallback_c.cp37-win_amd64.pyd"
File "D:\Alexzander__\PythonApplications\PDFCreator\scipy\_lib\_fpumode.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\scipy\_lib\_uarray"
File "D:\Alexzander__\PythonApplications\PDFCreator\scipy\_lib\_uarray\_uarray.cp37-win_amd64.pyd"
SetOutPath "$INSTDIR\win32com\shell"
File "D:\Alexzander__\PythonApplications\PDFCreator\win32com\shell\shell.pyd"
SetOutPath "$INSTDIR\yarl"
File "D:\Alexzander__\PythonApplications\PDFCreator\yarl\_quoting_c.cp37-win_amd64.pyd"

SectionEnd


######################################################################


Section -Icons_Reg
SetOutPath "$INSTDIR"
WriteUninstaller "$INSTDIR\uninstall_PDFCreator.exe"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
CreateDirectory "$SMPROGRAMS\$SM_Folder"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall_PDFCreator.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!insertmacro MUI_STARTMENU_WRITE_END
!endif

!ifndef REG_START_MENU
CreateDirectory "$SMPROGRAMS\PDFCreator"
CreateShortCut "$SMPROGRAMS\PDFCreator\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\PDFCreator\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall_PDFCreator.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\PDFCreator\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!endif

WriteRegStr ${REG_ROOT} "${REG_APP_PATH}" "" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayName" "${APP_NAME}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "UninstallString" "$INSTDIR\uninstall_PDFCreator.exe"
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

Delete "$INSTDIR\aiohttp\_frozenlist.cp37-win_amd64.pyd"
Delete "$INSTDIR\aiohttp\_helpers.cp37-win_amd64.pyd"
Delete "$INSTDIR\aiohttp\_http_parser.cp37-win_amd64.pyd"
Delete "$INSTDIR\aiohttp\_http_writer.cp37-win_amd64.pyd"
Delete "$INSTDIR\aiohttp\_websocket.cp37-win_amd64.pyd"
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
Delete "$INSTDIR\cv2\cv2.cp37-win_amd64.pyd"
Delete "$INSTDIR\cv2\opencv_videoio_ffmpeg440_64.dll"
Delete "$INSTDIR\icons\aopsdnjaosjbndajsidasjd.png"
Delete "$INSTDIR\icons\exec.ico"
Delete "$INSTDIR\icons\pdf1.ico"
Delete "$INSTDIR\icons\pdf1.png"
Delete "$INSTDIR\icons\pdf2.ico"
Delete "$INSTDIR\icons\pdf2.png"
Delete "$INSTDIR\icons\pdf3.ico"
Delete "$INSTDIR\icons\pdf3.png"
Delete "$INSTDIR\icons\pdf4.ico"
Delete "$INSTDIR\icons\pdf4.png"
Delete "$INSTDIR\icons\scripticon.ico"
Delete "$INSTDIR\icons\scripticon.png"
Delete "$INSTDIR\Include\pyconfig.h"
Delete "$INSTDIR\install_PDFCreator.exe"
Delete "$INSTDIR\libansari.R6EA3HQP5KZ6TAXU4Y4ZVTRPT7UVA53Z.gfortran-win_amd64.dll"
Delete "$INSTDIR\libbanded5x.ESF6LBN6R5UJFVJPSFF43URXBMGC3QEN.gfortran-win_amd64.dll"
Delete "$INSTDIR\libbispeu.7AH3PCQ2E2NGLC3AQD7FFAH73KGJTZCJ.gfortran-win_amd64.dll"
Delete "$INSTDIR\libblkdta00.4WSITLJKIDKQOUHFTTKLQEGVSSFMMZS7.gfortran-win_amd64.dll"
Delete "$INSTDIR\libchkder.G7WSOGIYYQO3UWFVEZ3PPXCXR53ADVPA.gfortran-win_amd64.dll"
Delete "$INSTDIR\libcobyla2.25EVUSEBAW7VKISARB7LO3UGZPN2HXE3.gfortran-win_amd64.dll"
Delete "$INSTDIR\libcrypto-1_1-x64.dll"
Delete "$INSTDIR\libdcsrch.I2AOPDCXAPDRFNPWY55H5UE7XZSU5CVN.gfortran-win_amd64.dll"
Delete "$INSTDIR\libdet.ZR5WBP5EE4H6A2LANGYSEUMRZX2FURDL.gfortran-win_amd64.dll"
Delete "$INSTDIR\libdfft.M3WGVBMYA2L7GTSQSBCA5QKI6BDRF2IU.gfortran-win_amd64.dll"
Delete "$INSTDIR\libdfitpack.TCSQXP62XZEF2TJFDUO4ZNU2JINJ5MPX.gfortran-win_amd64.dll"
Delete "$INSTDIR\libdgamln.HZLYI765YOFRVQOCNKFL5RM2SXIDZ2F6.gfortran-win_amd64.dll"
Delete "$INSTDIR\libdqag.Y76S4TW6JPXNBNXUTVXLMXJ7XT6OMWLT.gfortran-win_amd64.dll"
Delete "$INSTDIR\libd_odr.THQQ64REMK7ZMZRF2IS7Z5IEON7RSLK5.gfortran-win_amd64.dll"
Delete "$INSTDIR\libgetbreak.YQM3SI6KRD7DFG7DL7B6RJEWQS4O6YW3.gfortran-win_amd64.dll"
Delete "$INSTDIR\liblbfgsb.KB47UAMDWJMP5C4XWQK5Y34RR3LKHELH.gfortran-win_amd64.dll"
Delete "$INSTDIR\liblsoda-f2.FIRRCAPSEZOIP3OLBLML4456LCBTH74K.gfortran-win_amd64.dll"
Delete "$INSTDIR\libmvndst.5VXNIPAPINAF5NIHXAFNA4OTHOPNDEWG.gfortran-win_amd64.dll"
Delete "$INSTDIR\libnnls.4HUTGAJQTI623WTX372VAIIWXRLC62YU.gfortran-win_amd64.dll"
Delete "$INSTDIR\libopenblas.3HBPCJB5BPQGKWVZAVEBXNNJ2Q2G3TUP.gfortran-win_amd64.dll"
Delete "$INSTDIR\libopenblas.NOIJJG62EMASZI6NYURL6JBKM4EVBGM7.gfortran-win_amd64.dll"
Delete "$INSTDIR\libslsqp_op.RGGN6ZOFD2K47X7YRNDYCM7JFP4AGLER.gfortran-win_amd64.dll"
Delete "$INSTDIR\libspecfun.LQCTHMCYNULEOOGKIO6AGREE6D6V37RU.gfortran-win_amd64.dll"
Delete "$INSTDIR\libssl-1_1-x64.dll"
Delete "$INSTDIR\libvode-f2p.6FM2HIVOTF5QYRFPB7NAXVUGSWK7BJAT.gfortran-win_amd64.dll"
Delete "$INSTDIR\libwrap_dum.E2DMRP662KYHKE5OXJQOLMJBUYPRL4WK.gfortran-win_amd64.dll"
Delete "$INSTDIR\libwrap_dum.PULJDUMZZKIM7OUS2TIYPZE4PPPRMQA2.gfortran-win_amd64.dll"
Delete "$INSTDIR\lib_arpack-.7TQXDBTMUFOO5AB4ZKS2WPRZAGXNAPTE.gfortran-win_amd64.dll"
Delete "$INSTDIR\lib_blas_su.X3MTOIZ5PXAH5LOTFDAJVXR3245XHGNP.gfortran-win_amd64.dll"
Delete "$INSTDIR\lib_dop-f2p.H5ICLGM4NKU5EDEIUJIKVMQ6YNOF7IZ6.gfortran-win_amd64.dll"
Delete "$INSTDIR\lib_test_fo.JF5HTWMUPBXWGAYEBVEJU3OZAHTSVKCT.gfortran-win_amd64.dll"
Delete "$INSTDIR\logs\build_27.02.2021__12_54_16.log"
Delete "$INSTDIR\mfc140u.dll"
Delete "$INSTDIR\msvcp140.dll"
Delete "$INSTDIR\multidict\_multidict.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\core\_multiarray_tests.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\core\_multiarray_umath.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\fft\_pocketfft_internal.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\linalg\lapack_lite.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\linalg\_umath_linalg.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\bit_generator.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\mtrand.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_bounded_integers.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_common.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_generator.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_mt19937.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_pcg64.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_philox.cp37-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_sfc64.cp37-win_amd64.pyd"
Delete "$INSTDIR\PDFCreator.exe"
Delete "$INSTDIR\PDFCreator.exe.manifest"
Delete "$INSTDIR\PDFCreator.nsi"
Delete "$INSTDIR\PDFCreator.py"
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
Delete "$INSTDIR\scipy\fft\_pocketfft\pypocketfft.cp37-win_amd64.pyd"
Delete "$INSTDIR\scipy\_lib\messagestream.cp37-win_amd64.pyd"
Delete "$INSTDIR\scipy\_lib\_ccallback_c.cp37-win_amd64.pyd"
Delete "$INSTDIR\scipy\_lib\_fpumode.cp37-win_amd64.pyd"
Delete "$INSTDIR\scipy\_lib\_uarray\_uarray.cp37-win_amd64.pyd"
Delete "$INSTDIR\select.pyd"
Delete "$INSTDIR\ucrtbase.dll"
Delete "$INSTDIR\unicodedata.pyd"
Delete "$INSTDIR\VCRUNTIME140.dll"
Delete "$INSTDIR\win32api.pyd"
Delete "$INSTDIR\win32com\shell\shell.pyd"
Delete "$INSTDIR\win32pdh.pyd"
Delete "$INSTDIR\win32trace.pyd"
Delete "$INSTDIR\win32ui.pyd"
Delete "$INSTDIR\win32wnet.pyd"
Delete "$INSTDIR\yarl\_quoting_c.cp37-win_amd64.pyd"
Delete "$INSTDIR\_asyncio.pyd"
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
Delete "$INSTDIR\_overlapped.pyd"
Delete "$INSTDIR\_queue.pyd"
Delete "$INSTDIR\_socket.pyd"
Delete "$INSTDIR\_ssl.pyd"
Delete "$INSTDIR\_win32sysloader.pyd"


RmDir "$INSTDIR\cryptography\hazmat\bindings"
RmDir "$INSTDIR\scipy\fft\_pocketfft"
RmDir "$INSTDIR\scipy\_lib\_uarray"
RmDir "$INSTDIR\cryptography\hazmat"
RmDir "$INSTDIR\numpy\core"
RmDir "$INSTDIR\numpy\fft"
RmDir "$INSTDIR\numpy\linalg"
RmDir "$INSTDIR\numpy\random"
RmDir "$INSTDIR\scipy\fft"
RmDir "$INSTDIR\scipy\_lib"
RmDir "$INSTDIR\win32com\shell"
RmDir "$INSTDIR\aiohttp"
RmDir "$INSTDIR\certifi"
RmDir "$INSTDIR\cryptography"
RmDir "$INSTDIR\cryptography-3.4.6-py3.7.egg-info"
RmDir "$INSTDIR\cv2"
RmDir "$INSTDIR\icons"
RmDir "$INSTDIR\Include"
RmDir "$INSTDIR\logs"
RmDir "$INSTDIR\multidict"
RmDir "$INSTDIR\numpy"
RmDir "$INSTDIR\PIL"
RmDir "$INSTDIR\scipy"
RmDir "$INSTDIR\win32com"
RmDir "$INSTDIR\yarl"



Delete "$INSTDIR\uninstall_PDFCreator.exe"
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
Delete "$SMPROGRAMS\PDFCreator\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\PDFCreator\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\PDFCreator\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\PDFCreator"
!endif

DeleteRegKey ${REG_ROOT} "${REG_APP_PATH}"
DeleteRegKey ${REG_ROOT} "${UNINSTALL_PATH}"
SectionEnd