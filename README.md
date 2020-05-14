# PIL_Building_Contact_Sheet
#### Using Python Imaging Library "PIL" to build better contact sheet

<img src="output_image.png" alt="Output" width="800"/>

you were shown how to make a contact sheet for digital photographers, and how you can take one image and create nine different variants based on the brightness of that image. you are going to change the colors of the image, creating variations based on a single photo. There are many complex ways to change a photograph using variations, such as changing a black and white image to either "cool" variants, which have light purple and blues in them, or "warm" variants, which have touches of yellow and may look sepia toned.

From the image you can see there are two parameters which are being varied for each sub-image. First, the rows are changed by color channel, where the top is the red channel, the middle is the green channel, and the bottom is the blue channel. Wait, why don't the colors look more red, green, and blue, in that order? Because the change you to be making is the ratio, or intensity, or that channel, in relationship to the other channels. We're going to use three different intensities, 0.1 (reduce the channel a lot), 0.5 (reduce the channel in half), and 0.9 (reduce the channel only a little bit).
For instance, a pixel represented as (200, 100, 50) is a sort of burnt orange color. So the top row of changes would create three alternative pixels, varying the first channel (red). one at (20, 100, 50), one at (100, 100, 50), and one at (180, 100, 50). The next row would vary the second channel (blue), and would create pixels of color values (200, 10, 50), (200, 50, 50) and (200, 90, 50).


#### *This work was delivered to week-one assignmet of "Python Project: pillow, tesseract, and opencv". 
#### *This course is part of the "Python 3 Programming Specialization" by University of Michigan.
#### https://www.coursera.org/learn/python-project/home/welcome
