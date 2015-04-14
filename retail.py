#!/usr/bin/env python

# Author: Matthew Mole <code@gairne.co.uk>
# This program is released under the GNU General Public License Version 3

# Cards Against Humanity is a card game produced by Cards Against Humanity LLC and is released under a Creative Commons BY-NC-SA 2.0 license
# Information is available at https://cardsagainsthumanity.com/

import subprocess, os

from genCards import createCards
#createCards(inputFile, outputDir, prefix="", offset=1, verbose=False)

createCards(os.getcwd() + "/sample/retail.csv", os.getcwd() + "/generated/retail/", "retail-", 1, True)