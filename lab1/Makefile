FILES=getting-started-sbc.pdf
FILES+=browser-based-ui.pdf
FILES+=preparing-new-sd-card.pdf

PANDOCFLAGS=--toc --number-sections --pdf-engine=xelatex\
         -V mainfont='Fira Sans' \
         -V geometry:margin=1in  -V colorlinks=true -V linkcolor=blue -V urlcolor=teal -V toccolor=purple \
         --listings -H ../style/listings-setup.tex -H ../style/keystroke-setup.tex -H ../style/includes.tex 

%.pdf: %.md
	pandoc $^ $(PANDOCFLAGS) -o $@ 

all: $(FILES)

clean: 
	rm -f *.pdf
