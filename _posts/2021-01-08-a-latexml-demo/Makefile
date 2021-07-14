STATIC_FOLDER="../../static"

all: pdf html clean

html: main.html

%.html: %.tex refs.bib
	@latexmlc --destination=$(basename $(@F)).xml --noparse $<
	@if [ -d "_XSLT" ]; then \
		latexmlpost --destination=$@ --nodefaultresources --format=html5 --nosplit --stylesheet="./_XSLT/LaTeXML-jekyll-post.xsl" $(basename $(@F)).xml ; \
	else \
		latexmlpost --destination=$@ --nodefaultresources --format=html5 --nosplit --stylesheet="$(STATIC_FOLDER)/_XSLT/LaTeXML-jekyll-post.xsl" $(basename $(@F)).xml ; \
	fi

pdf: main.pdf

%.pdf: %.tex refs.bib
	@latexmk -pdf $<
	@cp -vp $@ $(STATIC_FOLDER)/posts/a-latexml-demo/

clean:
	@latexmk -c
	@rm -rf LaTeXML.cache *.bbl *.dvi *.log *.bak *.aux *.blg *.idx *.ps *.eps *.toc *.out *.snm *.nav *.xml *.bcf *.spl *.synctex.gz *~

archive:
	@zip -u -r $(STATIC_FOLDER)/posts/a-latexml-demo/main.zip ./ || \
		if [[ $$? -eq 12 ]]; then exit 0; fi
	@cd $(STATIC_FOLDER) && zip -u -r ./posts/a-latexml-demo/main.zip $(STATIC_FOLDER)/_XSLT || \
		if [[ $$? -eq 12 ]]; then exit 0; fi
