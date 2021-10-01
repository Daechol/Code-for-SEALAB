# GOCI-II  위성영상 다운로드 튜토리얼에 사용된 Code
해당 포스트에 대한 자세한 내용은 아래 링크에서 보실 수 있습니다.
<br>
<br>
[GOCI-II 위성영상 다운로드 방법: 1편](http://sealab.kesti.info/view/166)
<br>
[GOCI-II 위성영상 다운로드 방법: 2편](http://sealab.kesti.info/view/170)
<br>
<br>
<br>
<br>

### GOCI-II Slot-7 URL list making (1 day)

```python
import arrow

seoul = arrow.get('2021-08-31 07:00')

for j in range(10):
    seoul = seoul.shift(hours=1)
    url_list = f"http://www.khoa.go.kr/nosc/satellite/down/netCDFfileDownload.do?obsTime={seoul.format('YYYY-MM-DD+HH')}%3A00&slot=7&stdTime=KST&productType="
    print(url_list)
```

<br>
<br>

### URL download

```python
import requests

urls = open('listGoci.txt', 'r')

for i, url in enumerate(urls):
    r = requests.get(url, allow_redirects=True)
    arr = url.split('=')
    open(f'{arr[1]}.nc', 'wb').write(r.content)
```

