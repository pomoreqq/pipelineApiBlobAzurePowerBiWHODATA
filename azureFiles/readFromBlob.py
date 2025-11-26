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


def read_from_blob(blobPrefix:str):
    dictOfBlobs = dict()
    container_client = getClientsWithConnectionString()
    blob_list = container_client.list_blobs(name_starts_with=blobPrefix)
    for blob in blob_list:
        blobClient = container_client.get_blob_client(blob.name)
        data = blobClient.download_blob().readall()
        dictOfBlobs[blob.name] = data
    return dictOfBlobs


def saveToFolder(dictBlobs:dict,targetFolder:str):
    for name,data in dictBlobs.items():
        path = os.path.join(targetFolder,name)
        with open(path,'wb') as f:
            f.write(data)


def saveDynamic(dictBlobs:dict):
    for name,data in dictBlobs.items():
        prefix = ''
        for c in name:
            if c.islower():
                prefix+= c
            else:
                break
        folderPath = os.path.join('dataRawFromBlob',prefix + 'Data')
        os.makedirs(folderPath,exist_ok=True)
        filePath = os.path.join(folderPath,name)
        with open(filePath,'wb') as f:
            f.write(data)
saveDynamic(read_from_blob('alcohol'))
# saveToFolder(read_from_blob('indicators'),'C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/indicatorsData')
# saveToFolder(read_from_blob('countries'),'C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/countriesData')
# saveToFolder(read_from_blob('ncd'),'C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/ncdData')
# saveToFolder(read_from_blob('tobacco'),'C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/tobaccoData')
# saveToFolder(read_from_blob('lifeExpectancy'),'C:/Users/tomas/Pulpit/pipelineApiBlobAzurePowerBiWHODATA/dataRawFromBlob/lifeExpectancyData')