# HDF5Converter
###Converts PED / MAP files into a single HDF5 file
Testing using Syngenta data resulted in a file 52% of the original size 

(PED + MAP file sizes compared to .h5 output file size)

1.614GB -> 0.849GB


###Usage
####To HDF5
convert.py -v to --dir Data --output H5FileName
-v / --verbosity is optional and triggers verbose mode
-d / --dir is the directory containing files to convert to a HDF5 file
-o /  --output is the name to save the .h5 file as, the extension will be added (i.e. don't use H5FileName.h5)
-c / --collength is the length of each column (excluding the last column of the PED file). Default is set to 16 characters per cell

####From HDF5
converty.py -v from --hdf H5FileName --dir OutputDirectory
-v / --verbosity is optional and triggers verbose mode
-i / --hdf is the H5 file (with extension) to convert back to numerous files
-d / --dir is the directory to save the output to


###Contributing
####Adding DataTypes
The PED.py and MAP.py files located in the DataTypes directory should be used as reference.
The data_format represents how the data is organized within your files after it is split. By default, the split is made using whitespace. If you have data formatted in another way, you will have to override the read function. The data_format is a dictionary where the key is the column name, the first value of the tuple is the location of the data point within the split line, and the second value of the tuple is the DataType used by PyTables to instantiate the table. 
