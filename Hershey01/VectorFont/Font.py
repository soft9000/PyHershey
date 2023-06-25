from Hershey01.VectorFont.FontData import FontData


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






