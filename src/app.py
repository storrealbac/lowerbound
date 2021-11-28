# Flask
from flask import Flask, render_template

# Markdown
import markdown

# CSS
from pygments.formatters import HtmlFormatter

# App
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("page/index.html", title="Inicio")

@app.route("/<folder>/<file>")
def material(folder, file):

    try:
        file = open(f"docs/{folder}/{file}.md")
    except:
        return "Error", 404

    formatter = HtmlFormatter(style="native",full=True, cssclass="codehilite")
    md_template_string = markdown.markdown(file.read(), extensions=["fenced_code", "tables", "codehilite", "mdx_math"])
    
    return render_template(
        "page/material.html",
        title="Test",
        info=md_template_string,
        styles=formatter.get_style_defs()
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
