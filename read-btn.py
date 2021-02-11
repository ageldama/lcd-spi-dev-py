import spi
spi = SPI("/dev/spidev1.0")
spi.mode = SPI.MODE_0
while True:
    received = spi.read(10)
    print(received)
