import os
from PIL import Image, ImageDraw, ImageFont

# Constants
DEFAULT_FONT_SIZE = 42
TEXT_HEIGHT = 100
PANEL_SPACING = 15
BORDER_THICKNESS = 6
TEXT_BOX_BORDER = 4

# Font Loader
def load_default_font(size):
    """Loads Arial font or falls back to PIL default."""
    try:
        return ImageFont.truetype("arial.ttf", size)  
    except OSError:
        print("Arial font not found! Using Pillow's default font.")
        return ImageFont.load_default()

# Border Adder
def add_border(image, border_thickness, color="black"):
    """Adds a bold border around the image."""
    bordered_image = Image.new(
        "RGB",
        (image.width + 2 * border_thickness, image.height + 2 * border_thickness),
        color
    )
    bordered_image.paste(image, (border_thickness, border_thickness))
    return bordered_image

# Text Adder
def add_text_below(image, text, font, text_height=TEXT_HEIGHT):
    """Adds readable text below each panel with padding and centering."""
    width, height = image.size
    new_height = height + text_height
    new_image = Image.new("RGB", (width, new_height), "white")
    new_image.paste(image, (0, 0))

    draw = ImageDraw.Draw(new_image)
    
    # Text box
    text_box = [(0, height), (width, new_height)]
    draw.rectangle(text_box, outline="black", width=TEXT_BOX_BORDER)

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]

    # Center the text horizontally
    text_x = (width - text_width) // 2
    text_y = height + (text_height - DEFAULT_FONT_SIZE) // 2
    draw.text((text_x, text_y), text, fill="black", font=font)

    return new_image

# Image Processor
def process_image(image_path, output_path, text="Sample Text"):
    """Adds border, text, and saves the modified image."""
    img = Image.open(image_path)
    font = load_default_font(DEFAULT_FONT_SIZE)

    img_with_border = add_border(img, BORDER_THICKNESS)
    final_image = add_text_below(img_with_border, text, font)

    final_image.save(output_path)
    print(f"✅ Image saved at: {output_path}")

# Comic Strip Generator
def create_comic_strip_with_text(panel_images, panel_texts, output_image_path):
    """Combines six images into a 3x2 comic strip with text on each panel."""

    if len(panel_images) != 6 or len(panel_texts) != 6:
        raise ValueError("There must be exactly 6 panel images and 6 panel texts.")

    # Check if all image paths exist
    missing = [path for path in panel_images if not os.path.exists(path)]
    if missing:
        print("❌ Missing image files:", missing)
        raise FileNotFoundError("Some panel images are missing!")

    # Processing each panel
    processed_panels = []
    for i in range(6):
        img = Image.open(panel_images[i])
        font = load_default_font(DEFAULT_FONT_SIZE)
        img_with_text = add_text_below(img, panel_texts[i], font)
        processed_panels.append(img_with_text)

    # ✅ Correct grid dimensions
    width, height = processed_panels[0].size
    comic_width = width * 2      # ✅ 2 columns
    comic_height = height * 3    # ✅ 3 rows
    comic_strip = Image.new("RGB", (comic_width, comic_height), "white")

    # Add panels to the grid in 3x2 format
    for i, panel in enumerate(processed_panels):
        x = (i % 2) * width      # ✅ 2 columns
        y = (i // 2) * height    # ✅ 3 rows
        comic_strip.paste(panel, (x, y))

    # Save the final comic strip
    comic_strip.save(output_image_path)
    print(f"✅ Comic strip saved at {output_image_path}")


# ======== MAIN EXECUTION ========
if __name__ == "__main__":
    # Define folders
    input_folder = "PANEL_IMAGES"
    output_folder = "OUTPUT"

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load images dynamically from the PANEL_IMAGES folder
    input_paths = [os.path.join(input_folder, f"panel_{i+1}.png") for i in range(6)]
    texts = [f"Dialogue {i+1}" for i in range(6)]

    # Final comic strip path
    output_image_path = os.path.join(output_folder, "final_comic_strip.png")

    # Generate the comic strip
    create_comic_strip_with_text(input_paths, texts, output_image_path)
