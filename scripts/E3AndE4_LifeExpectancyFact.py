import pandas as pd
import fastparquet
import numpy as np

lifeExpectancyAdolescentMortalityRate = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyAdolescentMortalityRate.parquet')
lifeExpectancyAdultMortality = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyAdultMortality.parquet')
lifeExpectancyAtBirth = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyAtBirth.parquet')
lifeExpectancyhaleAtBirth = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyhaleAtBirth.parquet')
lifeExpectancyNeonatalMortalityRate = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyNeonatalMortalityRate.parquet')
lifeExpectancyUnderFiveMortalityRate = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData/lifeExpectancyUnderFiveMortalityRate.parquet')


# print(lifeExpectancyAdolescentMortalityRate) # dobrze

# print(lifeExpectancyAdultMortality)

# print(lifeExpectancyAtBirth) dobrze

# print(lifeExpectancyhaleAtBirth) dobrze

# print(lifeExpectancyNeonatalMortalityRate)


# print(lifeExpectancyUnderFiveMortalityRate) dobrze


factDataFrame = pd.DataFrame(columns=['IndicatorCode','SpatialDim','TimeDim','Dim1','Value'])

factDataFrame = pd.concat([factDataFrame,lifeExpectancyAdolescentMortalityRate,lifeExpectancyAdultMortality,lifeExpectancyAtBirth,lifeExpectancyhaleAtBirth,lifeExpectancyNeonatalMortalityRate,
                          lifeExpectancyUnderFiveMortalityRate],ignore_index=True)

factDataFrame = factDataFrame.drop('Id',axis=1)

factDataFrame.to_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataProccessed/factLifeExpectancy.parquet',engine='fastparquet')
