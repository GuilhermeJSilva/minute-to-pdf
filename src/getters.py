import re as regex


def getTitle(sourceCode):
    titleRegex = r"^# ([^\n]*)"
    return regex.search(titleRegex, sourceCode).group(1)
