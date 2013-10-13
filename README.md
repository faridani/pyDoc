pyDoc: Simple Collaborative Python Coding Using Google Doc
=====
Making cloud coding as simple as typing: 

    On Windows: run.bat
    On Mac/Linux: bash run.bat



Prerequisites
=============
Make a google document like [this](https://docs.google.com/document/d/1vhPW2O35duAQWuF78b306_5gsPBjq7Jiygdt9U-iIdc/edit?usp=sharing). Note down the Document ID that appears in the url 
    
https://docs.google.com/document/d/ **1vhPW2O35duAQWuF78b306_5gsPBjq7Jiygdt9U-iIdc** /edit

(optional) For easier coding go to tools>prefrences and turn off all options. Also from the fonts use "Consolas".

In the pydoc directory you will also find a copy of the unicode module. Install it by going into that directory and typing 

    $ python setup.py install


In the pydoc.py file that exists in the rood directory replace your DOCID 

    DOCID = "1vhPW2O35duAQWuF78b306_5gsPBjq7Jiygdt9U-iIdc"
    
Usage
=====
run:

    $ python pydoc.py
    $ python py.py
    
The first command fetches the Google doc and places it in py.py. The second command runs the py.py
