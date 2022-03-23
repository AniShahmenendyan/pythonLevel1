import requests

host = 'cb.am'
path = 'latest.json.php'


def to_dram(currency):
    """
    Convert currency to dram
    currency: str
    return: int
    """

    # https://cb.am/latest.json.php?currency=USD
    # https://cb.am/latest.json.php?currency=EUR

    response = requests.get(f'https://{host}/{path}')

    if response.status_code == 200:
        data = response.json()
        return data.get(currency)

    return None


if __name__ == '__main__':
    print(to_dram('USD'))
    print(to_dram('EUR'))
