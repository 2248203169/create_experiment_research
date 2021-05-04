import tldextract, requests, xlwt, time, random, sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from xlrd import open_workbook
from pandas import DataFrame

# 数据初始化
def init():
    global url, headers, workbook, table, row_now, get_url, todo_url, get_domin, count_layer
    get_url = []
    todo_url = []
    get_domin = []
    count_layer = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    workbook = xlwt.Workbook(encoding='utf-8')
    table = workbook.add_sheet("name", cell_overwrite_ok=True)
    row_now = 0


# 获取当前URL的页面 用BeautifulSoup解析后返回
def GetUrlCodeBS(now_url):
    req = requests.get(now_url, headers=headers)
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding
    else:
        encoding = req.encoding
    encode_content = req.content.decode(encoding, 'ignore').encode('utf-8', 'ignore')
    return BeautifulSoup(encode_content.decode('utf-8'),'lxml')


# 判断当前函数是否可以作为待选项
def TodoUrl(now_url, domain_url):
    global todo_url
    if 'javascript' in now_url:
        return 0
    elif '/' == now_url:
        return 0
    elif '#' in now_url:
        return 0
    elif 'com' in now_url:
        return 0
    elif 'cn' in now_url:
        return 0
    elif '{' in now_url:
        return 0
    else:
        todo_url.append(domain_url + now_url)


# 获取当前URL页面的title
def GetUrlTitle(now_url):
    try:
        soup = GetUrlCodeBS(now_url)
        return soup.head.title.text
    except:
        return False

    # 获取当前域名下的所有子域名


def GetSubdomain(domain_url, domain_name):
    global get_url, todo_url, get_domin
    now_domain = tldextract.extract(domain_url).domain
    soup = GetUrlCodeBS(domain_url)
    message = soup.find_all('a')
    test_1 = []
    test_1.append(domain_url)
    test_1.append(domain_name)
    get_url.append(test_1)
    #print(message)
    for data in message:
        try:
            # 判断当前的href属性是否存在
            if hasattr(data, 'href') == True:
                # 根据不同的href内容执行不同操作
                if 'http' in data['href']:
                    data_url = urlparse(data['href']).scheme + '://' + urlparse(data['href']).netloc
                    # 若当前URL的domain和当前页面的domain相同 认为此URL是当前页面的子网页或者同级网页
                    if tldextract.extract(data_url).domain == now_domain:
                        # 若当前URL的地址以及被获取过 则抛弃该URL
                        if urlparse(data_url).netloc in get_domin:
                            continue
                        test_1 = []
                        test_1.append(data_url)
                        #                     if '/' in data['href'].replace('//',''):
                        #                         url_title = GetUrlTitle(data_url)
                        #                         if url_title == False:
                        #                             continue
                        #                     else:
                        if len(data.text) > 10 or len(data.text) == 0:
                            continue
                        url_title = data.text
                        test_1.append(url_title)
                        get_domin.append(urlparse(data_url).netloc)
                        get_url.append(test_1)
                        table.write(row_now, 0, url_title)
                        table.write(row_now, 1, data_url)
                        row_now = row_now + 1
                elif 'www' in data['href']:
                    data_url = 'https://' + urlparse(data['href']).netloc
                    if tldextract.extract(data_url).domain == now_domain:
                        if urlparse(data_url).netloc in get_domin:
                            continue
                        test_1 = []
                        test_1.append(data_url)
                        #                     if '/' in data['href'].replace('//',''):
                        #                         url_title = GetUrlTitle(data_url)
                        #                         if url_title == False:
                        #                             continue
                        #                     else:
                        if len(data.text) > 10 or len(data.text) == 0:
                            continue
                        url_title = data.text
                        test_1.append(url_title)
                        get_domin.append(urlparse(data_url).netloc)
                        get_url.append(test_1)
                        table.write(row_now, 0, url_title)
                        table.write(row_now, 1, data_url)
                        row_now = row_now + 1
        #                     else:
        #                         TodoUrl(data['href'],domain_url)
        #                 else:
        #                     TodoUrl(data['href'],domain_url)
        except:
            continue
        print(data['href'])


# #     for url_new in todo_url:
# #         print(url_new)
# #         time.sleep(random.random()*10)
# #         GetSubdomain_Sub(url_new)

# 获取xls文件中的列表，逐个细化
def GetXlsToDetail():
    global get_url, get_domin
    workbook = open_workbook(r'D:/创新设计/常见域名列表_综合其他.xls')
    sheet = workbook.sheet_by_index(0)
    for i in range(sheet.nrows):
        try:
            GetSubdomain(sheet.row_values(i)[0],sheet.row_values(i)[1])
        except:
                        print('获取' + sheet.row_values(i)[1] + '网页代码失败！')
                        continue
        get_url = []
        get_domin = []


# 主函数
if __name__ == '__main__':
    init()
    GetXlsToDetail()
    workbook.save('D:/创新设计/常见域名列表_综合其他_细化(2).xls')