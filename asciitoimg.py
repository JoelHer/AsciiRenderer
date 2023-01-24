from PIL import Image, ImageDraw
import os

def asciiToIMG(matrix, i):
  font_width, font_height = 12, 12
  width, height = font_width * 40, font_height * 40
  # Create an empty image with a white background
  image = Image.new("RGB", (width, height), (0, 0, 0))
  
  # Create a draw object to draw on the image
  draw = ImageDraw.Draw(image)
  
  # Iterate through the character matrix and draw each character on the image
  for y in range(len(matrix)):
      for x in range(len(matrix[0])):
        # print(f'[{y}][{x}]')
        draw.text((x*font_width, y*font_height), matrix[y][x], fill=(255, 255, 255))
  
  # Save the image
  image.save(os.path.join("images", f"image{i}.png"))


def imagesToGif(image_num):
  images = []
  
  # Append the rest of the images to the list
  for i in range(image_num):
      image = Image.open(os.path.join("images", f"image{i}.png"))
      images.append(image)
  
  # Save the images as a GIF
  image.save(os.path.join("images", "render.gif"), save_all=True, append_images=images, duration=100, loop=0)
