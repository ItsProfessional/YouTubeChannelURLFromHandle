import requests
from bs4 import BeautifulSoup


def main():
    handle = input('Enter channel handle: ')

    resp = requests.get(f'https://www.youtube.com/@{handle}')
    soup = BeautifulSoup(resp.text, 'html.parser')

    channel_id = soup.select_one('meta[property="og:url"]')['content'].strip('/').split('/')[-1]
    print(f'URL: https://www.youtube.com/channel/{channel_id}')


if __name__ == '__main__':
    main()
