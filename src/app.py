# Flask
from flask import Flask, render_template

# Markdown
import markdown

# CSS
from pygments.formatters import HtmlFormatter

# Utils
from utils import validatePath, getAllContents

# App
app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "page/index.html", 
        title="Inicio",
        contents=getAllContents())

@app.route("/<theme>/<folder>/<file_name>")
def material(theme, folder, file_name):

    if not validatePath(theme):
        return "Error 1", 404

    if not validatePath(folder):
        return "Error 2", 404
    
    if not validatePath(folder):
        return "Error 3", 404

    try:
        file = open(f"docs/{theme}/{folder}/{file_name}.md")
    except:
        return "Error 4", 404

    formatter = HtmlFormatter(style="native",full=True, cssclass="codehilite")
    md_template_string = markdown.markdown(file.read(), extensions=["fenced_code", "tables", "codehilite", "mdx_math"])
    
   

    return render_template(
        "page/material.html",
        title=file_name.replace("_", " "),
        info=md_template_string,
        styles=formatter.get_style_defs()
    )

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
