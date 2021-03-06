# LED Matrix Controller

This project was designed with an Atmel ATSAMD51J19 microcontroller and a Lucky Light Electronics Co. 32x32 LED matrix in mind.  If you're using a different microcontroller, you probably need to change port/pin mappings.  If you're using a different LED matrix, make sure it uses the same control lines.

## Usage

Compile `led_matrix.ino` in Arduino IDE and upload to your microcontroller.  Wire your LED matrix appropriately for the model you've chosen.

## Image Generator

A python utility has been included to help generate data arrays that specify the images to display on the matrix.

```
create_led_pixel_array.py filename.txt
```

Where `filename.txt` is output from "export as C file" of a sprite generated at www.piskelapp.com.

For animation, create a series of images, then create the data structures following examples in the `data` directory.

## Examples

![flag](https://raw.githubusercontent.com/nickbild/led_matrix/master/README/flag.jpg)

![snowman](https://raw.githubusercontent.com/nickbild/led_matrix/master/README/snowman.jpg)

## Note

This code is highly optimized for processing speed at the expense of readability.  Microcontroller resources are limited, and manual pulse width modulation of a 32x32 LED matrix requires lots of cycles if flicker is to be avoided.

## About the Author

https://nickbild79.firebaseapp.com/

