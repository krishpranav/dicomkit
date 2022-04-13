# dicomkit
A Python Tool/Library To Convert Dicom File To Image

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## Tested on:
- Linux
- macOS
- Windows

## Requirements:
- Latest version of python3
- found any issues in running dicom kit feel free to open an [issue](https://github.com/krishpranav/dicomkit/issues/new)

# Using dicomkit as a library:
## Convert a single file
```python3
import dicomkit

dicomkit.convert_file('/home/user/file.dcm', '/home/user/output.png', auto_contrast=True)
```

## Convert a folder containing dicom files
```python3
import dicomkit

dicomkit.conver_folder('/home/user/dicomdir/', '/home/user/outputdir/')
```

## Cli of dicomkit:
## usage

- Installation:
```
python3 -m pip install -r requirements.txt
```

- convert a single file
```
python3 dicomkit --auto-contrast /folder/dicomfile.dcm outputdicomfile.png
```

- convert a directory containing dicom files:
```
python3 dicomkit.py /folder/ /output
```


## License:
```
MIT License

Copyright (c) 2022 Krisna Pranav

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```