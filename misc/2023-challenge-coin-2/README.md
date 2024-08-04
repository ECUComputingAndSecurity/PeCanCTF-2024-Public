The link from part 1 provides a option to complete a new challenge:
<https://pecanplus.ecusdf.org/?page=challenges&challenge=18efe3964fb3032409a48792070609d9>

There are two paths to solving stage 2:

## Brute force

Download the 16 images and manually reconstruct the QR code

## Logical approach

The 0's and 1's are not binary code, but do represent a 'state'. If you add line breaks after each block of digits and look carefully you can see the outline of QR-code locators. Replace all 0's with a space and all 1's with a █ - when properly scaled (excel is useful for this) you will get a QR-code that gives the following text: 'circumference over diameter, how unique'

cir/dia = pi

If we take the 'unique' digits in pi, we get '314592687'

Placing the images in this order gives the QR code.

The QR code links to: <https://pecanplus.ecusri.org/challenges/coin-2023/pi> where the flag is presented.
