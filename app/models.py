import colorsys

# Handle multiple pages
class PageManager:
    def __init__(self, pages, sections):
        for section in sections:
            # Handle single number section ranges
            if type(section.range) != type([]):
                section.range = [section.range, section.range]
            # Associate pages and sections
            for i in range(section.range[0], section.range[1] + 1):
                pages[i - 1].section = section
                pages[i - 1].index = i
        self.pages = pages
        self.sections = sections
        self.currentPageIndex = 1

    def getCurrentPage(self):
        return self.pages[self.currentPageIndex - 1]

    def setCurrentPageIndex(self, index):
        self.currentPageIndex = index


# Intiialize page
class Page:
    def __init__(
        self,
        file,
        section=None,
        embed=None,
        index=0,
    ):
        self.file = file
        self.section = section
        self.index = index
        self.embed = embed


# * Color convenience class
class Color:
    def __init__(self, hex):
        self.hex = hex
        rgb = Color.hex2rgb(hex)
        self.rgb = rgb
        self.hsv = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])

    def dimmed(self, dimFactor):
        hsv = self.hsv
        luminance = hsv[-1]
        luminance -= dimFactor
        if luminance < 0:
            luminance = 0
        elif luminance > 1:
            luminance = 1
        newRgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], luminance)
        return Color(Color.rgb2hex(newRgb))

    @staticmethod
    def hex2rgb(h):
        return tuple(int(h[i : i + 2], 16) / 255.0 for i in (1, 3, 5))  # skip '#'

    @staticmethod
    def rgb2hex(rgb):
        return f"#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}"


# Define a section
class Section:
    def __init__(self, name, range, theme: Color):
        self.name = name
        self.range = range
        self.theme = theme
        self.alt_theme = theme.dimmed(dimFactor=0.4)
