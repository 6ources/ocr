import cv2
import numpy as np
import requests
import io
import json
print('Enter the file name')
x = input()
print('Enter the extension')
y = input()
img = cv2.imread(x+"."+y)
height, width, _ = img.shape

# Cutting image
roi = img 

# Ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode("."+y, roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
              files = {x+"."+y: file_bytes},
              data = {"apikey": "",
                      "language": "eng"})

result = result.content.decode()
result = json.loads(result)


parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(text_detected)

cv2.imshow("roi", roi)
cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
