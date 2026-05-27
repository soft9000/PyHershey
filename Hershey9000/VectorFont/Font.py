# MISSION: Use the converted data in Modern Python.
# STATUS: Public Release
# VERSION: 1.1.0
# NOTES: See https://github.com/soft9000/PyHershey
# DATE: 2023-06-25 12:29:59
# FILE: Font.py
# AUTHOR: See https://ko-fi.com/randallnagy
#

from Hershey9000.VectorFont.FontData import FontData


class Font(FontData):
    ''' The font factory '''

    def __init__(self, dict_data):
        super().__init__(dict_data=dict_data.data)

    @staticmethod
    def List_Fonts():
        from Hershey01.GsDict.Library import Reader
        return Reader.list_fonts()

    @staticmethod
    def Load_Font(font_name):
        from Hershey01.GsDict.Library import Reader
        return Font(Reader.load_font(font_name))






