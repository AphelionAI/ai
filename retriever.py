from vector_db_utils import VectorStore
from llama_index.core import VectorStoreIndex

class Retriever:
    def __init__(self, vector_store: VectorStore, k: int):
        super().__init__()

        self.k = k
        self.vector_store = vector_store
        self.retriever = vector_store.index.as_retriever(similarity_top_k=k)
    
    def updateRetrieverWithNewIndex(self):
        self.retriever = self.vector_store.index.as_retriever(similarity_top_k=self.k)

    def retrieve(self, query):
        return self.retriever.retrieve(query)
        