import re as regex


def getTitle(sourceCode):
    titleRegex = r"^# ([^\n]*)"
    finding = regex.search(titleRegex, sourceCode)
    if finding is not None:
        return finding.group(1)
    return ""


def retrieveCommand(sourceCode, command):
    commandRegex = regex.compile(f"!{command} ([^\n]*)")
    return regex.findall(commandRegex, sourceCode)
