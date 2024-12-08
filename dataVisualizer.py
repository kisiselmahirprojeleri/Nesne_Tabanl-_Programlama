import matplotlib.pyplot as plt
import seaborn as sns

from dataAnalyzer import DataAnalyzer


class DataVisualizer(DataAnalyzer):
    def __init__(self, data):
        super().__init__(data)
    def plotHistogram(self):
        self.data.hist(bins = 30, figsize=(20,15))
        plt.tight_layout()
        plt.show()
    def plotCorrelationMatrix(self):
        corrMatrix = self.data.[['Age','Salary','Experience']].corr().abs()
        plt.figure(figsize =(12,8))
        sns.heatmap(corrMatrix, annot=True, cmap='coolwarm',fmt='.2f')
        plt.show()
    def plotCategorical(self):
        plt.figure(figsize=(10,6))
        sns.countplot(x='Department', hue= 'Gender', data = self.data)
        plt.show()
    
    def plotNumerical(self):
        ageSalary = self.data.groupby('Age')['Salary'].mean().sort_values(ascending=False)
        ageSalary.plot(x = 'Age', kind='bar', figsize=(16,10))
        plt.show()
    
    def advancedVisulation(self):
        sns.pairplot(self.data)
        plt.show()