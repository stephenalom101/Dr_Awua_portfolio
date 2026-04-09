import fitz
try:
    doc = fitz.open('cv.pdf')
    text = '\n'.join([page.get_text() for page in doc])
    with open('cv.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Done extracting text from PDF.")
except Exception as e:
    with open('cv.txt', 'w', encoding='utf-8') as f:
        f.write(str(e))
    print(f"Error: {e}")
