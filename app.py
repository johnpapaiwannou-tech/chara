import base64
import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Για το κορίτσι μου", page_icon="💖", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    body {
        background: linear-gradient(135deg, #ff6b6b, #c0392b, #e74c3c);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        min-height: 100vh;
        font-family: 'Poppins', sans-serif;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .stApp {
        background: transparent;
    }
    h1 {
        text-align: center;
        color: #fff;
        font-weight: 700;
        font-size: 3.5rem;
        text-shadow: 0 2px 15px rgba(0,0,0,0.3);
        margin-bottom: 15px;
        letter-spacing: 3px;
    }
    .stDivider {
        border-color: rgba(255,255,255,0.2);
        margin: 25px 0;
    }
    div.stButton > button {
        display: block;
        margin: 0 auto;
        font-size: 1.4rem;
        padding: 18px 55px;
        border-radius: 50px;
        font-weight: 600;
        background: linear-gradient(135deg, #ff6b6b, #ff4757);
        color: white;
        border: none;
        box-shadow: 0 10px 25px rgba(255,71,87,0.4);
        transition: all 0.3s ease;
        cursor: pointer;
        font-family: 'Poppins', sans-serif;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 35px rgba(255,71,87,0.6);
    }
    p, .stMarkdown, .stCaption {
        color: #fff;
        text-shadow: 0 1px 6px rgba(0,0,0,0.7);
        font-weight: 500;
        font-family: 'Poppins', sans-serif;
    }
    .stSubheader {
        color: #fff !important;
        font-weight: 600;
        text-align: center;
        text-shadow: 0 2px 10px rgba(0,0,0,0.5);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Για το κορίτσι μου")

PHOTO_PATH = "IMG_6960.jpeg"
UPLOAD_DIR = "photos"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def get_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


show_photo = st.button("Πάτα με!!")
if show_photo:
    img_b64 = get_image_base64(PHOTO_PATH)

    components.html(
        f"""
        <div class="stage">
            <div class="content">
                <img class="photo" src="data:image/jpeg;base64,{img_b64}" alt="My Photo" />
                <p class="caption">My Photo</p>
                <p class="love">
                    Στην αγορά του Αλ Χαλίλι. <br/>
                    θα πουλαν τα δύο σου χείλη.<br/>
                    δυο περιουσίες και άλλη μια.<br/>
                    τέσσερις εγώ θα δώσω.<br/>
                    θα πληρώσω όσο όσο.<br/>
                    να μου κάνουν μία μελανιά.<br/>
                </p>
            </div>
            <div id="hearts"></div>
        </div>

        <style>
        html, body {{
            margin: 0;
            padding: 0;
            overflow: hidden;
            font-family: "Source Sans Pro", sans-serif;
        }}
        .stage {{
            position: relative;
            width: 100%;
            min-height: 720px;
        }}
        .content {{
            position: relative;
            z-index: 1;
            text-align: center;
            padding: 10px;
        }}
        .photo {{
            width: 45%;
            max-width: 420px;
            border-radius: 12px;
            display: block;
            margin: 0 auto;
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        }}
        .caption {{
            color: #111;
            font-size: 14px;
            font-weight: 600;
            text-shadow: 0 1px 3px rgba(0,0,0,0.6), 0 0 8px rgba(255,255,255,0.6);
            margin: 6px 0 20px 0;
        }}
        .love {{
            font-size: 20px;
            color: #000;
            font-weight: 700;
            line-height: 1.6;
            text-shadow: 0 1px 4px rgba(0,0,0,0.7), 0 0 12px rgba(255,255,255,0.8), 0 0 20px rgba(214,51,108,0.9);
        }}
        #hearts {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 2;
            overflow: hidden;
        }}
        .heart {{
            position: absolute;
            top: -50px;
            animation: fall linear forwards;
        }}
        @keyframes fall {{
            0%   {{ transform: translateY(0) rotate(0deg); opacity: 1; }}
            100% {{ transform: translateY(760px) rotate(360deg); opacity: 0; }}
        }}
        </style>

        <script>
        const hearts = ["❤️", "💖", "💕", "💗", "💓", "💞", "💘"];
        const container = document.getElementById("hearts");
        function drop() {{
            const heart = document.createElement("div");
            heart.className = "heart";
            heart.innerText = hearts[Math.floor(Math.random() * hearts.length)];
            heart.style.left = Math.random() * 100 + "%";
            heart.style.fontSize = (Math.random() * 24 + 18) + "px";
            heart.style.animationDuration = (Math.random() * 3 + 3) + "s";
            container.appendChild(heart);
            setTimeout(() => heart.remove(), 6000);
        }}
        for (let i = 0; i < 80; i++) {{
            setTimeout(drop, i * 150);
        }}
        setInterval(drop, 300);
        </script>
        """,
        height=760,
    )

st.divider()

photo_files = sorted(
    [f for f in os.listdir(UPLOAD_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp"))]
)

if photo_files:
    images_data = []
    mime_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    for photo in photo_files:
        ext = os.path.splitext(photo)[1].lower()
        b64 = get_image_base64(os.path.join(UPLOAD_DIR, photo))
        mime = mime_types.get(ext, "image/jpeg")
        images_data.append({"b64": b64, "mime": mime})
    
    images_json = str(images_data)
    
    components.html(
        f"""
        <div class="gallery-container">
            <img id="slide" class="slide-image" src="data:{images_data[0]['mime']};base64,{images_data[0]['b64']}" />
            <p id="counter" class="counter">1 / {len(photo_files)}</p>
        </div>
        
        <style>
        .gallery-container {{
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 500px;
            background: transparent;
        }}
        .slide-image {{
            max-height: 600px;
            width: auto;
            max-width: 100%;
            border-radius: 16px;
            box-shadow: 0 15px 50px rgba(0,0,0,0.6), 0 0 30px rgba(214,51,108,0.5);
            object-fit: contain;
            transition: opacity 0.8s ease-in-out;
        }}
        .counter {{
            color: #fff;
            font-weight: 700;
            text-shadow: 0 2px 8px rgba(0,0,0,0.8), 0 0 15px rgba(255,255,255,0.5);
            margin-top: 20px;
            font-size: 18px;
            letter-spacing: 2px;
        }}
        </style>
        
        <script>
        const images = {images_json};
        let index = 0;
        const slide = document.getElementById("slide");
        const counter = document.getElementById("counter");
        
        function showSlide(i) {{
            slide.style.opacity = '0';
            setTimeout(() => {{
                slide.src = "data:" + images[i].mime + ";base64," + images[i].b64;
                slide.style.opacity = '1';
                counter.textContent = (i + 1) + " / " + images.length;
            }}, 800);
        }}
        
        function nextSlide() {{
            index = (index + 1) % images.length;
            showSlide(index);
        }}
        
        setInterval(nextSlide, 3000);
        </script>
        """,
        height=700,
    )
else:
    st.subheader("Η συλλογή μας")
    st.write("Βάλε φωτογραφίες στον φάκελο photos για να εμφανιστούν εδώ...")

st.divider()

st.subheader("🎵 Το τραγούδι μας")

spotify_url = st.text_input(
    "Βάλε το Spotify link εδώ",
    placeholder="https://open.spotify.com/track/...",
)

if spotify_url:
    import re
    match = re.search(r"spotify\.com/(track|playlist|album)/([a-zA-Z0-9]+)", spotify_url)
    if match:
        spotify_type = match.group(1)
        spotify_id = match.group(2)
        spotify_embed = f"https://open.spotify.com/embed/{spotify_type}/{spotify_id}?utm_source=generator&theme=0"
        components.iframe(spotify_embed, height=152, scrolling=False)
    else:
        st.error("Μη έγκυρο Spotify link. Χρησιμοποίησε format: https://open.spotify.com/track/...")
