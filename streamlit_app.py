import streamlit as st
from sentiment_and_generation import detect_sentiment, generate_text

st.set_page_config(page_title="Sentiment AI Text Generator", layout="centered")
st.markdown(
    """
    <style>
    body { 
        background-color: #1f2937; /* Dark background for professional look */
        font-family: 'Segoe UI', sans-serif; 
        color: #ffffff;
    }

    .stButton>button { 
        background: linear-gradient(90deg,#4facfe,#00f2fe); 
        color:white; 
        border-radius:10px; 
        font-weight:bold; 
        padding:0.5rem 1.2rem; 
        border:none;
    }
    .stButton>button:hover { opacity:0.9; }

    .stTextArea textarea { 
        border-radius:12px; 
        padding:10px; 
        border:1px solid #ddd; 
        background-color: #374151; 
        color: #ffffff;
    }

    .stSelectbox, .stSlider > div {
        border-radius: 8px !important;
        padding: 0.3rem !important;
        background-color: #374151 !important;
        color: #ffffff !important;
    }

    
    /* About section styling */
    .about { 
        padding:25px 20px; 
        margin-bottom:20px; 
        color: #ffffff;
    }

    .about h4 { margin-bottom:10px; }
    .about p { margin-bottom:10px; line-height:1.6; color:#ffffff; }

    /* Output boxes */
    .output-box {
        background-color: #374151;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        color: #ffffff;
    }

    /* Sentiment badge */
    .badge {
        padding: 5px 12px;
        border-radius: 6px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --- Header ---
st.title("✨ Sentiment-Aligned AI Text Generator")

# --- About Section ---
st.markdown(
    '<div class="about">'
    '<h4>About This Tool</h4>'
    '<p>The <b>Sentiment-Aligned AI Text Generator</b> is an AI-powered writing assistant that creates text aligned with the tone you want — positive, neutral, or negative.</p>'
    '<p>Simply provide a prompt, choose a sentiment (or let the AI detect it automatically), and generate high-quality paragraphs instantly.</p>'
    '<p>Designed for content creators, students, and professionals, this tool helps you write compelling, sentiment-aware text for blogs, social media, emails, essays, and more.</p>'
    '</div>',
    unsafe_allow_html=True
)

# --- Instructions ---
st.markdown("<p>Enter a prompt, choose sentiment, and get AI-generated text aligned with that sentiment!</p>", unsafe_allow_html=True)

# --- Input card ---
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    with st.form("input_form"):
        user_prompt = st.text_area("Enter your prompt:", value="Write about the value of learning continuously.", height=150)
        manual_sentiment = st.selectbox("Sentiment (optional)", options=["Auto-detect", "positive", "neutral", "negative"])
        max_len = st.slider("Max tokens", 60, 250, 120)
        num_variants = st.slider("Number of variants", 1, 3, 1)
        submitted = st.form_submit_button("Generate")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Output card ---
if submitted:
    with st.spinner("Generating your text..."):
        if manual_sentiment == "Auto-detect":
            label, conf = detect_sentiment(user_prompt)
            detected = True
        else:
            label, conf = manual_sentiment, None
            detected = False

        res = generate_text(user_prompt, sentiment_label=label, max_length=max_len, num_return_sequences=num_variants)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Results")
    
    # Colored sentiment badge
    color = {"positive": "#16a34a", "neutral": "#f59e0b", "negative": "#dc2626"}.get(res['sentiment'].lower(), "#2563eb")
    st.markdown(
        f"<span class='badge' style='background-color:{color}; color:white;'>"
        f"Sentiment: {res['sentiment']} {'(detected)' if detected else '(manual)'}"
        f"</span>", unsafe_allow_html=True
    )
    
    if conf is not None:
        st.markdown(f"**Confidence:** {conf:.2f}")

    st.subheader("Generated Paragraph(s)")
    for i, text in enumerate(res['generated'] if isinstance(res['generated'], list) else [res['generated']], start=1):
        st.markdown(f'<div class="output-box">{text}</div>', unsafe_allow_html=True)

    st.success("Done!")
    st.markdown('</div>', unsafe_allow_html=True)
