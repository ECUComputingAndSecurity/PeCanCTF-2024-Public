# Insignificant

---

The core of this challenge is using a steganography tool to decrypt this message hidden inside.

Using an image found online, I have overlayed some text which has a very simple computer science trivia question. The answer to the trivia question is the passcode used to encrypt the file. The file was encrypted using steghide, a common steganography tool.

The participant should be able to obtain the passphrase by answering the trivia question, if they don't know the answer, googling the question will return the answer immediately without further searching.
After they have the passcode it becomes a matter of determining where the information is stored within the image.
If the participant is familiar with steganography challenges, they should be aware of tools such as steghide and will likely recognise the challenge.
If the participant is unfamiliar with steganography challenges, they should come across valid solutions after performing some basic research into hiding messages into images.

The name of the challenge is a light hint, referring to the technique of hiding messages using the least significant bits within an image file.