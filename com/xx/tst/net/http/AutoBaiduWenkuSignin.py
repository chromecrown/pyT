#coding:utf-8
#author:wolf@future-sec
import urllib2
import re
def run(host,port,cookie,timeout=10):
    url = "http://%s:%d"%(host,int(port))
    login_url = url+'/task/submit/signin'
    cookies=''
    try:
        cookies = cookie
    except:
        pass
    data = []
    data.append('Accept: */*')
    data.append('Accept-Encoding: gzip, deflate, sdch')
    data.append('Accept-Language: zh-CN,zh;q=0.8,en;q=0.6')
    http_body = '\r\n'.join(data)
    try:
        req = urllib2.Request(login_url, data=http_body)
        req.add_header("X-Requested-With","XMLHttpRequest")
        req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
        req.add_header('Referer','http://wenku.baidu.com/task/browse/daily')
        req.add_header('Cookie',cookies)
        res_html = urllib2.urlopen(req, timeout=timeout).read()
        return res_html
    except Exception,e:
        print e

if __name__ == "__main__":
    host = "wenku.baidu.com"
    port = "80"
    cookie105 = """PSTM=1463737363; BIDUPSID=798F099CA5E9F3C44790DD39D8CC1CB0; BAIDUID=B65D0A575941E26FA4C26E794F560629:SL=0:NR=20:FG=1; wkview_gotodaily_tip=1; bdshare_firstime=1464591795235; viewedPg=97e687f0c77da26925c5b074%3D1%7C0; grownupTaskFinish=815346909%7C1; MCITY=-131%3A; H_PS_PSSID=1466_18241_19570_18560_15149_11879_20014; wk_shifen_pop_window=2888_2_1464591848926%7C2847_2_1464592310692%7C2355_2_1464744878387%7C2824_2_1464744909317%7C2875_2_1464745731212; BDUSS=X5QaDhzOEJ3NExxWHFmTVhrZHQtTi1LNEVoOEl6R21td1BzcUxIWWJOUVp6SFZYQVFBQUFBJCQAAAAAAAAAAAEAAACTvrk-Y2hyb21lY3IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABk~TlcZP05XS; Hm_lvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1464591794,1464744499; Hm_lpvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1464745781"""
    cookie815 = """PSTM=1463737363; BIDUPSID=798F099CA5E9F3C44790DD39D8CC1CB0; BAIDUID=B65D0A575941E26FA4C26E794F560629:SL=0:NR=20:FG=1; wkview_gotodaily_tip=1; bdshare_firstime=1464591795235; viewedPg=97e687f0c77da26925c5b074%3D1%7C0; grownupTaskFinish=815346909%7C1; MCITY=-131%3A; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDUSS=kFBLWhkMkxTa2dZRHk4bEl2NTYwRnYwenNaRkpDY3Z5anhvM0xxQm5DZXRJM2RYQVFBQUFBJCQAAAAAAAAAAAEAAACsJSwKODE1MzQ2OTA5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK2WT1etlk9XY; H_PS_PSSID=1466_18241_19570_18560_15149_11879_20014; Hm_lvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1464830159,1464833718,1464833738,1464833813; Hm_lpvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1464833813; wk_shifen_pop_window=2888_2_1464591848926%7C2847_2_1464592310692%7C2824_2_1464744909317%7C2355_2_1464830200621%7C2875_2_1464833828446"""
    run(host,port,cookie105)
    print "sign in 105 done"
    run(host,port,cookie815)
    print "sign in 815 done"