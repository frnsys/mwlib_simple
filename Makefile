all:: uscan cython MANIFEST.in

uscan:: mwlib/_uscan.re
	re2c -w --no-generation-date -o mwlib/_uscan.cc mwlib/_uscan.re

cython:: mwlib/templ/nodes.c mwlib/templ/evaluate.c

mwlib/templ/nodes.c: mwlib/templ/nodes.py
	cython mwlib/templ/nodes.py

mwlib/templ/evaluate.c: mwlib/templ/evaluate.py
	cython mwlib/templ/evaluate.py

MANIFEST.in::
	./make-manifest