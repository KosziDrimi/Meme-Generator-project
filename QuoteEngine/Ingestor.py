from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    
    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
            
            

