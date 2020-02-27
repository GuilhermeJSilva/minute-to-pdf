import sys
import uuid
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
        print(sourceCode)
