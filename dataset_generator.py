from PIL import Image, ImageDraw, ImageFont
import os
import random

WIDTH = 1400
HEIGHT = 1000

DATASET = "dataset"

font = ImageFont.load_default()


def border(draw):
    draw.rectangle((25,25,1375,975), outline="black", width=3)


def title(draw):
    draw.text((560,40),"MECHANICAL ENGINEERING DRAWING",fill="black",font=font)


def title_block(draw,rev):

    y=820

    draw.line((25,y,1375,y),fill="black",width=2)

    draw.line((500,y,500,975),fill="black",width=2)
    draw.line((850,y,850,975),fill="black",width=2)
    draw.line((1100,y,1100,975),fill="black",width=2)

    draw.text((40,850),"PART : Mounting Plate",font=font,fill="black")
    draw.text((530,850),"SCALE : 1 : 1",font=font,fill="black")
    draw.text((870,850),"DRAWN BY : AI",font=font,fill="black")
    draw.text((1130,850),f"REV : {rev}",font=font,fill="black")


def plate(draw):

    draw.rectangle((300,220,1100,700),outline="black",width=3)


def holes(draw,pts):

    for x,y,r in pts:
        draw.ellipse((x-r,y-r,x+r,y+r),outline="black",width=3)


def slots(draw,slots):

    for x1,y1,x2,y2 in slots:
        draw.rounded_rectangle((x1,y1,x2,y2),radius=18,outline="black",width=3)


def dimensions(draw):

    draw.line((300,170,1100,170),fill="black",width=2)

    draw.polygon([(300,170),(310,165),(310,175)],fill="black")
    draw.polygon([(1100,170),(1090,165),(1090,175)],fill="black")

    draw.text((650,145),"800 mm",font=font,fill="black")

    draw.line((250,220,250,700),fill="black",width=2)

    draw.polygon([(250,220),(245,230),(255,230)],fill="black")
    draw.polygon([(250,700),(245,690),(255,690)],fill="black")

    draw.text((190,440),"480 mm",font=font,fill="black")


def notes(draw):

    draw.text((1130,240),"NOTE",font=font,fill="black")
    draw.text((1130,260),"Material : Steel",font=font,fill="black")
    draw.text((1130,280),"Finish : Painted",font=font,fill="black")


def create_before():

    img=Image.new("RGB",(WIDTH,HEIGHT),"white")
    draw=ImageDraw.Draw(img)

    border(draw)
    title(draw)
    plate(draw)

    holes_list=[
        (380,300,22),
        (1020,300,22),
        (380,620,22),
        (1020,620,22)
    ]

    slot_list=[
        (570,430,830,500)
    ]

    holes(draw,holes_list)
    slots(draw,slot_list)
    dimensions(draw)
    notes(draw)
    title_block(draw,0)

    return img,holes_list,slot_list


def create_after(img,holes_list,slot_list):

    img=img.copy()

    draw=ImageDraw.Draw(img)

    change=random.randint(1,5)

    summary=""

    if change==1:
        holes_list.append((700,620,22))
        holes(draw,[(700,620,22)])
        summary="A new mounting hole has been added near the bottom centre."

    elif change==2:
        slot_list.append((540,320,860,370))
        slots(draw,[(540,320,860,370)])
        summary="A new horizontal slot has been added."

    elif change==3:
        draw.text((1120,320),"ADD M8 THREAD",font=font,fill="black")
        summary="A manufacturing note has been added."

    elif change==4:
        draw.text((660,120),"REVISION UPDATED",font=font,fill="black")
        summary="Revision annotation has been added."

    else:
        draw.ellipse((675,455,725,505),outline="black",width=3)
        summary="A circular feature has been added inside the slot."

    title_block(draw,1)

    return img,summary


def generate(n=50):

    os.makedirs(DATASET,exist_ok=True)

    for i in range(1,n+1):

        folder=os.path.join(DATASET,f"pair{i:03}")

        os.makedirs(folder,exist_ok=True)

        before,holes_list,slot_list=create_before()

        after,summary=create_after(before,holes_list,slot_list)

        before.save(os.path.join(folder,"before.png"))
        after.save(os.path.join(folder,"after.png"))

        with open(os.path.join(folder,"summary.txt"),"w") as f:
            f.write(summary)

        print(f"Pair {i} created")


generate()