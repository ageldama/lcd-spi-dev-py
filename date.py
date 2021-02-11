import LCD_1in44
import LCD_Config

from PIL import Image, ImageDraw, ImageFont

from datetime import datetime
import time


#try:
def main():
    LCD = LCD_1in44.LCD()

    print("**********Init LCD**********")
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    print(LCD.width, LCD.height)

    fnt = ImageFont.truetype('./FreeMono.ttf', 20)

    image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
    draw = ImageDraw.Draw(image)

    while True:
        draw.rectangle((0, 0, LCD.width-1, LCD.height-1), fill="BLACK")

        s = datetime.now().strftime('%H:%M:%S')
        draw.multiline_text((0, 36), s, fill="#00ff00", font=fnt)

        LCD.LCD_ShowImage(image,0,0)
        LCD_Config.Driver_Delay_ms(1)

        time.sleep(1)

if __name__ == '__main__':
    main()

#except:
#	print("except")
#	GPIO.cleanup()
