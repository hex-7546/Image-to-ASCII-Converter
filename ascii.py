from PIL import Image

#opens the image file
file = input("Enter the file name > ")
image = Image.open(file)

#turns the image to grayscale
gray_image = image.convert("L")

#saves the grayscale image
gray_image.save('grayscale_image.jpg')

#resize the image
res_img = gray_image.resize((200, 200))
res_img.save("resized_img.jpg")

#saves the color of the pixel to pixels variable
#pixels = res_img.getpixel((400,400))
width, height = res_img.size #saves width and height of image in variables

#print(width, height)

ascii_char = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`.  '

ascii_art =[]

for y in range(height):
    row_chars = ""
    for x in range(width):
        pixels = res_img.getpixel((x, y))
        char_index = pixels * (len(ascii_char) - 1) // 255  #matches the pixel (0 -255) to index of ascii_char
        row_chars += ascii_char[char_index] #saves each value of char_index in a variable
    ascii_art.append(row_chars)

complete_ascii_art = "\n".join(ascii_art)

with open("output.txt", "w") as file:
    file.write(complete_ascii_art)
