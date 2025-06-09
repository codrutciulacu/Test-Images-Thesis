from PIL import Image
import random
import os

def generate_random_pixel_image(width, height, output_dir='output', filename=None):
    os.makedirs(output_dir, exist_ok=True)
    
    image = Image.new('RGB', (width, height))
    pixels = image.load()
    
    for x in range(width):
        for y in range(height):
            # Generate random RGB values
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            pixels[x, y] = (r, g, b)
    
    
    if not filename:
        filename = f'image_{width}x{height}.png'
    
    image_path = os.path.join(output_dir, filename)
    image.save(image_path)
    print(f'Saved: {image_path}')

sizes = [
    (100, 100),
    (200, 200),
]

for w, h in sizes:
    generate_random_pixel_image(w, h)
