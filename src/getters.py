import re as regex


def getTitle(sourceCode):
    titleRegex = r"^# ([^\n]*)"
    return regex.search(titleRegex, sourceCode).group(1)


def retrieveCommand(sourceCode, command):
    commandRegex = regex.compile(f"!{command} ([^\n]*)")
    return regex.findall(commandRegex, sourceCode)
