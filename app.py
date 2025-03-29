import streamlit as st
import os
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Image as RLImage, Spacer
from BACKEND import generate_panels, generate_image, process_comic

PANEL_FOLDER = "PANEL_IMAGES"
OUTPUT_FOLDER = "OUTPUT"

os.makedirs(PANEL_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

STYLE_DESCRIPTIONS = {
    
    "Manga": "Predominantly black-and-white artwork with sharp lines and dramatic shading with no bright colors.",
    "Anime": "Vibrant colors, expressive eyes, and dynamic action poses.",
    "American": "Bold outlines, striking colors, and detailed inking styles.",
    "Belgian": "Clear, precise lines with rich, detailed backgrounds (e.g., Tintin)."
}

st.title("🎨 ComicCrafter AI")
st.write("Generate a 3x2 comic strip from your story prompt")

# User inputs
user_prompt = st.text_area("📝 Enter your story prompt", "")

art_style = st.selectbox("🎨 Choose an art style", list(STYLE_DESCRIPTIONS.keys()))
st.info(f"**Style Description:** {STYLE_DESCRIPTIONS[art_style]}")

if st.button(" Generate Comic"):
    if user_prompt:
        with st.spinner(" Generating panel descriptions & dialogues..."):
            panel_data = generate_panels.generate_panels(user_prompt, art_style)

        with st.spinner(" Generating images for comic panels..."):
            image_paths = list(generate_image.generate_images(panel_data, art_style))

        panel_texts = [panel["Text"] for panel in panel_data]

        if len(image_paths) == 6 and all(isinstance(img, str) and os.path.exists(img) for img in image_paths):
            
            output_image_path = os.path.join(OUTPUT_FOLDER, "comic_strip_with_text.png")

            process_comic.create_comic_strip_with_text(image_paths, panel_texts, output_image_path)

            st.image(output_image_path, caption="Your Comic Strip", use_container_width=True)
            st.success(" Comic generated successfully!")

            # PDF Generation
            pdf_output_path = os.path.join(OUTPUT_FOLDER, "comic_strip.pdf")

            def create_pdf(image_path, pdf_output_path):
                """Generate a PDF from the final comic strip"""
                doc = SimpleDocTemplate(pdf_output_path, pagesize=A4)
                img = RLImage(image_path, width=400, height=600)
                spacer = Spacer(1, 20)

                doc.build([img, spacer])

            create_pdf(output_image_path, pdf_output_path)

            # PDF Download Button
            with open(pdf_output_path, "rb") as pdf_file:
                st.download_button(
                    label="📥 Download Comic as PDF",
                    data=pdf_file,
                    file_name="comic_strip.pdf",
                    mime="application/pdf"
                )
        else:
            st.error(" Something went wrong! Please try again later.")
    
    else:
        st.error(" Please enter a story prompt.")
