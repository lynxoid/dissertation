
all:
	pdflatex DFilippova_thesis
	bibtex DFilippova_thesis
	pdflatex DFilippova_thesis
	pdflatex DFilippova_thesis

quick:
	pdflatex DFilippova_thesis
clean:
	rm -f *.bbl
	rm -f *.aux
	rm -f *.blg
	rm -f *.brf
	rm -f *.log
	rm -f *.lot
	rm -f *.lof
	rm -f *.out
	rm -f *.toc