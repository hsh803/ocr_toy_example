import pytesseract
from PIL import Image
import os
import json
from jiwer import cer


# 1. Setup paths
image_folder = '/content/image'
gs_folder = '/content/gs'

# 2. Accuracy Metric Function (Character Error Rate logic)
print(f"{'File':<10} | {'CER':<6} | {'Ground Truth':<25} | {'OCR Result'}")
print("-" * 100)

# 3. Batch Processing
for filename in sorted(os.listdir(image_folder)):
    if filename.endswith(".jpg"):
        base_name = os.path.splitext(filename)[0]


        # Perform OCR with Hanja support
        img = Image.open(os.path.join(image_folder, filename))
        ocr_text = pytesseract.image_to_string(img, lang='kor+chi_tra').strip()

        # Load Gold Standard
        gs_path = os.path.join(gs_folder, f"{base_name}.json")
        with open(gs_path, 'r', encoding='utf-8') as f:
            gs_data = json.load(f)
        gs_text = gs_data['content']['original'].strip()

        # Compare
        error_rate = cer(gs_text, ocr_text)
        print(f"{filename:<10} | {error_rate:<6.2f} | {gs_text:<25} | {ocr_text}")