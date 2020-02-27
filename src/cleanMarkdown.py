import re as regex


def removeTags(sourceCode):
    return regex.sub(r"###### tags: .*", "", sourceCode)


def getTitle(sourceCode):
    titleRegex = r"^# ([\w\ ]*)"
    return regex.search(titleRegex, sourceCode).group(1), regex.sub(titleRegex, "", sourceCode)


def downsizeTitles(sourceCode):
    titleRegex = r"#(#* [\w\ ]*)"
    return regex.sub(titleRegex, lambda match: match.group(1), sourceCode)


def spacePoints(sourceCode):
    pointRegex = r"(\*\*[\w\ ]*\*\*: [^\n]*)\n\*"
    while regex.search(pointRegex, sourceCode) is not None:
        sourceCode = regex.sub(pointRegex, lambda match: f"{match.group(1)}\n\n*", sourceCode)
    return sourceCode 


def addFrontmatter(sourceCode, title):
    frontmatter = f"---\ntitle: {title}\ngeometry:\n- margin=2cm\n---\n"

    return frontmatter + sourceCode.strip()
