import qrcode


class QRCodeGenerator:
    """
    A class to generate QR codes with customizable colors, size, and format.

    Attributes:
        url (str): The URL or text to encode in the QR code.
        fill_color (str): The color of the QR code pattern.
        back_color (str): The background color of the QR code.
        file_name (str): The name of the output image file.
        file_format (str): The format of the output image (e.g., png, jpg).
        box_size (int): The size of each box in the QR code grid.
        border (int): The width of the border around the QR code.
    """

    def __init__(self):
        """Initializes all attributes with default or empty values."""
        self.url = ""
        self.fill_color = ""
        self.back_color = ""
        self.file_name = ""
        self.file_format = "png"
        self.box_size = 10
        self.border = 4

    def ask(self):
        """
        Collects input from the user for QR code customization:
        - URL/text to encode
        - Fill and background colors
        - File name and format
        - Box size and border thickness
        """
        self.url = input("URL for QR Code: ")
        self.fill_color = input("Fill color (e.g., black): ")
        self.back_color = input("Background color (e.g., white): ")
        self.file_name = input("File name (without extension): ")
        self.file_format = input("File format (e.g., png): ") or "png"

        try:
            self.box_size = int(input("Box size (default 10): ")) or 10
        except ValueError:
            print("Invalid box size. Using default (10).")
            self.box_size = 10

        try:
            self.border = int(input("Border size (default 4): ")) or 4
        except ValueError:
            print("Invalid border size. Using default (4).")
            self.border = 4

    def make_qr_code(self):
        """
        Generates and saves a QR code based on the provided attributes.
        Uses the qrcode library with high error correction.
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=self.box_size,
            border=self.border
        )
        qr.add_data(self.url)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
        img.save(f"{self.file_name}.{self.file_format}")
        print(f"✅ QR Code saved as: {self.file_name}.{self.file_format}")


if __name__ == "__main__":
    qr_code = QRCodeGenerator()
    qr_code.ask()
    qr_code.make_qr_code()
