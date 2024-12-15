from build_vstore import buildRetriever
from utils import convertRetrievedContext


def autoCompletePrompt(working_dir: str, k: int, line: str, ctx: str | list):
    
    retriever = buildRetriever(working_dir, k=k)
    ctx = retriever.retrieve(line)
    ctx = convertRetrievedContext(ctx)

    return f"Use relevant references to autocomplete the rest of a line of code. Use the following references for your answer: {ctx} \nThe code is: {line}"


