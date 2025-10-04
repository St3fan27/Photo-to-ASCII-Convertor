# 🎨 Photo to ASCII Convertor

A simple tool to convert images to ASCII art in black and white using Python and Streamlit.

## Problem Solved

Before this tool, generating ASCII art often required searching for pre-made ASCII models or manually creating them.  
This app solves that problem by allowing you to generate ASCII art directly from any image in just a few clicks.

## Features

- Converts uploaded images to ASCII art.
- Adjustable ASCII width: 50, 100, 150, 200.
- Displays the ASCII art in a scrollable code block.
- No need to search for ASCII models manually — you can generate your own from any image.

## Installation

1. Clone the repository or download the files.

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. First, run the Streamlit app:

```bash
streamlit run main.py
```

2. Then, open the provided URL (usually `http://localhost:8501`) in your browser.  
3. Upload an image (`jpg`, `jpeg`, or `png`).  
4. Select the ASCII width (50, 100, 150, or 200).  
5. View the generated ASCII art in the code block.

## Principle

The tool works by:

1. Resizing the image while preserving its aspect ratio.  
2. Converting the image to grayscale.  
3. Mapping each pixel’s brightness to an ASCII character.  
4. Displaying the resulting ASCII characters as a text-based representation of the image.

## Notes

- The aspect ratio is slightly adjusted (`*0.55`) to compensate for characters being taller than wide, making the output look proportional.

Enjoy turning your photos into ASCII art! 🎨

