from vector_db_utils import VectorStore
from retriever import Retriever
from utils import getPyFiles

# Currently the chunking is just done in lines with no overlap, this is temporary and needs to be fixed later
def buildRetriever(directory: str, k: int):
    vector_store = VectorStore()
    file_list = getPyFiles(directory)
    lines = []
    print(file_list)
    for file_dir in file_list:
        with open(file_dir, 'r') as file:
            for line in file.readlines():
                lines.append(line)

    print(len(lines))

    vector_store.buildIndexFromChunks(chunks = lines)
    retriever = Retriever(vector_store, k)
    return retriever