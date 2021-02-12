import LCD_1in44
import LCD_Config

from PIL import Image, ImageDraw, ImageFont

from datetime import datetime
import time
from random import randint
import itertools
import math



def fmt_rgb(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def rand_rgb():
    r = randint(0, 0xff)
    g = randint(0, 0xff)
    b = randint(0, 0xff)

    r_i = r ^ 0xff
    g_i = g ^ 0xff
    b_i = b ^ 0xff

    return (fmt_rgb(r, g, b),
            fmt_rgb(r_i, g_i, b_i),)


def radians():
    return (math.radians(i) for i in itertools.cycle(range(0, 360)))


class Mover:
    def __init__(self,
                 cur_pos=0,
                 max_pos=120,
                 direction=1,
                 accel_gen=radians):
        self.cur_pos = cur_pos
        self.max_pos = max_pos
        self.direction = direction
        self.accel_gen = accel_gen()

    def __next__(self):
        new_pos = self.cur_pos + (self.direction * next(self.accel_gen))
        
        if new_pos <= 0:
            new_pos = 0
            self.direction *= -1
        elif new_pos >= self.max_pos:
            new_pos = self.max_pos
            self.direction *= -1

        self.cur_pos = new_pos

        return new_pos
    

def main():
    LCD = LCD_1in44.LCD()

    print("**********Init LCD**********")
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    print(LCD.width, LCD.height)

    fnt_size = 26
    fnt = ImageFont.truetype(
        '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', fnt_size)

    image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
    draw = ImageDraw.Draw(image)

    mover = Mover(max_pos=LCD.height - 1 - (fnt_size * 2))

    # rgb, rgb_i = rand_rgb()
    rgb_fg = '#000000'
    rgb_bg = '#ffb6c1'

    while True:
        draw.rectangle((0, 0, LCD.width-1, LCD.height-1), fill=rgb_bg)

        s = datetime.now().strftime('%H:%M:%S\n%f')
        draw.multiline_text((0, next(mover)),
                            s, align='center', fill=rgb_fg, font=fnt)

        LCD.LCD_ShowImage(image,0,0)
        LCD_Config.Driver_Delay_ms(1)

        time.sleep(0.3)


if __name__ == '__main__':
    main()

#except:
#	print("except")
#	GPIO.cleanup()
