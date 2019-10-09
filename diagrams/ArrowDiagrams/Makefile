TEX_FILES := $(wildcard tex/*.tex)
PNG_FILES := $(addprefix pdf/, $(SOURCE_DOCS:.tex=.png))
tex:
	sh build.sh

png: $(PNG_FILES)
%.png: tex/%.tex
	cd tex
	pdflatex -shell-escape $<

all: tex
