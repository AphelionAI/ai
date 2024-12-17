import glob
from retriever import Retriever
from transformers import AutoTokenizer


def getTokenizerForModel(model_name: str, model_path: str):
    if model_name == 'llama':
        
        return AutoTokenizer.from_pretrained(model_path)
    
    elif model_name == 'mistral':

        return AutoTokenizer.from_pretrained(model_path)
    
    else:
        raise Exception('Model name/type not supported, please choose from Mistral or OLlama')
    

def countTokensInChunk(tokenizer, chunk: str) -> int:
    return len(tokenizer.tokenize(chunk))


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
        print('-----------------------------------------------')
    return

def convertRetrievedContext(ctx_list):
    string = ""

    for i, ctx in enumerate(ctx_list):
        string.join(i + 1 + ". " + ctx.text + '\n\n')

    return string
