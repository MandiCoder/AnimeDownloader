from .get_response import get_response

def get_links(url:str):
    folder_key = url.split("/")[4]
    json_url = f"https://www.mediafire.com/api/1.4/folder/get_content.php?r=tymx&content_type=files&filter=all&order_by=name&order_direction=asc&chunk=1&version=1.5&folder_key={folder_key}&response_format=json"
    response = get_response(json_url)
    json:dict = response.json()
    files = json['response']['folder_content']['files']
    
    links = [file for file in files]
    return links