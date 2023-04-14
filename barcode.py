from flask import Flask, request, Response
import barcode
from barcode.writer import ImageWriter
from io import BytesIO

app = Flask(__name__)
@app.route('/')
def home():
    return 'Barcode API'

@app.route('/barcode')
def generate_barcode():
    code = request.args.get('code')
    if not code:
        return 'Code parameter missing', 400

    # Generate the barcode for the given code
    ean = barcode.get('ean13', code, writer=ImageWriter())
    
    # Store the barcode image in memory using BytesIO
    buffer = BytesIO()
    ean.write(buffer)
    
    # Set the buffer's cursor to the beginning to read the data
    buffer.seek(0)
    
    # Set the Content-Type header to specify the image format
    mimetype = 'image/png'
    response = Response(buffer.getvalue(), mimetype=mimetype)
    response.headers.add('Content-Disposition', 'attachment', filename=f'{code}.png')
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
