# Communication by meme

---

The core challenge is to read the EXIF data and decipher the flag which is encrypted with base64.

I have used a standard meme and added some text to it, which reads "WTF is EXIF".
This is the hint for the participant to look at the EXIF data, where they will find several fields that have incorrect information.
There are 3 red herrings and the flag.

Determining the encryption should be quite straightforward, participants that are familiar with base64 should recognise it immediately, and the others shouldn't have much trouble finding it through trial and error, as base64 is quite common.

During testing I found that not all EXIF reading programs displayed the full range of EXIF data that I had included, I have made sure that the flag is now under the author field to ensure that it is always findable.