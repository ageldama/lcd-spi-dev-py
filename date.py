import LCD_1in44
import LCD_Config

from PIL import Image, ImageDraw, ImageFont

from datetime import datetime
import time

from random import randint


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


def main():
    LCD = LCD_1in44.LCD()

    print("**********Init LCD**********")
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    print(LCD.width, LCD.height)

    fnt = ImageFont.truetype(
        '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 26)

    image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
    draw = ImageDraw.Draw(image)

    while True:
        rgb, rgb_i = rand_rgb()

        draw.rectangle((0, 0, LCD.width-1, LCD.height-1), fill=rgb)

        s = datetime.now().strftime('%H:%M:%S\n%f')
        draw.multiline_text((0, 36), s,
                            align='center',
                            fill=rgb_i, font=fnt)

        LCD.LCD_ShowImage(image,0,0)
        LCD_Config.Driver_Delay_ms(1)

        time.sleep(0.1)

if __name__ == '__main__':
    main()

#except:
#	print("except")
#	GPIO.cleanup()
