# Baseline Analysis & Structured Dataset Construction for Mixed-Script OCR
This repository demonstrates a Quality Assurance (QA) pipeline** for refining AI training data. I utilized a baseline OCR engine to identify recognition gaps in complex Korean-Hanja documents and constructed a structured "Gold Standard" dataset for VLM fine-tuning.
In this example, I used Pytesseract specifically to demonstrate a baseline failure case. Even with multi-language packs, it failed to recognize the Hanja in the news headlines and public notices. I used this 'failure' as a starting point to:
1. manually generate the correct ground truth in JSON to ensure 100% accuracy.
2. develop a QA Script that measures the exact error gap using CER.
3. structure the data so that a more advanced VLM can be fine-tuned to solve these specific recognition errors.

## Data
- Image: Unstructured mixed-script (Modern Korean + Hanja)
- Gold standard: Structured data containing original (visual text), transcription (phonetic Korean) and metadata (task difficulty, language tags) to support multi-task learning

## Python script
- The Python script uses Pytesseract to generate a machine-read "draft" of the images. This serves as a baseline to identify which characters (like complex Hanja) are most difficult for standard engines to recognize.
- Used Character Error Rate (CER) via jiwer to provide a character-level diagnostic of Hanja recognition failures, which is critical for historical document integrity
