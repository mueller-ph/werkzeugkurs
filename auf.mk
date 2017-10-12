all : list.txt end.pdf

list.txt : *.py
	@echo off ls $^ | sort > $@

end.pdf : out.tex
	pdflatex $<


