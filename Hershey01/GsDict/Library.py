from VectorFont.FontData import FontData

''' Sole objective is to CONVERT those legacy GSTEXT files. 
Most of wee 'Pythonic folks will want to simply get started 
using the output of this conversion by using the Font.py file 
in the VectorFont Module.
'''

class Reader:
    file_type = ".gsdict"

    @staticmethod
    def get_dir():
        nodes = str(__file__).replace("\\", "/")
        sep = nodes.rfind("/")
        return nodes[:sep + 1]

    @staticmethod
    def list_fonts():
        results = []
        import os
        files = os.listdir(Reader.get_dir())
        for file in files:
            if file.endswith(Reader.file_type):
                dot = file.rfind('.')
                results.append(file[0:dot])
        return results

    @staticmethod
    def load_font(font_name):
        try:
            with open(Reader.get_dir() + font_name + Reader.file_type) as fh:
                return Reader.eval_font(fh.readline())
        except Exception as ex:
            raise ex # Maybe something clever, later on?

    @staticmethod
    def eval_font(sdata):
        result = FontData()
        if sdata is None:
            return result
        from collections import OrderedDict
        result.data = eval(sdata)
        return result


class Writer:

    @staticmethod
    def save_font(font_data):
        if isinstance(font_data, (FontData)) is False:
            raise ValueError("Invalid type:" + type(font_data))
        try:
            with open(Reader.get_dir() + font_data.font_name + Reader.file_type, 'w') as fh:
                print(font_data.data, file=fh, sep='', end='')
        except Exception as ex:
            raise ex
        return True


class Converter:

    @staticmethod
    def Convert():
        from GsText.Reader import Reader as ZReader

        for font in ZReader.list_fonts():
            font1 = ZReader.load_font(font)
            print(font1.font_name, font1.font_rect)
            Writer.save_font(font1)
            font2 = Reader.load_font(font1.font_name)
            if font1.glyph_count() != font2.glyph_count():
                raise Exception("Conversion error:" + font1.font_name)

        print("Data are in", Reader.get_dir())


if __name__ == '__main__':
    ''' Official conversion routine '''
    Converter.Convert()
