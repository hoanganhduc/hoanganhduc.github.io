all: pdf html clean

html: main.html

%.html: %.tex refs.bib
	@latexmlc --destination=$(basename $(@F)).xml --noparse $<
	@latexmlpost --destination=$@ --nodefaultresources --format=html5 --nosplit --stylesheet="_XSLT/LaTeXML-jekyll-post.xsl" $(basename $(@F)).xml

pdf: main.pdf

%.pdf: %.tex refs.bib
	@latexmk -pdf $<
	@cp -vp $@ ../../static/posts/a-latexml-demo/

clean:
	@latexmk -c
	@rm -rf LaTeXML.cache *.bbl *.dvi *.log *.bak *.aux *.blg *.idx *.ps *.eps *.toc *.out *.snm *.nav *.xml *.bcf *.spl *.synctex.gz *~

archive:
	@zip -u -r ../../static/posts/a-latexml-demo/main.zip ./ || \
		if [[ $$? -eq 12 ]]; then exit 0; fi
	@cd ../../ && zip -u -r ./static/posts/a-latexml-demo/main.zip _XSLT || \
		if [[ $$? -eq 12 ]]; then exit 0; fi
