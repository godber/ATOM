
all: presentation

presentation: python-testing.rst screen.json
	rst2pdf -b1 -s screen.json python-testing.rst

html: python-testing.rst
	rst2html python-testing.rst > python-testing.html

clean:
	rm python-testing.pdf python-testing.html
