button_color = "#2e86de"
button_hover_color = "#5dade2"
background_image_url = "https://flipando-ai.github.io/email-assets/mail_1_logo.jpg"
text_color = "#34495e"
page_switcher_button_color = "#e74c3c"
page_switcher_button_hover_color = "#c0392b" 

app_styles = f"""
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


battle_styles = """
    .agent-config {
        margin-bottom: 2rem;
    }
    .subheader {
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .subheader + * {
        margin-top: 1rem;
    }
    .chat-bubble {
        padding: 10px 20px;
        border-radius: 40px;
        margin: 10px;
        display: inline-block;
        opacity: 0.5;
        max-width: 60%;
    }
    .user-message {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin: 10px 0;
    }
    .user-message .chat-bubble {
        background-color: #f0f0f0;
        opacity: 0.5;
        color: #333;
        text-align: left;
        width: auto;
        max-width: 100%;
        border-radius: 0;
        padding: 10px;
    }
    .agent-left .chat-bubble {
        background-color: #e0e0e0;
        float: left;
    }
    .agent-right .chat-bubble {
        background-color: #0084ff;
        color: white;
        float: right;
    }
    .chat-message {
        overflow: auto;
    }
    .agent-name {
        display: block;
        margin-bottom: 5px;
    }
    .agent-left .chat-bubble::after {
        content: '';
        position: absolute;
        border: 15px solid transparent;
        border-top-color: #e0e0e0;
        left: 0;
        bottom: 0;
        transform: translate(-100%, 50%);
    }
    .agent-right .chat-bubble::after {
        content: '';
        position: absolute;
        border: 15px solid transparent;
        border-top-color: #0084ff;
        right: 0;
        bottom: 0;
        transform: translate(100%, 50%);
    }
    .waiting-input {
        font-weight: bold;
        color: #004d00;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 10px;
        width: 100%;
        border-top: 1px dashed #004d00;
        border-bottom: 1px dashed #004d00;
        padding: 5px 0;
    }
"""

styles = f"<style>{battle_styles}{app_styles}</style>"
