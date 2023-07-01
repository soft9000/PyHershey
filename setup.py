# Works, yet beta.toml over-installs the .gsdict files?
#
from __future__ import unicode_literals
from distutils.core import setup
from setuptools import find_packages, find_namespace_packages

# from glob import glob as glob
# aFiles = glob("Hershey01//GsDict//*.gsdict")

# defer to README.md:
long_description= '''
THE DEMO
========
To enjoy the line x line rendering
of Hershey's amazingly cool font set:

>> import Hershey01

FONT DEMO
=========
To use the fonts in your project,
review TurtleShow.py and / or check
the project doc at the download location.

FONT PDF
========
In addition to re-using my code you
might also like to review the .PDFs:

https://github.com/soft9000/The-Book-of-Glyphs/tree/master/TheHersheyFonts
'''

aFiles = [
    "Hershey01/GsDict/astrology.gsdict",
    "Hershey01/GsDict/cursive.gsdict",
    "Hershey01/GsDict/cyrilc_1.gsdict",
    "Hershey01/GsDict/cyrillic.gsdict",
    "Hershey01/GsDict/futural.gsdict",
    "Hershey01/GsDict/futuram.gsdict",
    "Hershey01/GsDict/gothgbt.gsdict",
    "Hershey01/GsDict/gothgrt.gsdict",
    "Hershey01/GsDict/gothiceng.gsdict",
    "Hershey01/GsDict/gothicger.gsdict",
    "Hershey01/GsDict/gothicita.gsdict",
    "Hershey01/GsDict/gothitt.gsdict",
    "Hershey01/GsDict/greek.gsdict",
    "Hershey01/GsDict/greekc.gsdict",
    "Hershey01/GsDict/greeks.gsdict",
    "Hershey01/GsDict/japanese.gsdict",
    "Hershey01/GsDict/markers.gsdict",
    "Hershey01/GsDict/mathlow.gsdict",
    "Hershey01/GsDict/mathupp.gsdict",
    "Hershey01/GsDict/meteorology.gsdict",
    "Hershey01/GsDict/music.gsdict",
    "Hershey01/GsDict/rowmand.gsdict",
    "Hershey01/GsDict/rowmans.gsdict",
    "Hershey01/GsDict/rowmant.gsdict",
    "Hershey01/GsDict/scriptc.gsdict",
    "Hershey01/GsDict/scripts.gsdict",
    "Hershey01/GsDict/symbolic.gsdict",
    "Hershey01/GsDict/timesg.gsdict",
    "Hershey01/GsDict/timesi.gsdict",
    "Hershey01/GsDict/timesib.gsdict",
    "Hershey01/GsDict/timesr.gsdict",
    "Hershey01/GsDict/timesrb.gsdict"
    ]

zFiles = [
    ('Hershey01/GsDict',aFiles)
    ]

setup(name='Hershey01',
      author="Randall Nagy",
      description="Font Set -w- Vector Viewer",
      author_email="r.a.nagy@gmail.com",
      url="http://soft9000.com",
      download_url="https://github.com/soft9000/PyHershey",
      platforms="Turtle Graphics Required",
      packages=find_namespace_packages(),
      data_files=zFiles)
