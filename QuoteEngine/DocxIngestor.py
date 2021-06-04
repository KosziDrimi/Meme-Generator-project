from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []
        
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split('-')
                parsed[0] = parsed[0].strip(' ').strip('"')
                parsed[1] = parsed[1].strip(' ')
                new_quote = QuoteModel(parsed[0], parsed[1]) 
                             
                quotes.append(new_quote)

        return quotes