from VectorFont.FontData import FontData


class Reader:
    ''' Sole objective is to read those legacy GSTEXT files.
    Most of wee 'Pythonic geeks will want to use Library.py
    in the GsDict package to convert this to same, else simply
    get started using the output of the conversion by using
    the Font.py file in the VectorFont Module.
    '''
    delim = {
        "SEP_OBJ":"@",
        "SEP_MANY":"#",
        "SEP_PARAM":":",
        "SEP_FIELD":","
    }

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
            if file.endswith(".gstext"):
                dot = file.rfind('.')
                results.append(file[0:dot])
        return results

    @staticmethod
    def load_font(font_name):
        try:
            with open(Reader.get_dir() + font_name + ".gstext") as fh:
                return Reader.parse_font_line(fh.readline().strip())
        except Exception as ex:
            raise ex # Maybe something clever, later on?

    @staticmethod
    def parse_font_line(sdata):
        result = FontData()
        if sdata is None:
            return result
        data = str(sdata).split(Reader.delim["SEP_OBJ"])
        if len(data) < 2:
            return result
        result.font_name = data[0]
        result.font_rect = eval('[' + data[1] + ']')
        lines = data[2:]
        for ss, glyph in enumerate(lines):
            line = glyph.split(Reader.delim["SEP_MANY"])
            for points in line:
                point = points.split(Reader.delim["SEP_PARAM"])
                for param in point:
                    val = param.split(Reader.delim["SEP_FIELD"])
                    if len(val) >= 2:
                        result.add_point(val[0], val[1], glyph_number=ss) # omit closing
                        if len(val) > 2:
                            if val[2] != '':
                                raise ValueError("Yikes:", val)
                    else:
                        if val[0] != '':
                            raise ValueError("Detected:", val)
        return result


if __name__ == '__main__':
    ''' Official test case. '''
    print(Reader.get_dir())

    fonts = Reader.list_fonts()
    print(fonts)

    defset = []

    for font in fonts:
        result = Reader.load_font(font)
        print(result.font_name, result.font_rect)
        for line in result.data:
            print(line, result.data[line])
        print(result.data)
        defset.append(result.data)

    for ss, font in enumerate(defset, 1):
        print(ss, font)
