"""
Flask web application for generating random poems.
"""
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Poem templates with placeholders for random words
POEM_TEMPLATES = [
    {
        "title": "Nature's Song",
        "lines": [
            "The {adjective} {noun} {verb} through the {place},",
            "While {animal}s {verb2} in the {adjective2} {time}.",
            "A {color} {object} {verb3} so {adjective3},",
            "In this {adjective4} world of {noun2}."
        ]
    },
    {
        "title": "Dreams and Wonders",
        "lines": [
            "In {adjective} dreams I {verb} and {verb2},",
            "Through {place}s of {color} {noun}.",
            "The {animal} {verb3} with {adjective2} {noun2},",
            "Under the {adjective3} {time}."
        ]
    },
    {
        "title": "Whispers of Time",
        "lines": [
            "{adjective} {time} brings {adjective2} {noun},",
            "Where {animal}s {verb} and {verb2}.",
            "A {color} {object} in the {place},",
            "Makes everything {adjective3} and {adjective4}."
        ]
    }
]

# Word pools for replacement
WORD_POOLS = {
    "adjective": ["beautiful", "mysterious", "gentle", "vibrant", "peaceful", "enchanting", "radiant", "serene"],
    "adjective2": ["golden", "silver", "crystal", "emerald", "crimson", "azure", "violet", "amber"],
    "adjective3": ["bright", "soft", "warm", "cool", "fresh", "sweet", "pure", "clear"],
    "adjective4": ["magical", "wonderful", "amazing", "lovely", "charming", "graceful", "elegant", "divine"],
    "noun": ["flower", "star", "river", "mountain", "ocean", "forest", "meadow", "garden"],
    "noun2": ["light", "music", "poetry", "beauty", "harmony", "wonder", "magic", "dreams"],
    "verb": ["dance", "sing", "whisper", "glide", "float", "shimmer", "sparkle", "bloom"],
    "verb2": ["play", "laugh", "wander", "soar", "rest", "gather", "celebrate", "explore"],
    "verb3": ["glows", "shines", "flows", "grows", "moves", "dances", "sings", "flies"],
    "animal": ["butterfly", "bird", "deer", "rabbit", "fox", "swan", "eagle", "dolphin"],
    "place": ["meadow", "forest", "valley", "hillside", "shore", "garden", "field", "grove"],
    "color": ["golden", "silver", "rose", "azure", "emerald", "crimson", "violet", "pearl"],
    "object": ["petal", "leaf", "stone", "feather", "shell", "dewdrop", "crystal", "bloom"],
    "time": ["morning", "evening", "twilight", "dawn", "sunset", "moonlight", "starlight", "daybreak"]
}

def generate_poem():
    """Generate a random poem by selecting a template and filling in random words."""
    template = random.choice(POEM_TEMPLATES)
    poem = {
        "title": template["title"],
        "lines": []
    }
    
    # Create a mapping of placeholder to random word
    word_choices = {}
    for placeholder, words in WORD_POOLS.items():
        word_choices[placeholder] = random.choice(words)
    
    # Fill in the template
    for line in template["lines"]:
        filled_line = line.format(**word_choices)
        poem["lines"].append(filled_line)
    
    return poem

@app.route('/')
def index():
    """Main page displaying a random poem."""
    poem = generate_poem()
    return render_template('index.html', poem=poem)

@app.route('/api/poem')
def api_poem():
    """API endpoint to get a random poem as JSON."""
    poem = generate_poem()
    return jsonify(poem)

@app.route('/new')
def new_poem():
    """Generate a new poem and redirect to main page."""
    poem = generate_poem()
    return render_template('index.html', poem=poem)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)