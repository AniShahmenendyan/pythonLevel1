import http.client
import json
from urllib.parse import quote_plus


host = 'cb.am'


def to_dram(currency):
    """
    Convert currency to dram
    currncy: str
    return: int
    """
    connection = http.client.HTTPConnection(host)

    headers = {'Content-type': 'application/json'}

    path = '/{}?currency={}'.format('latest.json.php', quote_plus(currency))

    connection.request('GET', path, headers=headers)

    rawreply = connection.getresponse().read()

    reply = json.loads(rawreply.decode('utf-8'))

    return reply.get(currency)


if __name__ == '__main__':
    print(to_dram('USD'))
    # print(to_dram('EUR'))
