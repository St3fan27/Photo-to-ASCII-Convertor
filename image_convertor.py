from PIL import Image

ASCII_CHARS = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "
)

class ASCIIConverter:
    """
    ASCIIConverter class:
    Converts an image to ASCII art in black and white.
    """

    def __init__(self, ascii_chars=ASCII_CHARS):
        """
        Initializes the ASCIIConverter with a list of ASCII characters.
        """
        self.ascii_chars = ascii_chars

    def resize_image(self, image, new_width=100):
        """
        Resize the image while keeping the aspect ratio.
        Adjusts the height to better fit ASCII characters.
        """
        w, h = image.size
        ratio = h / w

        # Adjust the height to maintain the original image's aspect ratio.
        # ASCII characters are usually taller than they are wide, so we multiply by 0.55
        # to correct the vertical stretching and make the ASCII art look proportional.
        # Note: This was added to fix a problem encountered previously where
        # the ASCII art appeared vertically stretched or squashed.
        new_height = int(new_width * ratio * 0.55)
        return image.resize((new_width, new_height))

    def grayify(self, image):
        """
        Convert the image to grayscale.
        """
        return image.convert("L")

    def pixels_to_ascii(self, image):
        """
        Map each pixel to an ASCII character based on its brightness.
        """
        pixels = image.getdata()
        ascii_str = "".join(self.ascii_chars[p * (len(self.ascii_chars)-1) // 255] for p in pixels)
        return ascii_str

    def convert(self, uploaded_file, new_width=100):
        """
        Convert the uploaded image file to ASCII art.
        """
        image = Image.open(uploaded_file)
        image = self.resize_image(image, new_width)
        image = self.grayify(image)
        ascii_str = self.pixels_to_ascii(image)
        width = image.width
        ascii_img = "\n".join(
            line.replace(" ", ".") for line in
            (ascii_str[i:i+width] for i in range(0, len(ascii_str), width))
        )
        return ascii_img
