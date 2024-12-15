from modules.download_files import download_files
from modules.get_links import get_links


def main():
    url = "https://www.mediafire.com/folder/s9t1cnh3o88h4/OVER_II#s9t1cnh3o88h4"
    links = get_links(url)
    download_files(links)


if __name__ == '__main__':
    main()