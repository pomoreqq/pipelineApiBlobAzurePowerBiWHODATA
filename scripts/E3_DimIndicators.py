import pandas as pd
import fastparquet
import numpy as np
alcoholIndicators = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/indicatorsData/indicatorsAlcohol.parquet',engine='fastparquet')
lifeExpectancyIndicators = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/indicatorsData/indicatorsLifeExpectancy.parquet')
ncdIndicators = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/indicatorsData/indicatorsNcd.parquet')
tobaccoIndicators = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/indicatorsData/indicatorsTobacco.parquet')


alcoholIndicators['Unit'] = np.nan
alcoholIndicators.iloc[0,-1] = 'Yes/No'
alcoholIndicators.iloc[1,-1] = 'Yes/Partial/No'
alcoholIndicators.iloc[2,-1] = 'Age (years)'
alcoholIndicators.iloc[3,-1] = 'grams/day'
alcoholIndicators.iloc[4,-1] = 'DALYs per 100000 population'
alcoholIndicators.iloc[5,-1] = 'Number of deaths'


lifeExpectancyIndicators['Unit'] = np.nan


lifeExpectancyIndicators.iloc[0,-1] = 'Probability (%)'
lifeExpectancyIndicators.iloc[1,-1] = 'Years'
lifeExpectancyIndicators.iloc[2,-1] = 'Years'
lifeExpectancyIndicators.iloc[3,-1] = 'Deaths per 1000 live births'
lifeExpectancyIndicators.iloc[4,-1] = 'Deaths per 1000 live births'
lifeExpectancyIndicators.iloc[5,-1] = 'Deaths per 100000 population'


ncdIndicators['Unit'] = np.nan
ncdIndicators.iloc[0,-1] = 'mmol/L'
ncdIndicators.iloc[1,-1] = '%'
ncdIndicators.iloc[2,-1] = '%'
ncdIndicators.iloc[3,-1] = 'Deaths per 100000 population'
ncdIndicators.iloc[4,-1] = 'Number Of Deaths'
ncdIndicators.iloc[5,-1] = 'probabilty (%)'

tobaccoIndicators['Unit']=  np.nan
tobaccoIndicators.iloc[0,-1] = '% of GDP'
tobaccoIndicators.iloc[1,-1] = 'USD per pack'
tobaccoIndicators.iloc[2,-1] = 'Yes/No'
tobaccoIndicators.iloc[3,-1] = 'Yes/No'
tobaccoIndicators.iloc[4,-1] = 'Yes/No'
tobaccoIndicators.iloc[5,-1] = 'Yes/No'
tobaccoIndicators.iloc[6,-1] = 'Yes/No'
tobaccoIndicators.iloc[7,-1] = 'Yes/No'
tobaccoIndicators.iloc[8,-1] = 'Yes/No'


concatedDf = pd.concat([alcoholIndicators,tobaccoIndicators,ncdIndicators,lifeExpectancyIndicators],ignore_index=True)


concatedDf.to_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataProccessed/dimIndicators.parquet',engine='fastparquet')