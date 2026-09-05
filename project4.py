#Project 4 Image or Text Recognition 

import easyocr

# Create OCR reader using English language
reader = easyocr.Reader(['en'])

image_path = "sample.jpg"

# Recognize text from the image
result = reader.readtext(image_path)

print("\n===== TEXT RECOGNITION RESULT =====\n")

if len(result) > 0:

    for item in result:
        text = item[1]
        confidence = item[2]

        print("Detected Text :", text)
        print("Confidence    :", round(confidence * 100, 2), "%")
        print("----------------------------------")

else:
    print("No text detected in the image.")