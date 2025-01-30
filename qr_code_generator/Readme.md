# Resume QR Code Generator

This project generates a personalized resume QR code with your name and a link to your resume stored online. The generated QR code can be scanned by any QR code scanner, and it will redirect the user to the provided resume link.

## Features

- Generates a QR code containing a link to your online resume.
- Customizable content (e.g., your name or a personalized message).
- Allows you to change the appearance of the QR code (e.g., colors and text).
- Saves the QR code as an image file (`Resume.png`).
  
![Image](https://github.com/user-attachments/assets/e7fdce97-5df5-4d18-84a4-609dcb9d9bd6)

## Requirements

- Python 3.x
- `qrcode` library
- `Pillow` library (for working with images)
- A font file (`arial.ttf`) or fallback to default font

To install the necessary Python libraries, run:

```bash
pip install qrcode[pil] pillow
