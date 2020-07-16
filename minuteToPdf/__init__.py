import sys
import uuid
import cleanMarkdown
import getters
from convGraph import replaceGraphViz
from frontmatter import addFrontmatter


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


# if __name__ == "__main__":
#     operationUuid = uuid.uuid1().hex
#     if len(sys.argv) < 2:
#         sourceCode = sys.stdin.read()
#         print(buildSource(sourceCode, operationUuid))
#     else:
#         filename = sys.argv[1]
#         with open(filename, 'r') as file:
#             sourceCode = file.read()
#             print(buildSource(sourceCode, operationUuid))
