SOURCES=getting-started-sbc.md
SOURCES+=browser-based-ui.md
SOURCES+=preparing-new-sd-card.md
SOURCES = $(wildcard *.md)

PANDOCFLAGS=--toc --number-sections --pdf-engine=xelatex\
         -V mainfont='Fira Sans' \
         -V geometry:margin=1in  -V colorlinks=true -V linkcolor=blue -V urlcolor=teal -V toccolor=purple \
         --listings -H ../style/listings-setup.tex -H ../style/keystroke-setup.tex -H ../style/includes.tex 

PDFS := $(patsubst %.md,%.pdf,$(SOURCES))
PAGES:=  $(patsubst %.md, %.html,$(SOURCES))

%.pdf: %.md
	pandoc $^ $(PANDOCFLAGS) -o $@ 

%.html: %.md
	cat $^ | sed '/newpage/d' > $^.tmp
	pandoc -s -t html5 --mathjax -o $@ $^.tmp -c ../style/pandoc.css
	rm $^.tmp

all: $(PDFS) $(PAGES)

clean: 
	rm -f *.pdf
