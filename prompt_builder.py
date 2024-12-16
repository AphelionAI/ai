from build_vstore import buildRetriever
from utils import convertRetrievedContext


def autoCompletePrompt(working_dir: str, k: int, line: str, prev_lines: str, ctx: str | list):

    retriever = buildRetriever(working_dir, k=k)
    ctx = retriever.retrieve(line)
    ctx = convertRetrievedContext(ctx)

    return f"Use relevant references to autocomplete the rest of a line of code. Use the following references for your answer: {ctx} \nThe previous lines are: {prev_lines} \nThe code is: {line}"


