from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./_data/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', '-layout', path, tmp])
     
        file = open(tmp, 'r')
        
        quotes = []
        
        for line in file.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                parsed[0] = parsed[0].strip(' ').strip('"')
                parsed[1] = parsed[1].strip(' ')
                new_quote = QuoteModel(parsed[0], parsed[1]) 
                             
                quotes.append(new_quote)

        file.close()
        os.remove(tmp)
        
        return quotes