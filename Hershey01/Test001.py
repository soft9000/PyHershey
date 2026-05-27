# MISSION: Review the work of Dr. Allen Vincent Hershey using Modern Python.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: See https://github.com/soft9000/PyHershey
# DATE: 2023-06-25 12:12:10
# FILE: Test001.py
# AUTHOR: See https://ko-fi.com/randallnagy
#

from GsDict.Library import Reader
fonts = Reader.list_fonts()
print(fonts)

defset = []

for font in fonts:
    result = Reader.load_font(font)
    defset.append(result)

for ss, font in enumerate(defset, 1):
    print(ss, font.data)
