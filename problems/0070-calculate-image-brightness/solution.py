def calculate_brightness(img):
    if not img or len(img) == 0:
        return -1
    
    row_length = len(img[0])
    
    total = 0
    count = 0
    
    for row in img:
        if len(row) != row_length:
            return -1
        for pixel in row:
            if pixel < 0 or pixel > 255:
                return -1
            total += pixel
            count += 1
    
    return round(total / count, 2)