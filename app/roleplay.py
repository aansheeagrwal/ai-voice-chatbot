roleplay_scenarios = {
    "school": [
        "Good morning! What’s your name?",
        "Do you like school?",
        "What is your favorite subject?"
    ],
    "store": [
        "Welcome! What do you want to buy today?",
        "How many bananas do you want?",
        "Do you want anything else?"
    ]
}

def get_scenario_prompts(topic):
    return roleplay_scenarios.get(topic, [])
