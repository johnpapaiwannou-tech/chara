import base64
import streamlit as st
import streamlit.components.v1 as components

st.title("Για το κορίτσι μου")

st.markdown(
    "<style>div.stButton > button {display: block; margin: 0 auto;}</style>",
    unsafe_allow_html=True,
)


PHOTO_PATH = "IMG_6960.jpeg"


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
            color: #555;
            font-size: 14px;
            margin: 6px 0 20px 0;
        }}
        .love {{
            font-size: 20px;
            color: #d6336c;
            font-weight: 600;
            line-height: 1.6;
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
        // continuous rain of hearts
        for (let i = 0; i < 80; i++) {{
            setTimeout(drop, i * 150);
        }}
        setInterval(drop, 300);
        </script>
        """,
        height=760,
    )
