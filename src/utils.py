import os

"""
Validate if it is a valid name, to avoid
file transversal vulnerabilities
"""
def validatePath(name: str) -> bool:
    name = name.lower()
    valid_characters = "abcdefghijklmnñopqrstuvwxyz-_"
    for c in name:
        if c not in valid_characters:
            return False
    return True


def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))



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
