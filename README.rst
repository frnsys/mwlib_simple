.. -*- mode: rst; coding: utf-8 -*-

======================================================================
mwlib - MediaWiki parser and utility library
======================================================================


About This Fork/Branch
======================================================================
mwlib does not yet officially support Python 3. This branch is a more
lightweight version I have ported to Python 3 (I did not include
any backwards compatibility). I have tried to include only the Wikimedia
markup parsing functionality – that is the only functionality I needed,
and I didn't want to port the entire library. It's mainly meant to be
a substitute until the official library is ported over.


Overview
======================================================================
mwlib provides a library for parsing MediaWiki articles and
converting them to different output formats. mwlib is used by
wikipedia's "Print/export" feature in order to generate PDF documents
from wikipedia articles.

Documentation
=================
Please visit http://mwlib.readthedocs.org/en/latest/index.html for
detailed documentation.

License
======================================================================
Copyright (c) 2007-2012 PediaPress GmbH

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above
  copyright notice, this list of conditions and the following
  disclaimer in the documentation and/or other materials provided
  with the distribution. 

* Neither the name of PediaPress GmbH nor the names of its
  contributors may be used to endorse or promote products derived
  from this software without specific prior written permission. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

.. _SpamBayes: http://spambayes.sourceforge.net/
