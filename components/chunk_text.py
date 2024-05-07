import os
import sys
from pathlib import Path

from langchain.text_splitter import RecursiveCharacterTextSplitter
import pandas as pd

from utils.helper import read_yaml, read_doc
from utils.logger import logging

class Chunk():
    """
    
    """

    def __init__(self, 
            text: str,
            chunk_dir: Path):
        self.text = text
        self.chunk_dir = chunk_dir

    def chunk_text(self):
        try:
            # chunk text using langchain textsplitter
            text_splitter = RecursiveCharacterTextSplitter(
                                    chunk_size =  300,
                                    chunk_overlap = 50
                                    )
            
            text_chunk = text_splitter.split_text(self.text)
            logging.info("text chuck created")
            return text_chunk
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def save_chunks(self, text_chunk):
        try:
            chunk_df = pd.DataFrame({"text_chunk": text_chunk}, index = range(1, len(text_chunk) + 1))
            chunk_df.to_csv(self.chunk_dir, index = False)

        except Exception as e:
            raise CustomeException(e, sys)
