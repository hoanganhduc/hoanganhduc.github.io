# Define the title of the project
TITLE="Template"

# Define the directory for Overleaf synchronization
OVERLEAF_DIR="$(HOME)/Dropbox/Apps/Overleaf/$(TITLE)"

# Get the current working directory
WORK_DIR="$(PWD)"

# Default target to build the main PDF
all: main.pdf

# Rule to build a PDF from a .tex file and a bibliography file
%.pdf: %.tex refs.bib
	@latexmk $<
	@latexmk -c >/dev/null
	
# Clean up auxiliary files generated during the build process
clean:
	@rm -rf *.bbl *.dvi *.log *.bak *.aux *.blg *.idx *.ps *.toc *.out *.snm *.nav *.xml *.bcf *.spl *.synctex.gz *~ *.aux *.blg *.fdb_latexmk *.fls *.log*.synctex* *-blx.bib >/dev/null
	@echo "Junk files removed"
	
# Clean up all files except the main PDF and main ZIP
clean-all:
	@find ./ -mindepth 1 -maxdepth 1 ! -name "main.pdf" ! -name "main.zip" -exec rm -rf {} \;

# Remove comments from the main.tex file
remove-comments:
	## Removing comments
	@cp -vp main.tex main-backup.tex
	@latexpand --empty-comments main.tex > main-stripped.tex
	@sed -i '/^\s*%/d' main-stripped.tex
	@cp -vp main-stripped.tex main.tex
	@rm -rf main-stripped.tex

# Create a ZIP archive of the project
archive: main.zip

%.zip: %.tex ./*
	#@$(MAKE) remove-comments
	@zip -u -r $@ ./* -x "*.zip" -x "main.pdf" -x "*.synctex.gz" -x "*.bbl" -x "main-*.tex" || \
		if [[ $$? -eq 12 ]]; then echo "Nothing to update"; exit 0; fi
	#@cp -vp main-backup.tex main.tex >/dev/null
	#@rm -rf main-backup.tex >/dev/null

# Synchronize the project with Overleaf
overleaf:
	@$(MAKE) clean
	@echo "Updating Overleaf" && rsync -arv --delete --exclude-from=exclude.txt $(WORK_DIR)/ $(OVERLEAF_DIR)
	
# Update the local project with changes from Overleaf
update:
	@rsync -arv $(OVERLEAF_DIR)/ $(WORK_DIR)