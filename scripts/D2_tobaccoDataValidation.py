import pandas as pd

def validateDf(dateframe:pd.DataFrame):
    if {'Id','IndicatorCode','SpatialDim','TimeDim','Value'}.issubset(dateframe.columns) and len(dateframe.index) > 0 and len(dateframe.columns) >= 5:
      print('Df is correct')
    else:
      print('Check dataframe')



tobaccoAdvertisingBanAtPointOfSale = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoAdvertisingBanAtPointOfSale.parquet')
tobaccoAdvertisingBanInternet = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoAdvertisingBanInternet.parquet')
tobaccoAdvertisingBanNationalTvAndRadio = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoAdvertisingBanNationalTvAndRadio.parquet')
tobaccoAdvertisingBanOutdoor = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoAdvertisingBanOutdoor.parquet')
tobaccoAffordability = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoAffordability.parquet')
tobaccoBanInIndoorOffices = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoBanInIndoorOffices.parquet')
tobaccoBanInPublicTransport = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoBanInPublicTransport.parquet')
tobaccoBanInRestaurants= pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoBanInRestaurants.parquet')
tobaccoMostSoldCigarrete = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoMostSoldCigarrete.parquet')


validateDf(tobaccoAdvertisingBanAtPointOfSale)
validateDf(tobaccoAdvertisingBanInternet)
validateDf(tobaccoAdvertisingBanNationalTvAndRadio)
validateDf(tobaccoAdvertisingBanOutdoor)
validateDf(tobaccoAffordability)
validateDf(tobaccoBanInIndoorOffices)
validateDf(tobaccoBanInPublicTransport)
validateDf(tobaccoBanInRestaurants)
validateDf(tobaccoMostSoldCigarrete)