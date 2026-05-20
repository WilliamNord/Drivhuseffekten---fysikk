from flask import Flask, render_template, request

app = Flask(__name__)

# Konstantene
sigma = 5.67e-8
S0 = 1361


def temperatur_uten_atmosfare(albedo):
    inn = S0 / 4 * (1 - albedo)
    T = (inn / sigma) ** 0.25
    return T - 273.15


def temperatur_med_drivhuseffekt(albedo, epsilon):
    inn = S0 / 4 * (1 - albedo)

    # Enkel drivhusmodell
    ut = inn / (1 - epsilon / 2)

    T = (ut / sigma) ** 0.25
    return T - 273.15


@app.route("/", methods=["GET", "POST"])
def index():

    temp_uten = None
    temp_med = None

    if request.method == "POST":

        albedo = float(request.form["albedo"])
        epsilon = float(request.form["epsilon"])

        temp_uten = temperatur_uten_atmosfare(albedo)
        temp_med = temperatur_med_drivhuseffekt(albedo, epsilon)

    return render_template(
        "index.html",
        temp_uten=temp_uten,
        temp_med=temp_med,
        epsilon=epsilon
    )


if __name__ == "__main__":
    app.run(debug=True, port=5005)