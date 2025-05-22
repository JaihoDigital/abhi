import streamlit as st
from streamlit_option_menu import option_menu
import base64

# List of background images for the slideshow
background_images = [
    "images/img_bg1.jpg",
    "images/img_bg2.jpg",
    "images/img_bg3.jpg",
    "images/img_bg4.jpg",
    "images/img_bg5.jpg",
    "images/img_bg6.jpg",
    "images/img_bg7.jpg",
    "images/img_bg8.jpg"
]

# Function to add background slideshow using only CSS
def add_bg_from_local_slideshow_css(image_list, interval_sec=5):
    encoded_images = []
    for path in image_list:
        with open(path, "rb") as file:
            encoded = base64.b64encode(file.read()).decode()
            encoded_images.append(f"data:image/png;base64,{encoded}")

    num_images = len(encoded_images)
    percent_per_image = 100 / num_images

    keyframes = ""
    for i in range(num_images):
        percent_start = i * percent_per_image
        percent_end = (i + 1) * percent_per_image
        keyframes += f"""
        {percent_start}% {{ background-image: url('{encoded_images[i]}'); }}
        {percent_end}% {{ background-image: url('{encoded_images[i]}'); }}
        """

    css = f"""
    <style>
    .stApp {{
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        animation: bgSlide {interval_sec * num_images}s infinite;
        transition: background-image 1s ease-in-out;
    }}

    @keyframes bgSlide {{
        {keyframes}
    }}
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)

# Background video approach with greater separation between UI and video
def add_video_background(video_path: str):
    with open(video_path, "rb") as video_file:
        base64_video = base64.b64encode(video_file.read()).decode()
    
    # Create an HTML structure where the video is absolutely positioned
    # but we create a separate content div that will hold all UI elements
    video_html = f"""
    <style>
    /* Hide default streamlit container background and padding */
    .stApp {{
        background: none !important;
    }}
    
    /* Video background container */
    .video-background {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1000;
    }}
    
    /* Video element styling */
    .video-background video {{
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        object-fit: cover;
    }}
    
    /* Add a semi-transparent overlay to make UI elements more visible */
    .overlay {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.3);
        z-index: -999;
    }}
    
    /* Ensure form elements are visible on the video background */
    .stTextInput, .stButton, .stMarkdown, .stForm {{
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 8px !important;
        padding: 8px !important;
        margin: 8px 0 !important;
    }}
    
    /* Make form labels visible */
    .stTextInput label, .stForm label {{
        color: white !important;
        font-weight: bold !important;
        text-shadow: 1px 1px 2px black !important;
    }}
    </style>
    
    <div class="video-background">
        <video autoplay loop muted playsinline>
            <source src="data:video/mp4;base64,{base64_video}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    <div class="overlay"></div>
    """
    
    return video_html

# ----------------------------------------
# App UI starts here
# ----------------------------------------

st.set_page_config(page_title='Fission AI', page_icon='images/ai_icon.png', layout="centered")

# Insert this at the very beginning to ensure CSS is loaded before other elements
st.markdown("""
<style>
/* Global styles for better visibility */
.main .block-container {
    padding-top: 2rem;
}

h1, h2, h3, h4, h5, h6, p {
    color: white !important;
    text-shadow: 1px 1px 3px black !important;
}

.stButton > button {
    font-weight: bold !important;
    border: 1px solid #4CAF50 !important;
}

.stForm > div {
    background-color: rgba(255, 255, 255, 0.8) !important;
    padding: 15px !important;
    border-radius: 10px !important;
}

.stChatMessage {
    background-color: rgba(255, 255, 255, 0.8) !important;
    border-radius: 8px !important;
    padding: 8px !important;
    margin: 8px 0 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## FISSION AI ✨")

# Sidebar Menu
with st.sidebar:
    selected = option_menu("Fission AI ✨", ["🖼️ Generate Images", '🎞️ Generate Video'],
        icons=[' ', ' '], menu_icon=" ", default_index=0)
    # Clear button
    if st.button("🗑️ Clear History"):
        st.session_state.image_history = []

# Session state to hold history
if 'image_history' not in st.session_state:
    st.session_state.image_history = []

# Main Area
if selected == "🖼️ Generate Images":
    # Background slideshow
    add_bg_from_local_slideshow_css(background_images, interval_sec=5)

    st.subheader("AI Image Generator")
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

    # Input
    with st.form(key="image_prompt_form", clear_on_submit=True):
        prompt = st.text_input(label="Enter prompt", placeholder="e.g. cat and dog are fighting")
        submit = st.form_submit_button("Generate")
    
    # On submit
    if submit and prompt:
        response = f"🖼️ Generated image for: **{prompt}**"
        st.session_state.image_history.append((prompt, response))
    
    # Display conversation-like history
    for idx, (user_prompt, response) in enumerate(reversed(st.session_state.image_history), 1):
        with st.chat_message("user"):
            st.markdown(f"**Prompt {idx}:** {user_prompt}")
        with st.chat_message("assistant"):
            st.markdown(response)

elif selected == "🎞️ Generate Video":
    # Add background video HTML first
    video_bg_html = add_video_background("videos/bg_video.mp4")
    st.markdown(video_bg_html, unsafe_allow_html=True)
    
    # Add content with enhanced visibility
    st.markdown("""
    <div style="position: relative; z-index: 10; margin-top: 50px;">
        <h2 style="color: white; text-shadow: 2px 2px 4px #000000;">🎞️ Video Generator</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a container with custom styling to ensure visibility
    with st.container():
        st.markdown("""
        <div style="background-color: rgba(255, 255, 255, 0.7); padding: 20px; border-radius: 10px; margin-top: 20px; margin-bottom: 20px;">
            <h4 style="color: #333 !important; text-shadow: none !important; margin-top: 0;">Enter your video generation prompt below:</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Use a form with strong custom styling
        with st.form(key="video_prompt_form", clear_on_submit=True):
            st.markdown("""
            <style>
            /* Additional styling for this specific form */
            div[data-testid="stForm"] {
                background-color: rgba(255, 255, 255, 0.9) !important;
                padding: 20px !important;
                border-radius: 10px !important;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            prompt = st.text_input(label="Enter prompt", placeholder="e.g. cat and dog are fighting")
            submit = st.form_submit_button("Generate")
    
    # On submit
    if submit and prompt:
        response = f"🎞️ Generated video for: **{prompt}**"
        st.session_state.image_history.append((prompt, response))
    
    # Display history with enhanced visibility
    st.markdown("""
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 20px; border-radius: 10px; margin-top: 40px;">
        <h3 style="color: #333 !important; text-shadow: none !important; margin-top: 0;">Generation History</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Display conversation-like history with better visibility
    for idx, (user_prompt, response) in enumerate(reversed(st.session_state.image_history), 1):
        with st.container():
            st.markdown("""
            <style>
            /* Custom styling for chat messages */
            .stChatMessage {
                background-color: rgba(255, 255, 255, 0.9) !important;
                margin: 10px 0 !important;
                padding: 15px !important;
                border-radius: 10px !important;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            with st.chat_message("user"):
                st.markdown(f"**Prompt {idx}:** {user_prompt}")
            with st.chat_message("assistant"):
                st.markdown(response)