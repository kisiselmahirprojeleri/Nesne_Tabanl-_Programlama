from dataAnalyzer import AdvanceDataAnalyzer
from dataRead import DatasetReading
from dataVisualizer import DataVisualizer


def main():
    #Veri dosyasını okuyalım
    reading = DatasetReading(filePath=r/workspace.OOP_HR_ANALYSIS/hr.csv'
    data = reading.readData()

    analyzer = AdvanceDataAnalyzer(data)
    analyzer.cleanData().featureEngineering().featureSelection().analyze().advancedAnalysis()

    visulizer = DataVisualizer(analyzer.data)
    visulizer.plotHistogram()
    visulizer.plotCorrelationMatrix()
    visulizer.plotCategorical()
    visulizer.plotNumerical()
    visulizer.advancedVisulation()

if __name__ == '__main__':
    main()