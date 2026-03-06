from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    focus = request.form['focus']
    energy = request.form['energy']
    emotion = request.form['emotion']

    score = 0

    # Focus Scoring
    if focus == "Often":
        score += 3
    elif focus == "Sometimes":
        score += 2
    else:
        score += 1

    # Energy Scoring
    if energy == "High":
        score += 3
    elif energy == "Medium":
        score += 2
    else:
        score += 1

    # Emotion Scoring
    if emotion == "Positive":
        score += 3
    elif emotion == "Neutral":
        score += 2
    else:
        score += 1

    # Mental Wellness Evaluation (No High/Low words)
    if score <= 4:
        image = "low.png.png"
        message = f"""
        Hi My Love!🌧  

        It seems your mind may need gentle care today.

        Try taking short breaks, deep breathing, or listening to calm music.
        Remember — rest is productive too.
        """

    elif score <= 7:
        image = "moderate.png.png"
        message = f"""
        Hello My Dear!🌤  

        You are maintaining a balanced state.

        A little self-care like a walk or talking to a friend
        can help you feel even better.
        """

    else:
        image = "high.png.png"
        message = f"""
        Hey Dalring!🌸  
        
        Your mental state looks strong and positive today!

        Keep up the good energy and continue doing what makes you happy.
        """

    return render_template("result.html",
                           name=name,
                           message=message,
                           image=image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
