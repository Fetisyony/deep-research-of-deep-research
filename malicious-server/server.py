from flask import Flask, Response, redirect

app = Flask(__name__)

@app.route("/admin/secrets.txt")
def info():
    with open("page.html") as page:
        HTML = page.read()
    return Response(HTML, mimetype="text/html")

@app.route('/news')
def malicious_redirect():
    print(f"> Someone visited me. Redirecting to local ip...")
    return redirect("http://localhost:8000/admin/secrets.txt", code=302)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
