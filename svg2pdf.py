from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

import sys

if __name__ == "__main__":
    drawing = svg2rlg(sys.argv[1])
    renderPDF.drawToFile(drawing, sys.argv[2])