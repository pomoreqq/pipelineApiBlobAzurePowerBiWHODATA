from azure.storage.blob import BlobServiceClient,BlobClient
import os
import os
from dotenv import load_dotenv

load_dotenv()

ENV_CONNECTION_String = os.getenv('CONNECTION_STRING')



def getDetails():
    connectionString = ENV_CONNECTION_String
    containerName = 'phase6data'
    return connectionString,containerName

def getClientsWithConnectionString():
    connectionString,containerName = getDetails()
    blobServiceClient = BlobServiceClient.from_connection_string(connectionString)
    containerClient = blobServiceClient.get_container_client(containerName)
    return containerClient

def readDataFromFolder(folderPath:str):
    binaryContentOfFilesdict = dict()
    with os.scandir(folderPath) as folder:
        for i in folder:
            with open(i,'rb') as f:
                binaryContentOfFilesdict[i.name] = f.read()
    return binaryContentOfFilesdict

def uploadToBlobWithConnectionString(folderArrayOfByteDict: dict):
    connectionString,containerName = getDetails()
    for name,value in folderArrayOfByteDict.items():
        blob = BlobClient.from_connection_string(connectionString,container_name=containerName,blob_name=name)
        blob.upload_blob(value,overwrite=True)

countriesFolder = 'C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawBeforeBlob/countries'
byteDictDataCountries = readDataFromFolder(countriesFolder)

# uploadToBlobWithConnectionString(byteDictDataCountries)

alcoholDataFolder = 'C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawBeforeBlob/alcoholData'
byteDictDataAlcohol = readDataFromFolder(alcoholDataFolder)
# uploadToBlobWithConnectionString(byteDictDataAlcohol)

ncdDataFolder = 'C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawBeforeBlob/ncdData'
byteDictDataNcd = readDataFromFolder(ncdDataFolder)
# uploadToBlobWithConnectionString(byteDictDataNcd)

lifeExpectancyDataFolder = 'C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawBeforeBlob/lifeExpectancyData'
byteDictDataLifeExpectancy = readDataFromFolder(lifeExpectancyDataFolder)
uploadToBlobWithConnectionString(byteDictDataLifeExpectancy)

tobaccoDataFolder = 'C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawBeforeBlob/tobaccoData'
byteDictDataTobacco = readDataFromFolder(tobaccoDataFolder)
uploadToBlobWithConnectionString(byteDictDataTobacco)

indicatorsDataFolder = 'C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawBeforeBlob/indicators'
byteDictDataIndicators = readDataFromFolder(indicatorsDataFolder)
uploadToBlobWithConnectionString(byteDictDataIndicators)
