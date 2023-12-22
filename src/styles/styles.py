button_color = "#2e86de"
button_hover_color = "#5dade2"
background_image_url = "https://flipando-ai.github.io/email-assets/mail_1_logo.jpg"
text_color = "#34495e"
page_switcher_button_color = "#e74c3c"
page_switcher_button_hover_color = "#c0392b" 

styles = f"""
    <style>
    body {{
        background: url({background_image_url}) no-repeat center center fixed;
        background-size: cover;
    }}
    .reportview-container .main {{
        padding-top: 0rem;
    }}
    .reportview-container .main .block-container{{
        padding-top: 0rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 2rem;
        background-color: transparent;
    }}

    .sidebar .sidebar-content {{
        background-color: transparent;
        padding: 2rem;
    }}
    h1 {{
        color: {text_color};
    }}
    </style>
"""

