from curl_cffi import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from os.path import join
from os import makedirs
from tqdm import tqdm
from modules.get_response import get_response
from zipfile import ZipFile



def download_files(list_url: list[str], hilos=1):
    # file = "OVER II\OVER II - 01.zip"
    
    # with ZipFile(file, 'r') as zip:
    #     print(zip.namelist()[0])
    #     zip.extractall(path=".")
        
    # return
    
    folder_name = list_url[0].get("filename").split(" - ")[0]
    
    with ThreadPoolExecutor(max_workers=hilos) as executor:
        futures = {executor.submit(download, link, folder_name): link for link in list_url}
        for future in as_completed(futures):
            try:
                result = future.result()
                print(f"\033[F\033[K\u001b[32;1mDescarga completada para: {result}\u001b[0m")
            except Exception as e:
                print(f"Error en la descarga de {futures[future]}: {e}")



def download(data: dict, folder_name:str):
    filename = data.get("filename")
    total_size = data.get("size")
    url = data.get("links").get("normal_download")
    makedirs(folder_name, exist_ok=True)
    
    response = requests.get(url, impersonate='chrome')
    download_link = response.text.split('aria-label="Download file"')[-1].split('"')[1]
    response_stream = get_response(download_link, stream=True)
    total_size = int(response_stream.headers.get('content-length', 0))
    
    file_path = join(folder_name, filename)
    
    with open(file_path, 'wb') as file:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename, colour='green') as bar:
            for data in response_stream.iter_content(chunk_size=1024):
                file.write(data)
                bar.update(len(data))
                
    with ZipFile(file_path, 'r') as zip:
        print(zip.namelist())
        zip.extractall(path=folder_name)
        
        
    return filename