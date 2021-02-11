import LCD_1in44
import LCD_Config

from PIL import Image,ImageDraw,ImageFont,ImageColor

#try:
def main():
    LCD = LCD_1in44.LCD()

    print("**********Init LCD**********")
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    print(LCD.width, LCD.height)

    image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
    draw = ImageDraw.Draw(image)
    print("***draw text")
    draw.text((33, 22), 'WaveShare ', fill = "RED")
    draw.text((32, 36), 'Electronic ', fill = "#00ff00")
    draw.text((28, 48), '1.44inch LCD ', fill = "BLUE")

    LCD.LCD_ShowImage(image,0,0)
    LCD_Config.Driver_Delay_ms(1)

if __name__ == '__main__':
    main()

#except:
#	print("except")
#	GPIO.cleanup()
