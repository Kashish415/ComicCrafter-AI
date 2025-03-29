# ComicCrafter-AI

_ComicCrafter AI – Bring your stories to life with AI-generated comics.  🖼️⚡_

**Demo Video:** 

Click to watch the video.


[![ComicCrafter Demo](https://img.youtube.com/vi/bQmbAsUNWtY/hqdefault.jpg)](https://youtu.be/bQmbAsUNWtY)




---

##  **Project Overview**
**ComicCrafter AI** is a fully automated AI-powered tool that generates **comic strips** based on text prompts.  
It follows this pipeline:
1. **Panel Generation:** Generates structured panel descriptions and dialogues.  
2. **Image Creation:** Generates six art-style-specific images.  
3. **Text Overlay:** Adds dialogues from the panel descriptions onto images.  
4. **Final Output:** Combines images into a **3x2 grid comic strip** and saves it in the output/ folder.  

---

##  **Features**
 - **AI-Powered Comic Creation:**  Automatically generates structured panel descriptions and dialogues.  
 - **Art Style Selection:**  Choose from four unique art styles: Manga, Anime, American, and Belgian.  
 - **3x2 Grid Comic Strip:**  Combines six panels into a clean, ready-to-share comic strip.  
 - **User-Friendly Interface:**  Built with Streamlit for seamless interaction.  
 - **Downloadable Output:** The final comic strip is saved as an image (comic_strip.png) and can be downloaded as a PDF.  
 

---

##  **Tech Stack**
- **Programming Language:** Python  
- **Framework:** Streamlit  
- **APIs:**  
  - **Google Generative AI (Gemini Pro)** → For text generation.  
  - **ClipDrop (by Stability AI)** → For image generation.  

---

##  **Project Structure**
```bash
ComicCrafter-AI/
├── app.py                  
├── BACKEND/               
│   ├── generate_panels.py  
│   ├── generate_image.py   
│   ├── main.py
    ├── process_comic.py
           
├── PANEL_IMAGES/           
├── output/               
├── .env                   
├── requirements.txt      
└── README.md
```
---

##  **Installation and Setup**
### **1. Clone the Repository**
```bash
git clone https://github.com/Kashish415/ComicCrafter-AI.git  
cd ComicCrafter-AI
```

### **2. Install dependencies**
```bash
pip install -r requirements.txt
```

### **3. Add API Keys**
 Create a .env file in the root directory and add your API keys:
 
```bash
GOOGLE_API_KEY=your_google_api_key  
CLIPDROP_API_KEY=your_clipdrop_api_key
``` 

### **4. Run the Application**
```bash
streamlit run app.py
```


## **Contributing**
Contributions are welcome!

If you have improvements, bug fixes, or new feature ideas:

1. Fork the repository.

2. Create a new branch for your feature/fix.

3. Commit and push your changes.

4. Submit a pull request.

Feel free to experiment and create your own comics!

## Contributors  
- [Kashish Gupta](https://github.com/Kashish415)
- [Sunaina](https://github.com/Sunaina792) 


