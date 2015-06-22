
all:
	pdflatex DFilippova_thesis
	bibtex DFilippova_thesis
	pdflatex DFilippova_thesis
	pdflatex DFilippova_thesis

quick:
	pdflatex DFilippova_thesis