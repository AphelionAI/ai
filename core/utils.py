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

def detectSingleLineComments(line):
    hashtags = [m.start() for m in re.finditer('#', line)]

    if len(hashtags) != 0:
        single_quotes = [m.start() for m in re.finditer('\'', line)]
        temp = []
        for single_quote in single_quotes:
            if single_quote != 0:
                if line[single_quote - 1] != '\\':
                    temp.append(single_quote)
            else:
                temp.append(single_quote)
        single_quotes = temp

        if hashtags[0] == 0:
            return line[1:]
        else:
            for hashtag in hashtags:
                combined = single_quotes + [hashtag]
                combined.sort()
                if (combined.index(hashtag) + 1) % 2 != 0:
                    return line[hashtag + 1:]
                
        double_quotes = [m.start() for m in re.finditer('\'', line)]
        temp = []
        for double_quote in double_quotes:
            if double_quote != 0:
                if line[double_quote - 1] != '\\':
                    temp.append(double_quote)
            else:
                temp.append(double_quote)
        double_quotes = temp

        if hashtags[0] == 0:
            return line[1:]
        else:
            for hashtag in hashtags:
                combined = double_quotes + [hashtag]
                combined.sort()
                if (combined.index(hashtag) + 1) % 2 != 0:
                    return line[hashtag + 1:]
                
    else:
        return None