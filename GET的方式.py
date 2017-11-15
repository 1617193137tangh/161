值= {}
值[ ' username ' ] =  “ 805043442@qq.com ”
值[ '密码' ] =  “ wy980913 .. ”
data = urllib.urlencode（values）
url =  “ http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn ”
request = urllib2.Request（url，data）
response = urllib2.urlopen（request）
打印 response.read（）
