import pandas as pd


tobaccoAdvertisingBanAtPointOfSale = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoAdvertisingBanAtPointOfSale.parquet')
tobaccoAdvertisingBanNationalTvAndRadio = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoAdvertisingBanNationalTvAndRadio.parquet')
tobaccoAdvertisingBanOutdoor = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoAdvertisingBanOutdoor.parquet')
tobaccoAffordability = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoAffordability.parquet')
tobaccoBanInIndoorOffices = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoBanInIndoorOffices.parquet')
tobaccoBanInPublicTransport = pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoBanInPublicTransport.parquet')
tobaccoBanInRestaurants= pd.read_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData/tobaccoBanInRestaurants.parquet')


tobaccoAdvertisingBanAtPointOfSale['stringValue'] = tobaccoAdvertisingBanAtPointOfSale['Value']

tobaccoAdvertisingBanAtPointOfSale['Value'] = tobaccoAdvertisingBanAtPointOfSale['stringValue'].apply(lambda s: s == 'Yes')
tobaccoAdvertisingBanAtPointOfSale['Value'] = tobaccoAdvertisingBanAtPointOfSale['Value'].map({True:1,False:0})


tobaccoAdvertisingBanNationalTvAndRadio['stringValue'] = tobaccoAdvertisingBanNationalTvAndRadio['Value']
tobaccoAdvertisingBanNationalTvAndRadio['Value'] = tobaccoAdvertisingBanNationalTvAndRadio['stringValue'].apply(lambda s: s == 'Yes')
tobaccoAdvertisingBanNationalTvAndRadio['Value'] = tobaccoAdvertisingBanNationalTvAndRadio['Value'].map({True:1, False:0})

tobaccoAdvertisingBanOutdoor['stringValue'] = tobaccoAdvertisingBanOutdoor['Value']
tobaccoAdvertisingBanOutdoor['Value'] = tobaccoAdvertisingBanOutdoor['stringValue'].apply(lambda s: s == 'Yes')
tobaccoAdvertisingBanOutdoor['Value'] = tobaccoAdvertisingBanOutdoor['Value'].map({True:1, False:0})

tobaccoBanInIndoorOffices['stringValue'] = tobaccoBanInIndoorOffices['Value']
tobaccoBanInIndoorOffices['Value'] = tobaccoBanInIndoorOffices['stringValue'].apply(lambda s: s == 'Yes')
tobaccoBanInIndoorOffices['Value'] = tobaccoBanInIndoorOffices['Value'].map({True:1, False:0})

tobaccoBanInPublicTransport['stringValue'] = tobaccoBanInPublicTransport['Value']
tobaccoBanInPublicTransport['Value'] = tobaccoBanInPublicTransport['stringValue'].apply(lambda s: s == 'Yes')
tobaccoBanInPublicTransport['Value'] = tobaccoBanInPublicTransport['Value'].map({True:1, False:0})

tobaccoBanInRestaurants['stringValue'] = tobaccoBanInRestaurants['Value']
tobaccoBanInRestaurants['Value'] = tobaccoBanInRestaurants['stringValue'].apply(lambda s: s == 'Yes')
tobaccoBanInRestaurants['Value'] = tobaccoBanInRestaurants['Value'].map({True:1, False:0})



concatedDf = pd.concat([tobaccoAdvertisingBanAtPointOfSale,tobaccoAdvertisingBanNationalTvAndRadio,tobaccoAdvertisingBanOutdoor,tobaccoAffordability,tobaccoBanInIndoorOffices,tobaccoBanInPublicTransport
                        ,tobaccoBanInRestaurants],ignore_index=True)
concatedDf['Value'] = concatedDf['Value'].astype('float32')

concatedDf.to_parquet('C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataProccessed/factTobacco.parquet',engine='fastparquet')