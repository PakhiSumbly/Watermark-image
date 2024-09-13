import cv2
import numpy as np
from datetime import datetime

def add_watermark(image_path, output_path, latitude, longitude, unique_number):
    
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Cannot open or read the image file at {image_path}")

    (height, width) = image.shape[:2]

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (0, 0, 0) 
    thickness = 2

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    watermark_text = (f"Timestamp: {timestamp} ,"
                      f"Latitude: {latitude} ,"
                      f"Longitude: {longitude} ,"
                      f"Unique Number: {unique_number}")

    
    #Setting margins (space from the edges)
    margin_x = 20  #Margin from the left and right edges
    margin_y = 20  #Margin from the top and bottom edges

    #Calculate the maximum width available for the text
    available_width = width - 2 * margin_x

    #Adjusting the font size to fit the available width
    while True:
        (text_width, text_height), _ = cv2.getTextSize(watermark_text, font, font_scale, thickness)
        if text_width <= available_width:
            break
        font_scale -= 0.1

    #Calculating the starting position
    start_x = int((width - text_width) / 2)
    start_y = int((height + text_height) / 2)  

    #Ensuring the text fits within the margins
    start_x = max(margin_x, start_x)
    start_y = min(height - margin_y, start_y)

    #Adding watermark text to the input image
    cv2.putText(image, watermark_text, (start_x, start_y), font, font_scale, color, thickness, cv2.LINE_AA)

    #Saving the result
    cv2.imwrite(output_path, image)

latitude = '28.5155 N'       
longitude = '77.3110 E'    
unique_number = '21'   

input_image_path = r"C:\Users\PakhiSumbly\OneDrive - Paktolus Solutions - HigherL LLC\Desktop\watermark\Media.jpg"
watermarked_image_path = r"C:\Users\PakhiSumbly\OneDrive - Paktolus Solutions - HigherL LLC\Desktop\watermark\watermarked_image.jpg"

add_watermark(input_image_path, watermarked_image_path, latitude, longitude, unique_number)
