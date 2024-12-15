from requests import get
from user_agent import generate_user_agent


def get_response(url:str, stream=False):
    response = get(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, 
        allow_redirects=False,
        stream=stream
    )
    return response

