# Image Steganography

A simple Python command-line tool that hides UTF-8 text inside PNG images using least-significant-bit (LSB) steganography.

The program modifies the lowest bit of image pixel color values to store text. Because the changes are very small, the resulting image should look visually similar to the original.

## Features

- Accepts PNG images as input.
- Encodes UTF-8 text into image pixel data.
- Saves the result as a new encrypted PNG image.
- Can immediately attempt to decode the hidden text.
- Uses OpenCV for image loading, editing, and saving.

## Requirements

- Python 3.12 or newer
- `uv`
- OpenCV

The Python dependency is:

```text
opencv-python
