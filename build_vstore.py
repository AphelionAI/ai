from vector_db_utils import VectorStore
from retriever import Retriever
from utils import getPyFiles
from chunking import Chunker
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Currently the chunking is just done in lines with no overlap, this is temporary and needs to be fixed later
def buildRetriever(model_name: str, model_path: str, directory: str, embed_name: str, k: int = 8, max_chunk_size: int = 128):
    if embed_name == 'huggingface':
        embed_model = HuggingFaceEmbedding()
        embed_dim = 384
    else:
        embed_model = None
        embed_dim = 0
    chunker = Chunker(model_name, model_path, max_chunk_size)

    vector_store = VectorStore(embed_model, embed_dim)
    file_list = getPyFiles(directory)
    chunks = []
    
    for file_dir in file_list:
        chunker.buildChunks(file_dir, chunks)
        

    vector_store.buildIndexFromChunks(chunks = chunks)
    retriever = Retriever(vector_store, k)
    return retriever