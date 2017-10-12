# phony.mk
all : figure-1.png figure-2.png

figure-1.png : summary-1.dat
	python myplot.py summary-1.dat figure-1.png
figure-2.png : summary-2.dat
	python myplot.py summary-2.dat figure-2.png
