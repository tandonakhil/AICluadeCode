"""Local Flask server for the MAS knowledge base.

Serves templates/index.html — two tabs (Developers / Admins) covering the
platform end to end. Content is currently authored/embedded, mirroring
admin/MAS_REGISTRY.md and admin/ROADMAP.md by hand — wiring this to
deliverables-agent's regeneration trigger (so it updates automatically
whenever the registry changes) is tracked as a follow-up, not yet built.

Run: python app.py
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)
