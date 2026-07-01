from PIL import Image, ImageDraw, ImageFont
import os

WIDTH = 1200
HEIGHT = 900

os.makedirs("dataset/pair001", exist_ok=True)

img = Image.new("RGB", (WIDTH, HEIGHT), "white")
draw = ImageDraw.Draw(img)

# -----------------------
# Border
# -----------------------
margin = 30
draw.rectangle(
    [margin, margin, WIDTH-margin, HEIGHT-margin],
    outline="black",
    width=3
)

# -----------------------
# Title
# -----------------------
font = ImageFont.load_default()

draw.text(
    (450, 45),
    "MECHANICAL DRAWING",
    fill="black",
    font=font
)

# -----------------------
# Component Plate
# -----------------------
draw.rectangle(
    [250,200,950,650],
    outline="black",
    width=3
)

# -----------------------
# Holes
# -----------------------
holes = [
    (350,300),
    (850,300),
    (350,550),
    (850,550)
]

for x,y in holes:

    draw.ellipse(
        [x-20,y-20,x+20,y+20],
        outline="black",
        width=3
    )

# -----------------------
# Slot
# -----------------------
draw.rounded_rectangle(
    [520,390,680,460],
    radius=20,
    outline="black",
    width=3
)

# -----------------------
# Bottom Title Block
# -----------------------

draw.line(
    [(30,760),(1170,760)],
    fill="black",
    width=2
)

draw.text((60,790),"PART : Mounting Plate",fill="black",font=font)
draw.text((420,790),"SCALE : 1:1",fill="black",font=font)
draw.text((700,790),"REV : 0",fill="black",font=font)

img.save("dataset/pair001/before.png")

print("before.png created")