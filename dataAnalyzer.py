import numpy as np
import pandas as pd


class DataAnalyzer:
    def __init__(self, data):
        self.data = data
    def cleanData(self):
        missingDataRatio = self.data.isnull().mean()
        self.data[['Age','Salary','Experience']] = self.data[['Age','Salary','Experience']].fillna(self.data[['Age','Salary','Experience']].mean())
        self.data[columnsToFill] = self.data[columnsToFill].fillna(self.data[columnsToFill].mean())
        
        return self
    def featureEngineering(self):
        self.data['IncomePerExperience'] = round(self.data['Salary'] / self.data['Experience']).astype('int64')
        return self
    def featureSelection(self):
        corrMatrix = self.data.corr().abs()
        upperTri = corrMatrix.where(np.triu(np.ones(corrMatrix.shape), k = 1).astype(bool))
        toDrop = [column for column in upperTri.columns if any(upperTri[column] > 0.55)]
        self.data.drop(columns = toDrop, inplace=True)
        return self
    def analyze(self):
        """Veri Setinin temel Özelliklerini Analiz Eder"""
        print("Veri Setinin Özellikleri\n", self.data.describe())
        print('Eksik Değerleri:\n',self.data.isnull().sum())
        print('Sütun Türleri:\n',self.data.dtypes)
        return self
class AdvanceDataAnalyzer(DataAnalyzer):
    def advancedAnalysis(self):
        correlationMatrix = self.data.corr().abs()
        print("\nKorelasyon Matrixi:\n",correlationMatrix)
        return self