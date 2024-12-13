
from llama_index.core import VectorStoreIndex
from llama_index.readers.string_iterable import StringIterableReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.core.text_splitter import SentenceSplitter
from llama_index.core import Settings
from dotenv import load_dotenv
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from transformers import pipeline as pl

import faiss
import os
import sys
import torch
import pandas as pd


# This is temporary, make them environment variables or whatever the hell they are called, like configuration file whatsamacalled
EMBED_DIMENSION = 768


class VectorStore: # Add options for different indexes and different embedding models
    def __init__(self):
        super().__init__()
        self.vector_store = FaissVectorStore(faiss_index=faiss.IndexFlatL2(EMBED_DIMENSION))
        # Don't use ingestion pipeline and whatever, look at docs and do it manually cause ingestion pipeline is cringe
        # self.vector_store.add()

    def addToVectorStore(self, chunks: list | str):
        if type(chunks) is str:
            chunks = [chunks]
        nodes = self.embed_model(StringIterableReader().load_data(texts=chunks))
        self.vector_store.add(nodes)   

    def getIndex(self):
        return VectorStoreIndex.from_vector_store(self.vector_store)
