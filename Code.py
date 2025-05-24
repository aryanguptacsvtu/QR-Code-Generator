import qrcode
import validators

def generate_qr(data, fill, back, filename):

    if not data.strip():
        print("⚠️ Error: Data for QR code is empty.")
        return

    if data.startswith("http") and not validators.url(data):
        print(f"⚠️ Warning: '{data}' does not appear to be a valid URL.")
        
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=10,border=4,)
    
    # Create a QR code instance
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill, back_color=back)
    img.save(filename)
    print(f"✅ QR code saved as: {filename}")
    # img.show()


generate_qr("https://www.youtube.com/", fill="red", back="grey", filename="youtube_qr.png")
generate_qr("https://github.com/", fill="blue", back="pink", filename="git_qr.png")


"""
*** generate_qr(data, fill, back, filename) :-

    Generate and save a QR code image with customizable options.

    Parameters:
    - data (str): The content to encode into the QR code (URL, text, etc.).
    - fill (str): Color of the QR code blocks (default is 'black').
    - back (str): Background color of the QR code (default is 'white').
    - filename (str): The filename to save the QR code image (default is 'qr.png').

    Returns:
    - None
"""