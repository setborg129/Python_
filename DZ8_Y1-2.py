import re

data_info = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'

regulator_item = r'(^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)).*\[(.*)\].*"([A-Z]+)\ (\/.+?) ([\d]{1,3}) (\d+)'

regular = re.findall(regulator_item, data_info)

print(regular)
