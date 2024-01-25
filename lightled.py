# lightled.py
import time
from rpi_ws281x import Color, Adafruit_NeoPixel

# LED strip configuration:
LED_COUNT = 300      # Number of LED pixels.
LED_PIN = 18        # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10        # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

def set_leds(colors):
    """Set the LEDs to the specified colors."""
    # Turn off all pixels
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))

    # Set specified pixels to their colors
    for color in colors:
        strip.setPixelColor(color['id'], Color(color['color'][0], color['color'][1], color['color'][2]))

    strip.show()