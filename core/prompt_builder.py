from build_vstore import buildRetriever
from utils import convertRetrievedContext


def autoCompletePrompt(working_dir: str, k: int, line: str, prev_lines: str):

    retriever = buildRetriever(working_dir, k=k)
    ctx = retriever.retrieve(line)
    ctx = convertRetrievedContext(ctx)

    return f"Use relevant references to autocomplete the rest of a line of code. Use the following references for your answer: {ctx} \nThe previous lines are: {prev_lines} \nThe code is: {line}"


def codeBaseQuery(working_dir: str, k: int, query: str):
    retriever = buildRetriever(working_dir, k=k)
    ctx = retriever.retrieve(query)
    ctx = convertRetrievedContext(ctx)

    return f"Using relevant code context, conceptually answer the following technical question about the code.\nQuestion: {query}\nAnswer: "

def findActionableCommentsPrompt():
    return f"Sort through the following code comments and determine whether the programmer who wrote them intended for further revision of the code."