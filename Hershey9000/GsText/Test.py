# MISSION: The new vector font library for Modern Python.
# STATUS: Public Release
# VERSION: 1.1.0
# NOTES: See https://github.com/soft9000/PyHershey
# DATE: 2023-06-25 12:12:10
# FILE: Test.py
# AUTHOR: See https://ko-fi.com/randallnagy
#

import sys
if '..' not in sys.path:
    sys.path.append('..')
    
from GsText.Reader import Reader
font1 = Reader.load_font('japanese')
print(font1.font_name, font1.font_rect)
for line in font1.data:
    print(line, font1.data[line])
print(font1.data)
print(font1.glyph_count())



from GsDict.Library import Writer
Writer.save_font(font1)



from GsDict.Library import Reader as Reader2
font2 = Reader2.load_font('japanese')
print(font2.glyph_count())
