import pandas as pd
import fastparquet
import numpy as np
alcoholAdvertisingRestricionsOnNationalTelevision = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/alcoholData/alcoholAdvertisingRestricionsOnNationalTelevision.parquet')
alcoholAttributableAllCauseDeaths = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/alcoholData/alcoholAttributableAllCauseDeaths.parquet')
alcoholAverageDailyIntake = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/alcoholData/alcoholAverageDailyIntake.parquet')
alcoholDALYs = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/alcoholData/alcoholDALYs.parquet')
alcoholExciseTaxOnBeverages = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/alcoholData/alcoholExciseTaxOnBeverages.parquet')
alcoholOffPremiseAgeSale = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/alcoholData/alcoholOffPremiseAgeSale.parquet')


alcoholAdvertisingRestricionsOnNationalTelevision['stringValue'] = alcoholAdvertisingRestricionsOnNationalTelevision['Value']
alcoholAdvertisingRestricionsOnNationalTelevision['Value'] = alcoholAdvertisingRestricionsOnNationalTelevision['Value'].apply(lambda s: s.lower())


alcoholAdvertisingRestricionsOnNationalTelevision.loc[
    alcoholAdvertisingRestricionsOnNationalTelevision['Value'].str.contains('no', na=False),
    'Value'
] = 0

alcoholAdvertisingRestricionsOnNationalTelevision.loc[
    alcoholAdvertisingRestricionsOnNationalTelevision['Value'].str.contains('partial', na=False),
    'Value'
] = 1
alcoholAdvertisingRestricionsOnNationalTelevision.loc[
    alcoholAdvertisingRestricionsOnNationalTelevision['Value'].str.contains('voluntary', na=False),
    'Value'
] = 1

alcoholAdvertisingRestricionsOnNationalTelevision.loc[
    alcoholAdvertisingRestricionsOnNationalTelevision['Value'].str.contains('ban', na=False),
    'Value'
] = 2



# print(alcoholAttributableAllCauseDeaths) jest dobrze
# print(alcoholAverageDailyIntake) jest dobrze
# print(alcoholDALYs) # jest dobrze
alcoholExciseTaxOnBeverages['stringValue'] = alcoholExciseTaxOnBeverages['Value']
alcoholExciseTaxOnBeverages['Value'] = alcoholExciseTaxOnBeverages['Value'].apply(lambda s: s.lower())
alcoholExciseTaxOnBeverages.loc[alcoholExciseTaxOnBeverages['Value'].str.contains('no',na=False),'Value'] = 0 
alcoholExciseTaxOnBeverages.loc[alcoholExciseTaxOnBeverages['Value'].str.contains('yes',na=False),'Value'] = 1
# print(alcoholExciseTaxOnBeverages) jest dobrze
# print(alcoholOffPremiseAgeSale) jest cobrze
print(alcoholAdvertisingRestricionsOnNationalTelevision)
print(alcoholAttributableAllCauseDeaths)
print(alcoholAverageDailyIntake)
print(alcoholDALYs)
print(alcoholExciseTaxOnBeverages)
print(alcoholOffPremiseAgeSale)
#30 0004   '300004'  string  // 

factDataFrame = pd.DataFrame(columns=['IndicatorCode','SpatialDim','TimeDim','Dim1','Value','stringValue'])

factDataFrame = pd.concat([factDataFrame,alcoholAdvertisingRestricionsOnNationalTelevision,alcoholAttributableAllCauseDeaths,alcoholOffPremiseAgeSale,alcoholAverageDailyIntake,alcoholDALYs,alcoholExciseTaxOnBeverages],
                          ignore_index=True)

factDataFrame = factDataFrame.drop('Id',axis=1)
factDataFrame.loc[factDataFrame['Value'] == 'Subnational'] = np.nan

factDataFrame['Value'] = factDataFrame['Value'].str.replace(' ','',regex=False).astype(np.float32)
factDataFrame.to_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataProccessed/factAlcohol.parquet',engine='fastparquet')

