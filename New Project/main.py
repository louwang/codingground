# Hello World program in Python

import urllib2
#364
for i in range(1,364):
    strurl='http://www.plchardware.com/Products/Default.aspx?man=Siemens&cnd=1&t=OTA3Mw==&cp='+str(i)
    #print strurl
    response = urllib2.urlopen(strurl)
    html = response.read()
    print html
