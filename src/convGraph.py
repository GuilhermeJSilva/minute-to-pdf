import graphviz
import re as regex


def getGraphsFromSource(sourceCode):
    graphsCode = []
    graphsFound = regex.finditer(r"```graphviz\n([\S\s]*)```", sourceCode)
    for found in graphsFound:
        graphsCode.append((found.group(1), found.start(0), found.end(0)))
    return graphsCode


def renderGraph(operationUuid, graphCode, start, end, extension="png"):
    filename = f"/tmp/{operationUuid}-graph-{start}-{end}"
    s = graphviz.Source(graphCode, filename=filename, format=extension)
    s.render()
    return f"{filename}.{extension}"


def getMarkdownImage(filename, label=""):
    return f"![{label}]({filename})"


def replaceGraphViz(sourceCode, operationUuid=""):
    graphsCode = getGraphsFromSource(sourceCode)
    insertPointOffset = 0
    for graphCode, start, end in graphsCode:
        outFilename = renderGraph(operationUuid, graphCode, start, end)
        size = end - start
        imageCode = getMarkdownImage(outFilename)
        sourceCode = sourceCode[:start - insertPointOffset] + \
            imageCode + sourceCode[end - insertPointOffset:]
        insertPointOffset += size
    return sourceCode
