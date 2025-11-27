import pandas as pd
import fastparquet

ncdDeaths = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdDeaths.parquet')
ncdDiabetesPrevalence = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdDiabetesPrevalence.parquet')
ncdHypertensionPrevalence = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdHypertensionPrevalence.parquet')
ncdMeanCholesterol = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdMeanCholesterol.parquet')
ncdMortalityRatePer100000 = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdMortalityRatePer100000.parquet')
ncdProbabilityOfDying = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdProbabiltyOfDying.parquet')
ncdTotalDeaths = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdTotalDeaths.parquet')


def validateDf(dateframe:pd.DataFrame):
    if {'Id','IndicatorCode','SpatialDim','TimeDim','Dim1','Value'}.issubset(dateframe.columns) and len(dateframe.index) > 0 and len(dateframe.columns) >= 5:
        print('Df is correct')
    else:
        print('Check dataframe')

ncdDiabetesPrevalence = ncdDiabetesPrevalence.rename(columns={'Id_x':'Id','IndicatorCode_x':'IndicatorCode','Dim1_x':'Dim1','newDim2':'Dim2','meanValue':'Value'})
validateDf(ncdDeaths)
validateDf(ncdDiabetesPrevalence)
validateDf(ncdHypertensionPrevalence)
validateDf(ncdMeanCholesterol)
validateDf(ncdMortalityRatePer100000)
validateDf(ncdProbabilityOfDying)
validateDf(ncdTotalDeaths)
