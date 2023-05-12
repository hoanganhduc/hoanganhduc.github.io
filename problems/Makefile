# define the path to your Jekyll blog source by `export HOMEPAGE_SRC=/path/to/your/jekyll/blog/source`
STATIC_DIR="$(HOMEPAGE_SRC)/static"
#BLOG_DIR="$(HOMEPAGE_SRC)/problems"

all: pdf html clean

html: main.html

%.html: %.tex refs.bib
	@latexml --destination=$(basename $(@F)).xml --noparse $<
	@if [ -d "_XSLT" ]; then \
		latexmlpost --destination=$@ --nodefaultresources --format=html5 --nosplit --stylesheet="./_XSLT/LaTeXML-jekyll-post.xsl" $(basename $(@F)).xml ; \
	else \
		latexmlpost --destination=$@ --nodefaultresources --format=html5 --nosplit --stylesheet="$(STATIC_DIR)/_XSLT/LaTeXML-jekyll-post.xsl" $(basename $(@F)).xml ; \
	fi
	@touch -r main.html index.md
	#@find . -type f -name "*.png" -exec rsync -aRv {} $(BLOG_DIR)/a-latexml-demo/ \;

pdf: main.pdf

%.pdf: %.tex refs.bib
	@latexmk -pdf $<
	#@if [ -d $(BLOG_DIR) ]; then \
	#	cp -vp $@ $(BLOG_DIR)/a-latexml-demo/ ; \
	#fi

clean:
	@latexmk -c
	@rm -rf LaTeXML.cache *.bbl *.dvi *.log *.bak *.aux *.blg *.idx *.toc *.out *.snm *.nav *.xml *.bcf *.spl *.synctex.gz *-eps-converted-to.pdf *~

# archive:
	# @if [ -d $(STATIC_DIR) ]; then \
		# zip -u -r $(BLOG_DIR)/a-latexml-demo/main.zip ./ || \
		# if [[ $$? -eq 12 ]]; then exit 0; fi ; \
		# cd $(STATIC_DIR) && zip -u -r $(BLOG_DIR)/a-latexml-demo/main.zip _XSLT || \
		# if [[ $$? -eq 12 ]]; then exit 0; fi ; \
	# else \
		# zip -u -r main.zip ./ || \
		# if [[ $$? -eq 12 ]]; then exit 0; fi ; \
	# fi
