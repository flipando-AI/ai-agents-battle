
button_color = "#2e86de"
button_hover_color = "#5dade2"
background_color = "#f8f9fa"
text_color = "#34495e"

styles = f"""
    <style>
    .reportview-container .main .block-container{{
        max-width: 95%;
        padding: 2rem;
        
    }}
    .sidebar .sidebar-content {{
        background-color: {background_color};
        padding: 2rem;
    }}
    h1 {{
        color: {text_color};
    }}
    .stButton>button {{
        color: white;
        background-color: #27ae60;
        border: 2px solid #27ae60;
        padding: 10px 24px;
        font-size: 16px;
        line-height: 1.5;
        border-radius: 5px;
        transition: background-color 0.2s, color 0.2s;
    }}
    .stButton>button:hover {{
        color: white;
        background-color: #2ecc71;
        border-color: #2ecc71;
    }}
    .st-eb {{
        border-bottom: 1px solid {text_color};
        margin-bottom: 10px;
    }}
    </style>
"""
