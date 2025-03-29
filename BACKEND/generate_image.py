import io
import os
import requests
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
API_KEY = os.getenv("CLIPDROP_API_KEY")

OUTPUT_DIR = "PANEL_IMAGES"
os.makedirs(OUTPUT_DIR, exist_ok=True)

STYLE_MAPPINGS = {
    "Manga": "Black and white, sharp lines, exaggerated expressions, dramatic shading , No bright colors",
    "Anime": "Vivid colors, cel shading, expressive eyes, dynamic action poses.",
    "American": "Bold outlines, vibrant colors, comic book ink style, exaggerated features.",
    "Belgian": "Clear lines, soft shading, rich backgrounds, Tintin comic style.",
}

SYSTEM_INSTRUCTIONS = """
STRICT INSTRUCTIONS: 
Generate a high-quality, visually appealing image, consisting of the following elements:
- No speech bubbles, no text, no symbols, no gibberish language.
- Only clear, clean, and high-quality visual details.
- Do NOT add any text or letters in the image.
- No distorted, strange, unrealistic, or ugly facial features or elements.
- Ensure realistic proportions, natural expressions, and artistic coherence.
"""

def generate_images(panel_data, art_style):
    """Generates six images (one per panel) based on panel descriptions."""

    if art_style not in STYLE_MAPPINGS:
        raise ValueError(f"Invalid art style! Choose from: {', '.join(STYLE_MAPPINGS.keys())}.")

    image_paths = []

    # Loop through all six panels
    for i, panel in enumerate(panel_data):
        prompt = panel["Description"]
        full_prompt = (
            f"{prompt}.\n"
            f"Art Style: {STYLE_MAPPINGS[art_style]}.\n"
            f"{SYSTEM_INSTRUCTIONS}"
        )

        response = requests.post(
            "https://clipdrop-api.co/text-to-image/v1",
            headers={"x-api-key": API_KEY},
            files={"prompt": (None, full_prompt)}
        )

        if response.status_code == 200:
            try:
                image = Image.open(io.BytesIO(response.content))
                image_path = os.path.join(OUTPUT_DIR, f"panel_{i+1}.png")
                image.save(image_path)
                image_paths.append(image_path)
                print(f"Image {i+1} saved at: {image_path}")
            
            except Exception as e:
                print(f"Error opening image {i+1}: {e}")

        else:
            print(f"Error generating image for panel {i+1}: {response.text}")

    return image_paths




