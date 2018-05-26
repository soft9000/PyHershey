class FontData:
    ''' An easy way to manage an external collection of related Glyphs '''

    def __init__(self, dict_data=None):
        from collections import OrderedDict
        if dict_data is None:
            self.data = OrderedDict()
            self.font_name = 'Undefined'
            self.font_rect = '0,0,0,0'
        else:
            self.data = dict_data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    @property
    def font_name(self):
        return self.data["font_name"]

    @font_name.setter
    def font_name(self, value):
        self.data["font_name"] = value

    @property
    def font_rect(self):
        return self.data["font_rect"]

    @font_rect.setter
    def font_rect(self, value):
        self.data["font_rect"] = value

    def is_null(self):
        return len(self.data) <= 2

    def glyph_count(self):
        if self.is_null():
            return -1
        size = len(self.data) - 2
        return size

    def get_glyph(self, glyph_number):
        line = int(glyph_number)
        return list(self.data[glyph_number])

    def calc_rect(self, glyph_number):
        lines = self.get_glyph(glyph_number)
        result = [99, 99, 0, 0]
        for point in lines:
            if point[0] < result[0]:
                result[0] = point[0]
            if point[1] < result[1]:
                result[1] = point[1]
            if point[0] > result[2]:
                result[2] = point[0]
            if point[1] > result[3]:
                result[3] = point[1]
        return result

    def add_point(self, xval, yval, glyph_number=0):
        xval = int(xval); yval=int(yval)
        if glyph_number in self.data.keys():
            points = self.data[glyph_number]
            points.append([xval, yval])
        else:
            self.data[glyph_number] = [[xval, yval]]

