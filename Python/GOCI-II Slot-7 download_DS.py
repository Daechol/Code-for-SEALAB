# GOCI-II Slot-7 URL list making (1 day) code
import arrow
seoul = arrow.get('2021-08-31 07:00')
for j in range(10):
    seoul = seoul.shift(hours=1)
    url_list = f"http://www.khoa.go.kr/nosc/satellite/down/netCDFfileDownload.do?obsTime={seoul.format('YYYY-MM-DD+HH')}%3A00&slot=7&stdTime=KST&productType="
    print(url_list)


# URL download code
import requests
urls = open('listGoci.txt', 'r')
for i, url in enumerate(urls):
    r = requests.get(url, allow_redirects=True)
    arr = url.split('=')
    open(f'{arr[1]}.nc', 'wb').write(r.content)

    
