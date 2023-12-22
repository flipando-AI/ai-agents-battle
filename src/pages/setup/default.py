from src.battle.prompts import (system_message_analytics_assistant,
                                system_message_confident_founder,
                                system_message_shark_partner,
                                system_message_shy_founder)

default_agents = [
    ("Willy", system_message_shark_partner, "gpt-35-turbo-16k", False, "Right"),
    ("Monica", system_message_analytics_assistant, "gpt-35-turbo-16k", False, "Right"),
    ("Flipper", system_message_confident_founder, "gpt-35-turbo-16k", False, "Left"),
    ("Dwight", system_message_shy_founder, "gpt-35-turbo-16k", False, "Left")
]
