import re as regex
import sys


def removeTags(sourceCode):
    return regex.sub(r"###### tags: .*", "", sourceCode)


def removeTitle(sourceCode):
    titleRegex = r"^# ([^\n]*)"
    return regex.sub(titleRegex, "", sourceCode)


def downsizeTitles(sourceCode):
    titleRegex = r"#(#* [\w\ ]*)"
    return regex.sub(titleRegex, lambda match: match.group(1), sourceCode)


def spacePoints(sourceCode):
    pointRegex = r"(\*\*[\w\ ]*\*\*: [^\n]*)\n\*"
    while regex.search(pointRegex, sourceCode) is not None:
        sourceCode = regex.sub(
            pointRegex, lambda match: f"{match.group(1)}\n\n*", sourceCode)
    return sourceCode
