import pandas as pd
import fastparquet

alcoholAdvertisingRestricionsOnNationalTelevision = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/alcoholData/alcoholAdvertisingRestricionsOnNationalTelevision.parquet')
alcoholAttributableAllCauseDeaths = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/alcoholData/alcoholAttributableAllCauseDeaths.parquet')
alcoholAverageDailyIntake = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/alcoholData/alcoholAverageDailyIntake.parquet')
alcoholDALYs = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/alcoholData/alcoholDALYs.parquet')
alcoholExciseTaxOnBeverages = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/alcoholData/alcoholExciseTaxOnBeverages.parquet')
alcoholOffPremiseAgeSale = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/alcoholData/alcoholOffPremiseAgeSale.parquet')



def validateDf(dateframe:pd.DataFrame):
    if {'Id','IndicatorCode','SpatialDim','TimeDim','Dim1','Value'}.issubset(dateframe.columns) and len(dateframe.index) > 0 and len(dateframe.columns) >= 5:
      print('Df is correct')
    else:
      print('Check dataframe')



validateDf(alcoholAdvertisingRestricionsOnNationalTelevision)
validateDf(alcoholAttributableAllCauseDeaths)
validateDf(alcoholAverageDailyIntake)
validateDf(alcoholDALYs)
validateDf(alcoholExciseTaxOnBeverages)
validateDf(alcoholOffPremiseAgeSale)