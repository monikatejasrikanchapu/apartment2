from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Flat data with floor, direction text, and layout coordinates (x,y) in px
flat_data = {
    "101": {"floor": 1, "direction": "Left side near the steps", "coords": [50, 100]},
    "102": {"floor": 1, "direction": "Right side near the lift", "coords": [200, 100]},
    "103": {"floor": 1, "direction": "Opposite side across open space from 102", "coords": [150, 180]},
    
    "201": {"floor": 2, "direction": "Left side near the steps", "coords": [50, 100]},
    "202": {"floor": 2, "direction": "Right side near the lift", "coords": [200, 100]},
    "203": {"floor": 2, "direction": "Opposite side across open space from 202", "coords": [150, 180]},
    
    "301": {"floor": 3, "direction": "Left side near the steps", "coords": [50, 100]},
    "302": {"floor": 3, "direction": "Right side near the lift", "coords": [200, 100]},
    "303": {"floor": 3, "direction": "Opposite side across open space from 302", "coords": [150, 180]},
    
    "401": {"floor": 4, "direction": "Left side near the steps", "coords": [50, 100]},
    "402": {"floor": 4, "direction": "Right side near the lift", "coords": [200, 100]},
    "403": {"floor": 4, "direction": "Opposite side across open space from 402", "coords": [150, 180]},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_flat_info', methods=['POST'])
def get_flat_info():
    user_input = request.json.get("flat_number")
    flat_info = flat_data.get(user_input)
    if flat_info:
        response = {
            "floor": flat_info["floor"],
            "direction": flat_info["direction"],
            "coords": flat_info["coords"],
            "message": f"Flat {user_input} is on floor {flat_info['floor']}. Directions: {flat_info['direction']}."
        }
    else:
        response = {"message": "Sorry, I don't have information about that flat."}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

  
