from flask import Flask, render_template, request, send_from_directory
import generate

app = Flask(__name__)
CONTRACT_FOLDER = "static/contracts"
app.config['CONTRACT_FOLDER'] = CONTRACT_FOLDER

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        law = request.form["lawyer"]
        client = request.form["client"]
        service = request.form["service"]
        comp = request.form["comp"]
        deposit = request.form["deposit"]
        deposit_date = request.form["deposit_date"]
        jur = request.form["jur"]

        # Now we need to use this information to generate the contract in docx format
        filename = generate.generate(app, law, client, service, comp, deposit, deposit_date, jur)
        #return f"Hey, you pressed the button, {law} {client} {service} {comp} {deposit} {deposit_date} {jur}"
        # we need to give the contract as a download:
        return send_from_directory(app.config['CONTRACT_FOLDER'], filename, as_attachment=True)
    else:
        # this means we are on a regular get
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
