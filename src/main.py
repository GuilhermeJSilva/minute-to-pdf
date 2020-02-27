import sys
import uuid
import cleanMarkdown
from convGraph import replaceGraphViz


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            f'Missing source file.\nUsage: python {sys.argv[0]} <source-file>')
        sys.exit(-1)

    operationUuid = uuid.uuid1().hex
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        sourceCode = file.read()
        sourceCode = replaceGraphViz(sourceCode, operationUuid=operationUuid)
        sourceCode = cleanMarkdown.removeTags(sourceCode)
        title, sourceCode = cleanMarkdown.getTitle(sourceCode)
        sourceCode = cleanMarkdown.downsizeTitles(sourceCode)
        sourceCode = cleanMarkdown.spacePoints(sourceCode)
        sourceCode = cleanMarkdown.addFrontmatter(sourceCode, title)
        print(sourceCode)
