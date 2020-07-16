import sys
import requests
import uuid
from .convGraph import replaceGraphViz
from .frontmatter import addFrontmatter
import minuteToPdf.cleanMarkdown as cleanMarkdown
import minuteToPdf.getters as getters
import pypandoc


def buildData(sourceCode, pipeline):
    options = {}
    for field, getter in pipeline:
        options[field] = getter(sourceCode)
    return options


def modifyCode(sourceCode, pipeline):
    code = sourceCode
    for step in pipeline:
        if callable(step):
            code = step(code)
        else:
            print(
                f"Warning: object {step} is not a function and it is being ignored.", file=sys.stderr)
    return code


def buildSource(sourceCode, operationUuid):
    getterPipeline = [
        ("title", getters.getTitle),
        ("author", lambda code: getters.retrieveCommand(code, "author"))
    ]

    modifyPipeline = [
        lambda code: replaceGraphViz(code, operationUuid),
        lambda code: cleanMarkdown.removeCommands(code, ["author"]),
        cleanMarkdown.removeTags,
        cleanMarkdown.removeTitle,
        cleanMarkdown.downsizeTitles,
        cleanMarkdown.spacePoints
    ]

    data = buildData(sourceCode, getterPipeline)
    cleanCode = modifyCode(sourceCode, modifyPipeline)
    return addFrontmatter(cleanCode, data)


def parseMarkdown(sourceCode):
    operationUuid = uuid.uuid1().hex
    return buildSource(sourceCode, operationUuid)


def getSourceFromURL(url: str):
    return requests.get(url).text


def getSourceFromFile(filename: str):
    file = open(filename, "r")
    return file.read()


def getSourceFromStdin():
    return sys.stdin.read()

def convertToPdf(markdownSource: str, filename: str):
    return pypandoc.convert_text(markdownSource, "pdf", format="md", outputfile=filename)