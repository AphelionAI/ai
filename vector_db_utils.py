
from llama_index.core import VectorStoreIndex, StorageContext
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


Settings.embed_model = HuggingFaceEmbedding()
# This is temporary, make them environment variables or whatever the hell they are called, like configuration file whatsamacalled
EMBED_DIMENSION = 384


class VectorStore: # Add options for different indexes and different embedding models
    def __init__(self):
        super().__init__()
        self.vector_store = FaissVectorStore(faiss_index=faiss.IndexFlatL2(EMBED_DIMENSION))
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
        self.index = None
        # Don't use ingestion pipeline and whatever, look at docs and do it manually cause ingestion pipeline is cringe
        # self.vector_store.add()

    def buildIndexFromChunks(self, chunks: list | str):
        if type(chunks) is str:
            chunks = [chunks]
        nodes = StringIterableReader().load_data(texts=chunks)
        self.index = VectorStoreIndex.from_documents(
            documents=nodes, storage_context=self.storage_context,
        )

    def hasIndex(self):
        if self.index == None:
            return False
        else:
            return True