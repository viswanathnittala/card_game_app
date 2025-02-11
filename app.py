from flask import Flask, request, jsonify, send_from_directory
import openai

app = Flask(__name__, static_folder="static")  # Specify static folder for frontend files

# Add your OpenAI API key
openai.api_key = "PLACEHOLDER KEY"

# Route to serve the frontend HTML file
@app.route("/", methods=["GET"])
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")  # Serve index.html

@app.route('/get-game', methods=['POST'])
def get_game():
    data = request.json
    number_of_players = data.get('number_of_players', 4)
    game_complexity = data.get('complexity', 'easy')

    prompt = f"Suggest a card game for {number_of_players} players with {game_complexity} complexity. Provide step-by-step instructions for a dummy game to help beginners learn it."

    try:
        # Correct API call
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Convert response object to dictionary
        response_dict = response.to_dict()

        # Extract the message content
        game_instructions = response_dict["choices"][0]["message"]["content"]

        return jsonify({
            "instructions": game_instructions,
            "success": True
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "success": False
        })

if __name__ == "__main__":
    app.run(debug=True)
