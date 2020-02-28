import sys
import uuid
import cleanMarkdown
from convGraph import replaceGraphViz

def buildSource(sourceCode, operationUuid):
    sourceCode = replaceGraphViz(sourceCode, operationUuid=operationUuid)
    sourceCode = cleanMarkdown.removeTags(sourceCode)
    title, sourceCode = cleanMarkdown.getTitle(sourceCode)
    sourceCode = cleanMarkdown.downsizeTitles(sourceCode)
    sourceCode = cleanMarkdown.spacePoints(sourceCode)
    return cleanMarkdown.addFrontmatter(sourceCode, title)

if __name__ == "__main__":
    operationUuid = uuid.uuid1().hex
    if len(sys.argv) < 2:
        sourceCode = sys.stdin.read()
        print(buildSource(sourceCode, operationUuid))
    else:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            sourceCode = file.read()
            print(buildSource(sourceCode, operationUuid))
