import glob
from retriever import Retriever

def getPyFiles(directory: str, recursive=True):
    pattern = f'{directory}/**/*'
    fileList = []
    files = glob.glob(pattern, recursive=recursive)
    for file in files:
        if file.endswith('.py'):
            fileList.append(file)

    return fileList

def showRetrievedContext(query: str, retriever: Retriever):
    context_list = retriever.retrieve(query)
    for context in context_list:
        print(context.text, end = '\n\n')
    return

def convertRetrievedContext(ctx_list):
    string = ""

    for i, ctx in enumerate(ctx_list):
        string.join(i + 1 + ". " + ctx.text + '\n\n')

    return string
