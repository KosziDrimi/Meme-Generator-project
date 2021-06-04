from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []
        
        with open(path) as file:
            for line in file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split('-')
                    parsed[0] = parsed[0].strip(' ').strip('"')
                    parsed[1] = parsed[1].strip(' ')
                    new_quote = QuoteModel(parsed[0], parsed[1]) 
                             
                    quotes.append(new_quote)

        return quotes