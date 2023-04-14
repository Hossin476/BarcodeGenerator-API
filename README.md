# BarcodeGenerator-API

This is a simple Flask-based API that generates barcode images in PNG format. The API currently supports EAN-13 barcode format.

Usage

The API has a single endpoint:

/barcode?code=<barcode_value>

Where <barcode_value> is the value you want to generate the barcode for.

If the code parameter is missing or empty, the API will return a 400 error.

Example

To generate a barcode image for the value 123456789012, make a GET request to:

http://localhost:5000/barcode?code=123456789012
This will return a PNG image with the barcode for the given value.

Dependencies

This API was built using Python3 and the following libraries:

Flask
python-barcode

Running the API

To run the API locally, simply execute the script:

python barcode.py

By default, the API listens on port 5000. Set the FLASK_RUN_PORT environment variable to change the port.

API Access

You can also access this API on RapidAPI at:

https://rapidapi.com/hossaynsohail2018-JItm-7SiChY/api/barcode-generator12