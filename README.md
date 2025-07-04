# QR Code Generator (Python OOP)

A customizable QR Code generator built using Python and the `qrcode` library. This project uses an object-oriented approach and runs in the terminal/CLI.

## 🧩 Features

- Create QR codes from any URL or text
- Customize:
  - Fill color
  - Background color
  - Box size and border
  - Output file name and image format
- High error correction (`ERROR_CORRECT_H`)

---

## 🛠️ Technologies Used

- Python 3
- `qrcode` library
- `Pillow` (automatically installed with `qrcode[pil]`)

---

## 🚀 How to Run

```bash
# Install dependencies
pip install qrcode[pil]

# Run the script
python qr_code_generator.py
