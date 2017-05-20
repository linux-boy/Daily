import optparse
import urllib2, urllib


zone_code={'hd02.upload.inner.cn-OTHER':'8a5f6a2d0d504e98a5f3ba2482a4292a',
'hd02.upload.inner.cn-YD':'ffdaded6356645c8a2d16f04d689c39a',
'hd02.upload.inner.cn-LT':'e496b8ab46474ea2b3982c778cb74200',
'hd02.upload.inner.cn-DX':'8eb393bb7cc94d83b6fefa5fb6120a8a',
'hd01.upload.inner.cn-OTHER':'20be3f837f634585858449ff4760a297',
'hd01.upload.inner.cn-LT':'37f42fd901124ddbaea4d6d14fe0789d',
'hd01.upload.inner.cn-YD':'60a24e4775104511a2a031317e22645b',
'hd01.upload.inner.cn-DX':'242d63f667a445e1b3d1b8412976f9d5',
'xn02.upload.inner.cn-DX':'cfa70989e3db4eca8bd8de387c86a73d',
'xn02.upload.inner.cn-LT':'58f858a9365a4658a584df2e02c837a4',
'xn02.upload.inner.cn-YD':'d42f1a04a7bd402c8f80fa71aa635125',
'xn02.upload.inner.cn-OTHER':'2b012990916246279fbe890257c27d70',
'xn01.upload.inner.cn-LT':'fbfc47d42f444f748bff2aeb39306ae6',
'xn01.upload.inner.cn-YD':'2fb8d3931ed849d7a1ca45359e230b1f',
'xn01.upload.inner.cn-DX':'513871a5d8ec4143a0e5b7c8073a039e',
'xn01.upload.inner.cn-OTHER':'c1fc1d4d74b54608b419513b06c457ca',
'hn02.upload.inner.cn-OTHER':'31e3857feb3d4c51a541b673591e8e50',
'hn02.upload.inner.cn-YD':'392b391e539540c5bbf70c0e5aa2e14e',
'hn02.upload.inner.cn-DX':'997f8a20e3d04c7b9e1a658e4174efba',
'hn02.upload.inner.cn-LT':'6b4bd1dbb9714df9a833898dc1fb5330',
'hn01.upload.inner.cn-DX':'adeae072bda646769d1dcb6bd72b43c6',
'hn01.upload.inner.cn-LT':'b5c3156f5a7e4fcba3487d4a5a58cda3',
'hn01.upload.inner.cn-YD':'015bc849e04c4d26bf5887be2ac66719',
'hn01.upload.inner.cn-OTHER':'a1307c66142949adb727ab0b5d3a4404'}


def diff_value():
    opt = optparse.OptionParser()
    opt.add_option("-f", '--file', dest='filename', 
        help='write report to File',metavar='FILE')
    (opention, args) = opt.parse_args()
    return opention.filename

def read_file():
    filename = diff_value()
    print ('filename: %s'%filename)
    with open(filename, 'r') as file:
        for line in file:
            words = line.split('|')
            try:
                code = zone_code[words[2]+'-'+words[3]]
                inputdata = [code, words[5], words[6]]
                put_data_into_oss(inputdata)
            except Exception as e:
                pass

def put_data_into_oss(inf):
    postdata = "metricId="+inf[0]+"&date="+inf[1]+"&dateFormat=yyyy-MM-dd HH:mm&value=79"
    posturl = 'https://oss.tech.cn.com/api/data/v1/save'
    try:
        response = urllib2.urlopen(posturl, postdata)
        print response.geturl()
    except Exception as e:
        raise e
    
if __name__ == '__main__':
    print 'start'
    read_file()
