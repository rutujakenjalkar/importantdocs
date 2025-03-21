import firebase_admin
from firebase_admin import db,credentials
import pandas as pd 
import os 
import zipfile
import requests
import json
import shutil

cred=credentials.Certificate("C:\\Users\\Abhay\\Downloads\\web3user-d60b4-firebase-adminsdk-fbsvc-12c23de398.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://web3user-d60b4-default-rtdb.firebaseio.com/"})

ref = db.reference("/")

data = ref.get()


document_list=data['Authentication'].values()
walletaddress_list=[]

#obtain all the wallet in the response at the backend

for document in (document_list):
   walletaddress_list.append(document['walletaddress'])

print(walletaddress_list)

#check if the wallet exists in the directory & do the operations required

for wallet in walletaddress_list:
   path="C:\\Users\\Abhay\\Documents\\internimage\\wallet_data"
   print(wallet)
  
   new_folder_path = os.path.join(path,wallet)  #used to create the address

   if os.path.exists(new_folder_path)==True:
     print("the folder already exists")
        
   else:
     os.chdir("C:\\Users\\Abhay\\Documents\\internimage\\wallet_data")
     sanitized_wallet = wallet.strip().replace("\t", "").replace(" ", "_")
     print(sanitized_wallet)
     os.mkdir(sanitized_wallet)
     print("wallet created succesfully")

     new_folder_path = os.path.join(os.getcwd(), sanitized_wallet)
   
     for document in document_list:
        if document['walletaddress'] == wallet:
          file_name = "details.txt"
          file_path = os.path.join(new_folder_path,file_name)
          try:
             with open(file_path, "w") as file:
               file.write(f"character name: {document['charactername']}\ncharacter description: {document['characterdescription']}\n")
               print("file created")
               
          except Exception as e:
                print(f"An error occurred: {e}")
           
          #creating an image formatted list for the zip file creation
          image_url_list = document['uploadedurllist']  
          print(image_url_list)



          #file to download image before storing them
          image_folder = os.path.join(new_folder_path, "downloaded_images")
          zip_filename = os.path.join(new_folder_path, "images.zip")
          os.makedirs(image_folder, exist_ok=True)

          print(f"Folder '{image_folder}' is ready!")
          for idx, url in enumerate(image_url_list):

            url = url.strip()  # Remove any leading/trailing spaces and brackets

            if not url:
               print(f"Skipping empty URL at index {idx}")
               continue


            # Validate if the URL is correct
            if not url.startswith("http"):
               print(f"Skipping invalid URL: {url}")
               continue   

            image_path = os.path.join(image_folder, f"image_{idx + 1}.jpg")  # Naming files
    
            try:
               response = requests.get(url, stream=True)  # Download image
               if response.status_code == 200:
                  with open(image_path, "wb") as file:
                     for chunk in response.iter_content(1024):  # Write image in chunks
                        file.write(chunk)
                  print(f"Downloaded: {image_path}")
               else:
                     print(f"Failed to download {url}")
            except Exception as e:
                print(f"Error downloading {url}: {e}")
            with zipfile.ZipFile(zip_filename, "w") as zipf:
               for file in os.listdir(image_folder):  # Loop through downloaded images
                  file_path = os.path.join(image_folder, file)  # Get full path
                  zipf.write(file_path, os.path.basename(file_path))  # Add to ZIP
                  print(f"Added {file} to ZIP")

          zip_filepath = os.path.join(new_folder_path, zip_filename)
          print(f"ZIP file created successfully: {zip_filepath}")

          #delete the the download_image folder from the directory
          shutil.rmtree(image_folder)
          print("folder deleted")



          

           
           




    



   
   
   


    

