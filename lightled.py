# lightled.py
import time
import threading
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

stop_thread = threading.Event()

def continuously_show():
    while not stop_thread.is_set():
        strip.show()
        time.sleep(0.1)

def set_leds(buttons):
    """Set the LEDs to the specified colors."""
    # Stop the thread that continuously shows the LEDs
    stop_thread.set()
    
    # Turn off all pixels
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

    # Set specified pixels to their colors
    for button in buttons:
        rgb = led_id = None
        try:
            rgb = button['color']
            led_id = int(button['id'])  # Convert led_id to integer
            print(f"Setting LED {led_id} to color {rgb}")
            color_int = Color(rgb[0], rgb[1], rgb[2])
            strip.setPixelColor(led_id, color_int)
        except Exception as e:
            print(f"Error setting LED {led_id} to color {rgb}: {e}")
            raise    

    # Start the thread that continuously shows the LEDs
    stop_thread.clear()
    threading.Thread(target=continuously_show).start()
    