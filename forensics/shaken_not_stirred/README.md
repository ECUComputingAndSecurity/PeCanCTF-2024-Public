# Shaken Not Stirred

---

This is a wrong extension/header challenge.
I have used ChatGPT to write a simple story about Pecan+, I have put that into a word document and placed the flag next to the title.
From there I inserted the jpg hex `FF D8` file signature before the docx signature, still keeping the docx signature in tact.
I have also changed the extension to .jpg to make it look more like an image file.

If the participant tries to view the image, they will be met with an error that something is wrong.
If the participant uses the 'strings' command on the file, they will see many strings that denote a word file.
The key step that they must then take, is to remove the jpg hex signature and extension from the file, once they do that the file becomes much easier to work with.
The participant should be able to research the information necessary to determine what file type the file was originally.

To remove 2 bytes from the start of the file:
```sh
dd bs=2 skip=1 if=file.jpg of=file.docx
```

See <https://www.garykessler.net/library/file_sigs.html>.
Note that the JPG entries here differ from those [on Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures).
