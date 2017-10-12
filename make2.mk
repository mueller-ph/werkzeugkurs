master.pdf: master.tex figure-1.png figure-2.png
	pdflatex $<
figure-1.png : summary-1.dat
	python myplot.py $^ $@ 
figure-2.png : summary-2.dat
	python myplot.py $^ $@ 
summary-1.dat: data-1-*.dat 
	python myanalysis.py $@ $^
summary-2.dat: data-2-*.dat 
	python myanalysis.py $@ $^
summary-1.dat : myanalysis.py
summary-2.dat : myanalysis.py
