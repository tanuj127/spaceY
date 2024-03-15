import cv2
import matplotlib.pyplot as plt
import requests
import csv
from io import StringIO
import pandas as pd
from io import BytesIO
import numpy as np
from PIL import Image
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from PIL import Image
import numpy as np
import cv2
from io import BytesIO

#Importing the modules
import openpyxl

import base64  # Import base64 module

# import gsheet csv

csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRaKnGD-LiM4Kghdwey9yjfLaMujVpfgjGx4TLFlieM2AtzkB-NGFj26pOpYStY94o9n58QJCc0GhdO/pub?gid=1954586132&single=true&output=csv'
response = requests.get(csv_url)

# Convert the response to df
if response.status_code == 200:
    csv_data = response.text
    df = pd.read_csv(StringIO(csv_data))
    print(df)
else:
    print(f'Error: {response.status_code}')

image= df['Upload XRay Image'][4] 
image

import gdown

drive_url = 'https://drive.google.com/uc?id=1RsPKVXsLy-ID4Pg7sVFH3mmndYb7TxUe'
destination_path = 'desire.jpg'
gdown.download(drive_url, destination_path, quiet=False)

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Initialize GoogleAuth object with the client_secrets_file parameter
from pydrive.auth import GoogleAuth

# Initialize GoogleAuth object
gauth = GoogleAuth()

# Perform authentication
gauth.LocalWebserverAuth()  # For authentication with your Google account

# ID of the file you want to make public
file_id = '1RsPKVXsLy-ID4Pg7sVFH3mmndYb7TxUe'

# Retrieve the file
file = drive.CreateFile({'id': file_id})

# Fetch metadata
file.FetchMetadata()

# Make the file publicly accessible
file.InsertPermission({
    'type': 'anyone',
    'value': 'anyone',
    'role': 'reader'
})

# Download the file
destination_path = 'desired.jpg'
file.GetContentFile(destination_path)

print(f"File '{destination_path}' downloaded successfully.")
