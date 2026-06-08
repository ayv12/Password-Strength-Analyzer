from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    message = ""
    strength = ""

    if request.method == "POST":

        password = request.form["password"]

        pass_len = len(password)

        has_upper = False
        has_lower = False
        has_number = False
        has_special = False

        special_char = "!?*&%$_"

        for char in password:

            if char.isupper():
                has_upper = True

            if char.islower():
                has_lower = True

            if char.isdigit():
                has_number = True

            if char in special_char:
                has_special = True

        # Strength points
        points = 0

        if pass_len >= 8:
            points += 1

        if has_upper:
            points += 1

        if has_lower:
            points += 1

        if has_number:
            points += 1

        if has_special:
            points += 1

        # Strength Level

        if points <= 2:
            strength = "weak"

        elif points <= 4:
            strength = "medium"

        else:
            strength = "strong"

        # Validation Messages

        if (
            pass_len >= 8
            and has_upper
            and has_lower
            and has_number
            and has_special
        ):

            message = """
            <div style='background:#00ff88;
            color:black;
            padding:15px;
            border-radius:10px;
            font-weight:bold;
            text-align:center;'>
            ✅ Strong Password
            </div>
            """

        else:

            if pass_len < 8:
                message += "❌ Password must be at least 8 characters long<br>"

            if not has_upper:
                message += "❌ Password needs an uppercase letter<br>"

            if not has_lower:
                message += "❌ Password needs a lowercase letter<br>"

            if not has_number:
                message += "❌ Password needs a number<br>"

            if not has_special:
                message += "❌ Password needs a special character<br>"

    return render_template(
        "index.html",
        message=message,
        strength=strength
    )

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=10000)