from sys import stderr

templates = {
    "title": "title: \"{}\"\n",
    "author": "author: {}\n"
}


def generateFromTemplate(data, entry):
    if entry in data and entry in templates:
        return templates[entry].format(data[entry])
    print(
        f"Warning: There is no template for {entry}, so it is being ignored", file=stderr)
    return ""


def addFrontmatter(sourceCode, data={}):
    frontmatter = f"---\n"
    for entry in data:
        frontmatter += generateFromTemplate(data, entry)
    frontmatter += "geometry:\n- margin=2cm\n"
    frontmatter += "---\n"

    return frontmatter + sourceCode.strip()
