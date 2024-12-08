import pandas as pd


class DatasetReading:
    def __init__(self,filePath=None):
        self.filePath = filePath
    def readData(self):
        try:
            data = pd.read_csv(self.filePath)
            print(f'Veri Başarıyla Yüklendi. Toplam {len(data)} satır ve {len(data.columns)} sütun mevcut')
        except FileNotFoundError:
            print(f'Dosya Bulunamadı: {self.filePath}')
            data = pd.DataFrame()

        return data    
    