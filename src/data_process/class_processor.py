import pandas as pd

class Processor:
    def __init__(self, file):
        self.df = pd.read_csv(file, sep=',', encoding='utf-8')
    
    def insert_id(self):
        self.df.insert(0, 'id', range(1, len(self.df) + 1))