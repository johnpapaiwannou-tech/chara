import base64
import os
import streamlit as st
import streamlit.components.v1 as components

st.title("Για το κορίτσι μου")

st.markdown(
    "<style>div.stButton > button {display: block; margin: 0 auto;}</style>",
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ff6b6b, #c0392b);
        min-height: 100vh;
    }
    .stApp {
        background: transparent;
    }
    h1 {
        color: #000;
        text-shadow: 0 1px 6px rgba(0,0,0,0.7), 0 0 20px rgba(255,255,255,0.9);
        font-weight: 800;
    }
    p, .stMarkdown {
        color: #000;
        text-shadow: 0 1px 4px rgba(0,0,0,0.6), 0 0 10px rgba(255,255,255,0.7);
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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
                    I will always love you. <br/>
                    I will always be your everything.<br/>
                    I will always be your soulmate.
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
            width: 100%;
            border-radius: 12px;
            display: block;
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
    images_b64 = []
    for photo in photo_files:
        images_b64.append(get_image_base64(os.path.join(UPLOAD_DIR, photo)))
    
    images_json = str(images_b64)
    
    components.html(
        f"""
        <div class="gallery-container">
            <img id="slide" class="slide-image" src="data:image/jpeg;base64,{images_b64[0]}" />
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
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
            object-fit: contain;
        }}
        .counter {{
            color: #000;
            font-weight: 600;
            text-shadow: 0 1px 4px rgba(0,0,0,0.6), 0 0 10px rgba(255,255,255,0.7);
            margin-top: 15px;
            font-size: 16px;
        }}
        </style>
        
        <script>
        const images = {images_json};
        let index = 0;
        const slide = document.getElementById("slide");
        const counter = document.getElementById("counter");
        
        function showSlide(i) {{
            slide.src = "data:image/jpeg;base64," + images[i];
            counter.textContent = (i + 1) + " / " + images.length;
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
