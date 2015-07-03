
all:
	pdflatex DFilippova_thesis
	bibtex DFilippova_thesis
	pdflatex DFilippova_thesis
	pdflatex DFilippova_thesis

quick:
	pdflatex DFilippova_thesis
clean:
	rm *.bbl
	rm *.aux
	rm *.blg
	rm *.brf
	rm *.log
	rm *.log
	rm *.lot
	rm *.out
	rm *.toc
