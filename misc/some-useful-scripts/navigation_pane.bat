@echo off

:: Script to add or remove a folder to the Windows Explorer navigation pane
:: Originally from https://stackoverflow.com/a/34595293
:: Last Modified: 2025-01-23

:: Check if the correct number of arguments is provided
if "%~1"=="" (
    echo Error: Missing action argument.
    call :print_usage
    exit /b 1
)

if "%~2"=="" (
    echo Error: Missing folder path argument.
    call :print_usage
    exit /b 1
)

:: Check if the action argument is valid
if /i not "%~1"=="add" if /i not "%~1"=="remove" (
    echo Error: Invalid action argument. Must be "add" or "remove".
    call :print_usage
    exit /b 1
)

:: Check if the folder path exists
if not exist "%~2" (
    echo Error: The specified folder path does not exist.
    exit /b 1
)

:: Define the directory to store GUID files
set "guid_dir=%APPDATA%\NavigationPaneGUIDs"

:: Create the directory if it doesn't exist
if not exist "%guid_dir%" (
    mkdir "%guid_dir%"
)

set "action=%~1"
set "folder_path=%~2"
for %%I in ("%folder_path%") do set "folder_name=%%~nxI"

set "guid_file=%guid_dir%\%folder_name%.guid"

if /i "%action%"=="add" (
    echo Adding folder to navigation pane...
    :: Generate a unique GUID in uppercase and enclose it in curly brackets
    echo Generating a unique GUID...
    :generate_guid
    for /f "delims=" %%I in ('powershell -command "[guid]::NewGuid().ToString().ToUpper()"') do set "clsid={%%I}"
    reg query HKCU\Software\Classes\CLSID\%clsid% >nul 2>&1
    if %errorlevel%==0 goto generate_guid

    echo Saving the GUID to a file...
    echo %clsid% > "%guid_file%"
    echo GUID file saved at: %guid_file%

    echo Adding CLSID registry key...
    reg add HKCU\Software\Classes\CLSID\%clsid% /ve /t REG_SZ /d "%folder_name%" /f

    echo Adding DefaultIcon registry key...
    reg add HKCU\Software\Classes\CLSID\%clsid%\DefaultIcon /ve /t REG_EXPAND_SZ /d %%SystemRoot%%\system32\imageres.dll,-3 /f

    echo Setting System.IsPinnedToNameSpaceTree...
    reg add HKCU\Software\Classes\CLSID\%clsid% /v System.IsPinnedToNameSpaceTree /t REG_DWORD /d 0x1 /f

    echo Setting SortOrderIndex...
    reg add HKCU\Software\Classes\CLSID\%clsid% /v SortOrderIndex /t REG_DWORD /d 0x42 /f

    echo Adding InProcServer32 registry key...
    reg add HKCU\Software\Classes\CLSID\%clsid%\InProcServer32 /ve /t REG_EXPAND_SZ /d %%systemroot%%\system32\shell32.dll /f

    echo Adding Instance CLSID...
    reg add HKCU\Software\Classes\CLSID\%clsid%\Instance /v CLSID /t REG_SZ /d {0E5AAE11-A475-4c5b-AB00-C66DE400274E} /f

    echo Setting InitPropertyBag Attributes...
    reg add HKCU\Software\Classes\CLSID\%clsid%\Instance\InitPropertyBag /v Attributes /t REG_DWORD /d 0x11 /f

    echo Setting TargetFolderPath...
    reg add HKCU\Software\Classes\CLSID\%clsid%\Instance\InitPropertyBag /v TargetFolderPath /t REG_EXPAND_SZ /d "%folder_path%" /f

    echo Setting ShellFolder FolderValueFlags...
    reg add HKCU\Software\Classes\CLSID\%clsid%\ShellFolder /v FolderValueFlags /t REG_DWORD /d 0x28 /f

    echo Setting ShellFolder Attributes...
    reg add HKCU\Software\Classes\CLSID\%clsid%\ShellFolder /v Attributes /t REG_DWORD /d 0xF080004D /f

    echo Adding NameSpace registry key...
    reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Desktop\NameSpace\%clsid% /ve /t REG_SZ /d "%folder_name%" /f

    echo Adding HideDesktopIcons registry value...
    reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel /v %clsid% /t REG_DWORD /d 0x1 /f

    echo Folder added successfully.
    exit /b
) else if /i "%action%"=="remove" (
    echo Removing folder from navigation pane...
    if not exist "%guid_file%" (
        echo GUID file not found for folder: %folder_name%
        exit /b 1
    )
    set /p clsid=<"%guid_file%"
    echo %clsid%
    echo Deleting CLSID registry key...
    reg delete HKCU\Software\Classes\CLSID\%clsid% /f

    echo Deleting NameSpace registry key...
    reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Desktop\NameSpace\%clsid% /f

    echo Deleting HideDesktopIcons registry value...
    reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel /v %clsid% /f

    echo Deleting GUID file...
    del "%guid_file%"

    echo Folder removed successfully.
    exit /b
) else (
    echo Invalid action: %action%
    call :print_usage
)

:print_usage
echo "Usage: %~nx0 [add|remove] folder_path"
echo.
echo add    - Adds the specified folder to the navigation pane.
echo remove - Removes the specified folder from the navigation pane.
echo folder_path - The full path to the folder to add or remove.
echo.
echo Examples:
echo %~nx0 add "C:\Users\YourUsername\Documents\MyFolder"
echo %~nx0 remove "C:\Users\YourUsername\Documents\MyFolder"
exit /b