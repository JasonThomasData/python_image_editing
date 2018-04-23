#### Outlines

Original - note this is an original RAW file from a Nikon d90. All other pics here have been
converted to JPEG after processing to display here, because the actual files are too large.

![original](../images/DSC_0110.NEF)

    ufraw-batch --output=FILE_geeves.tiff --out-type=tiff images/DSC_0110.NEF 

![FILE_geeves.tiff](../images/FILE_geeves.tiff.jpg)

    ./make_simple.py images/FILE_geeves.tiff 4 4 4

![make_simple_4_4_4_FILE_geeves.tiff](../images/make_simple_4_4_4_FILE_geeves.tiff.jpg)

    ./outlines.py images/make_simple_4_4_4_FILE_geeves.tiff

![outlines__make_simple_4_4_4_FILE_geeves.tiff](outlines__make_simple_4_4_4_FILE_geeves.tiff.jpg)
