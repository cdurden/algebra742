TEX_FILES := $(wildcard *.tex)
PNG_FILES := $(TEX_FILES:.tex=.png)

png: $(PNG_FILES)
%.png: %.tex
	cd tex
	pdflatex -shell-escape $<

all: tex
