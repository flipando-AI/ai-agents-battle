from src.battle.prompts import (system_message_analytics_assistant,
                                system_message_confident_founder,
                                system_message_shark_partner,
                                system_message_shy_founder)

default_agents = [
    ("Willy", system_message_shark_partner, "gpt-4-1106-preview", False, "Right"),
    ("Karin", system_message_analytics_assistant, "gpt-4-1106-preview", False, "Right"),
    ("Ernesto", system_message_confident_founder, "gpt-4-1106-preview", False, "Left"),
    ("Mica", system_message_shy_founder, "gpt-4-1106-preview", False, "Left")
]
