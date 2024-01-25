# lightled.py
from rpi_ws281x import Color, Adafruit_NeoPixel

# LED strip configuration:
LED_COUNT = 300      # Number of LED pixels.
LED_PIN = 18        # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10        # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

def set_leds(colors):
    """Set the LEDs to the specified colors."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(colors[i][0], colors[i][1], colors[i][2]))
    strip.show()