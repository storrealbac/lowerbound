import os

"""
Validate if it is a valid name, to avoid
file transversal vulnerabilities
"""
def validatePath(name: str) -> bool:
    name = normalize(name.lower())
    valid_characters = "abcdefghijklmnñopqrstuvwxyz-_"
    for c in name:
        if c not in valid_characters:
            return False
    return True

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def getAllContents():
    contents = {}
    
    all_divisions = os.listdir("docs")
    for theme in all_divisions:
        contents[theme] = {}
        all_sub_divisions = os.listdir(f"docs/{theme}")
        for sub_division in all_sub_divisions:
            all_files = os.listdir(f"docs/{theme}/{sub_division}")
            contents[theme][sub_division] = all_files

    return contents
