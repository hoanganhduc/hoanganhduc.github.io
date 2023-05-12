@echo off

set HOMEPAGE_SRC="%USERPROFILE%\Dropbox\personal-webpage"
set STATIC_DIR="%HOMEPAGE_SRC%\static"

:loop
IF "%~1"=="" GOTO all
IF "%~1"=="pdf" GOTO pdf
IF "%~1"=="html" GOTO html
IF "%~1"=="clean" GOTO clean
GOTO loop

:all
"%~0" pdf && "%~0" html && "%~0" clean
GOTO:EOF

:pdf
latexmk -pdf main.tex
GOTO:EOF

:html
latexml --destination=main.xml --noparse main.tex
latexmlpost --destination=main.html --nodefaultresources --format=html5 --nosplit --stylesheet="%STATIC_DIR%\_XSLT\LaTeXML-jekyll-post.xsl" main.xml
GOTO:EOF

:clean
latexmk -c
del LaTeXML.cache *.bbl *.dvi *.log *.bak *.aux *.blg *.idx *.toc *.out *.snm *.nav *.xml *.bcf *.spl *.synctex.gz *-eps-converted-to.pdf *~
GOTO:EOF