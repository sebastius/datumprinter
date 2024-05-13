# datumprinter
Generate and print labels with $current_date

Also install: `https://pypi.org/project/brother-ql/`

I edited brother-ql to work with modern pillow. Edit `conversion.py` to change `ANTIALIAS` to `LANCZOS`

Print using:
```
brother_ql -b pyusb -m QL-700 -p usb://0x04f9:0x2042/000L5Z725272 print -l 62 current_date.png
```
