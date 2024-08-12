TITLE="Template"
OVERLEAF_DIR="$(HOME)/Dropbox/Apps/Overleaf/$(TITLE)"
DATE := $(shell date +%Y%m%d)
WORK_DIR="$(PWD)"

all: main.pdf

%.pdf: %.tex refs.bib
	@latexmk $<
	@latexmk -c >/dev/null
	
clean:
	@rm -rf *.bbl *.dvi *.log *.bak *.aux *.blg *.idx *.ps *.toc *.out *.snm *.nav *.xml *.bcf *.spl *.synctex.gz *~ *.aux *.blg *.fdb_latexmk *.fls *.log*.synctex* *-blx.bib >/dev/null
	@echo "Junk files removed"
	
clean-all:
	@find ./ -mindepth 1 -maxdepth 1 ! -name "main.pdf" ! -name "main.zip" -exec rm -rf {} \;

remove-comments:
	## Removing comments
	@cp -vp main.tex main-backup.tex
	@latexpand --empty-comments main.tex > main-stripped.tex
	@sed -i '/^\s*%/d' main-stripped.tex
	@cp -vp main-stripped.tex main.tex
	@rm -rf main-stripped.tex

archive: main.zip

%.zip: %.tex ./*
	#@$(MAKE) remove-comments
	@zip -u -r $@ ./* -x "*.zip" -x "main.pdf" -x "*.synctex.gz" -x "*.bbl" -x "main-*.tex" || \
		if [[ $$? -eq 12 ]]; then echo "Nothing to update"; exit 0; fi
	#@cp -vp main-backup.tex main.tex >/dev/null
	#@rm -rf main-backup.tex >/dev/null

overleaf:
	@$(MAKE) clean
	@echo "Updating Overleaf" && rsync -arv --delete --exclude-from=exclude.txt $(WORK_DIR)/ $(OVERLEAF_DIR)
	
update:
	@rsync -arv $(OVERLEAF_DIR)/ $(WORK_DIR)