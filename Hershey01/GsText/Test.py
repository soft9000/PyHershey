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
