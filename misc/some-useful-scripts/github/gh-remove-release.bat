@echo off
setlocal enabledelayedexpansion

REM Check if GitHub CLI is installed
gh --version >nul 2>&1
if errorlevel 1 (
    echo GitHub CLI is not installed. Please install it first.
    exit /b 1
)

REM Get repository input from argument
if "%~1"=="" (
    echo Usage: %~nx0 owner/repo
    exit /b 1
)
set "repo=%~1"

REM Verify the repository input
gh repo view %repo% >nul 2>&1
if errorlevel 1 (
    echo Invalid repository: %repo%
    exit /b 1
)

REM Fetch releases using GitHub API
echo Fetching releases for %repo%...
set count=0
for /f "tokens=* usebackq" %%i in (`gh api repos/%repo%/releases --paginate --jq ".[].tag_name"`) do (
    set /a count+=1
    set "release[!count!]=%%i"
    echo !count!. %%i
)

if !count! equ 0 (
    echo No releases found for %repo%.
) else (
    REM Ask user for input
    set /p choice="Enter the numbers of the releases you want to delete (comma-separated, 'all' to delete all, or press Enter to skip): "

    if not "!choice!"=="" (
        if /i "!choice!" equ "all" (
            for /l %%i in (1,1,!count!) do (
                echo Deleting release !release[%%i]!...
                gh api --silent repos/%repo%/releases/tags/!release[%%i]! -X DELETE
                echo Deleting corresponding tag !release[%%i]!...
                gh api --silent repos/%repo%/git/refs/tags/!release[%%i]! -X DELETE
            )
        ) else (
            for %%i in (!choice!) do (
                echo Deleting release !release[%%i]!...
                gh api --silent repos/%repo%/releases/tags/!release[%%i]! -X DELETE
                echo Deleting corresponding tag !release[%%i]!...
                gh api --silent repos/%repo%/git/refs/tags/!release[%%i]! -X DELETE
            )
        )
    )
)

@REM REM Fetch remaining tags using GitHub API
@REM echo Fetching tags for %repo%...
@REM set count=0
@REM for /f "tokens=* usebackq" %%i in (`gh api repos/%repo%/tags --paginate --jq ".[].name"`) do (
@REM     set /a count+=1
@REM     set "tag[!count!]=%%i"
@REM     echo !count!. %%i
@REM )

@REM if !count! equ 0 (
@REM     echo No tags found for %repo%.
@REM ) else (
@REM     REM Ask user for input
@REM     set /p choice="Enter the numbers of the tags you want to delete (comma-separated, 'all' to delete all, or press Enter to skip): "

@REM     if not "!choice!"=="" (
@REM         if /i "!choice!" equ "all" (
@REM             for /l %%i in (1,1,!count!) do (
@REM                 echo Deleting tag !tag[%%i]!...
@REM                 gh api --silent repos/%repo%/git/refs/tags/!tag[%%i]! -X DELETE
@REM             )
@REM         ) else (
@REM             for %%i in (!choice!) do (
@REM                 echo Deleting tag !tag[%%i]!...
@REM                 gh api --silent repos/%repo%/git/refs/tags/!tag[%%i]! -X DELETE
@REM             )
@REM         )
@REM     )
@REM )

echo Done.
endlocal
