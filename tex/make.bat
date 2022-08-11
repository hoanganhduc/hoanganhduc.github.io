@echo off

set NAME="main"
set ARCHIVE_NAME="main"

:loop
IF "%~1"=="" GOTO all
IF "%~1"=="archive" GOTO archive
IF "%~1"=="remove-comments" GOTO remove-comments
IF "%~1"=="clean" GOTO clean
GOTO loop

:all
latexmk %NAME%
latexmk -c
GOTO:EOF

:archive
zip -u -r --exclude="*.zip" --exclude "*.synctex.gz" --exclude "*.bbl" --exclude="%NAME%.pdf" --exclude="%NAME%-*.tex" "%ARCHIVE_NAME%.zip" ./
GOTO:EOF

:clean
latexmk -c
del /F *.bbl *.dvi *.log *.bak *.aux *.blg *.idx *.ps *.toc *.out *.snm *.nav *.xml *.bcf *.spl *.synctex.gz *~ *.aux *.blg *.fdb_latexmk *.fls *.log*.synctex* *-blx.bib
echo "Junk files removed"
GOTO:EOF

:: Require sed for windows @ https://github.com/mbuilov/sed-windows
:remove-comments
xcopy /Y /F main.tex main-backup.tex*
latexpand --empty-comments main.tex --output main-stripped.tex
sed -i "/^\s*%%/d" main-stripped.tex
xcopy /Y /F main-stripped.tex main.tex*
del /F main-stripped.tex
echo "Comments in main.tex removed. See the original file main-backup.tex"
GOTO:EOF
