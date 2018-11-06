

from __future__ import print_function

import io

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from httplib2 import Http
from oauth2client import file, client, tools
from pathlib import Path
import pyunpack

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

def connect_to_drive():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('../../credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=40, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])


    raw_png_id = None

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
            if(item["name"] == "data_png_128.rar"):
                raw_png_id = item["id"]
    if raw_png_id is not None:
        download_file(service, raw_png_id, "../../data/raw/data_png.rar")
    return "../../data/raw/data_png.rar"

def download_file(drive_service, file_id: str, filename:str):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(filename, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print( "Download %d%%." % int(status.progress() * 100))

def is_dataset_downloaded() -> bool:
    data_file_path = Path("../../data/raw/data_png.rar")
    return data_file_path.exists()


def extract_data(from_path: Path, to_path:str):
    archive = pyunpack.Archive(str(from_path))
    archive.extractall(str(to_path), True)

def main():
    path = Path("../../data/raw/data_png.rar")
    if not is_dataset_downloaded():
        path = connect_to_drive()
    extract_data(path, "../../data/raw/data_png/")



if __name__ == '__main__':
    main()