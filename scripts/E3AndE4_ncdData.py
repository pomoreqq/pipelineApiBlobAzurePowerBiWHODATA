import pandas as pd
import fastparquet

ncdDiabetesPrevalence = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdDiabetesPrevalence.parquet')
ncdHypertensionPrevalence = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdHypertensionPrevalence.parquet')
ncdMeanCholesterol = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdMeanCholesterol.parquet')
ncdMortalityRatePer100000 = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdMortalityRatePer100000.parquet')
ncdProbabilityOfDying = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdProbabiltyOfDying.parquet')
ncdTotalDeaths = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData/ncdTotalDeaths.parquet')

countriesDf = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/countriesData/countriesData.parquet')
# print(ncdDeaths) # dobre
ncdDiabetesPrevalence = ncdDiabetesPrevalence.rename(columns={'Id_x':'Id','IndicatorCode_x':'IndicatorCode','Dim1_x':'Dim1','meanValue':'Value'})
# print(ncdDiabetesPrevalence) dobre

# print(ncdHypertensionPrevalence) dobre

# print(ncdMeanCholesterol)

print(ncdMortalityRatePer100000)
ncdProbabilityOfDying = ncdProbabilityOfDying.loc[ncdProbabilityOfDying['SpatialDim'].isin(countriesDf['Code'])]
ncdProbabilityOfDying = ncdProbabilityOfDying[['Id','IndicatorCode','SpatialDim','TimeDim','Dim1','Value']]
# print(ncdProbabilityOfDying) dobrze


# print(ncdTotalDeaths)  dpbrze

concatedDf = pd.concat([ncdDiabetesPrevalence,ncdHypertensionPrevalence,ncdMeanCholesterol,ncdMortalityRatePer100000,ncdProbabilityOfDying,ncdTotalDeaths],ignore_index=True)
concatedDf = concatedDf.drop(['Id','newDim2'],axis=1)


concatedDf.to_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataProccessed/factNcd.parquet',engine='fastparquet')