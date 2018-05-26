
from GsDict.Library import Reader
fonts = Reader.list_fonts()
print(fonts)

defset = []

for font in fonts:
    result = Reader.load_font(font)
    defset.append(result)

for ss, font in enumerate(defset, 1):
    print(ss, font.data)
