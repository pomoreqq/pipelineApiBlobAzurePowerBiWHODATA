import pandas as pd

def validateDf(dateframe:pd.DataFrame):
    if {'Id','IndicatorCode','SpatialDim','TimeDim','Dim1','Value'}.issubset(dateframe.columns) and len(dateframe.index) > 0 and len(dateframe.columns) >= 5:
      print('Df is correct')
    else:
      print('Check dataframe')



lifeExpectancyAdolescentMortalityRate = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyAdolescentMortalityRate.parquet')
lifeExpectancyAdultMortality = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyAdultMortality.parquet')
lifeExpectancyadultMortalityRate = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyadultMortalityRate.parquet')
lifeExpectancyAtBirth = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyAtBirth.parquet')
lifeExpectancyhaleAtBirth = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyhaleAtBirth.parquet')
lifeExpectancyNeonatalMortalityRate = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyNeonatalMortalityRate.parquet')
lifeExpectancyUnderFiveMortalityRate = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyUnderFiveMortalityRate.parquet')



validateDf(lifeExpectancyAdolescentMortalityRate)
validateDf(lifeExpectancyAdultMortality)
validateDf(lifeExpectancyadultMortalityRate)
validateDf(lifeExpectancyAtBirth)
validateDf(lifeExpectancyhaleAtBirth)
validateDf(lifeExpectancyNeonatalMortalityRate)
validateDf(lifeExpectancyUnderFiveMortalityRate)