This is a temporary label software solution built with Tkinter, a python GUI library.


The exe is built by auto-py-to-exe


With python-barcode module:
when importing the class ImageWriter from barcode.writer
it will invoke PIL (pillow)
must install freetype to solve the _imagingft C module not installed error
https://anaconda.org/anaconda/freetype
In order for python-barcode to export PNG correctly, freetype module must be installed.
You can use anaconda command prompt to use pip and install any packages not available in conda repo.

Hidden-import for auto-py-to-exe : babel.numbers
