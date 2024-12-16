from utils import getTokenizerForModel, countTokensInChunk


class Chunker:
    def __init__(self, model_name: str, model_path: str, max_chunk_size: int, overlap: int = 0):
        """
        max_chunk_size is measured in tokens in the chosen 
        """

        self.tokenizer = getTokenizerForModel(model_name, model_path)
        self.max_chunk_size = max_chunk_size
        self.overlap = overlap


    def buildChunks(self, file_path: str, chunks: list): 
        # Add support for single lines that are longer than the token count
        # + Add support for overlap
        lines = open(file_path, 'r').readlines()
        current_chunk = ""
        
        token_count = 0

        for line in lines:
            if token_count + countTokensInChunk(self.tokenizer, line) > self.max_chunk_size - 1:
                chunks.append(current_chunk)
                current_chunk = line
                token_count = countTokensInChunk(self.tokenizer, line)
            else:
                current_chunk = "".join([current_chunk, line])
        chunks.append(current_chunk)

        return chunks

       