import socks

# Authentication keys. Get it here: https://core.telegram.org/api/obtaining_api_id
api_id = '21430875'
api_hash = '5820acaa648e7f05007d84853d0207f7'


#proxy support
use_proxy = False
proxy_port = 9999
proxy_data = (socks.SOCKS5, 'proxy_host', proxy_port, True, 'proxy_login', 'proxy_password')


