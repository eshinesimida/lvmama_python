# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from datetime import datetime
import re
import time
import uuid
import random
from mysql import xiechengDAO

class XiechengDriverService(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        
        self.xiechengDao = xiechengDAO()
        # 存放列表页数据
        self.listPageInfo = []
        
        self.commList = []
        #self.urls=['http://you.ctrip.com/sight/beijing1/234.html','http://you.ctrip.com/sight/beijing1/229.html','http://you.ctrip.com/sight/beijing1/231.html','http://you.ctrip.com/sight/yanqing770/230.html','http://you.ctrip.com/sight/beijing1/5174.html','http://you.ctrip.com/sight/beijing1/233.html','http://you.ctrip.com/sight/huairou120418/243.html']
        self.urls=[

'http://ticket.lvmama.com/scenic-104772#yhdp','http://ticket.lvmama.com/scenic-158731#yhdp','http://ticket.lvmama.com/scenic-158721#yhdp','http://ticket.lvmama.com/scenic-103209#yhdp','http://ticket.lvmama.com/scenic-103294#yhdp','http://ticket.lvmama.com/scenic-187#yhdp','http://ticket.lvmama.com/scenic-108097#yhdp','http://ticket.lvmama.com/scenic-153319#yhdp',
'http://ticket.lvmama.com/scenic-107676#yhdp','http://ticket.lvmama.com/scenic-104474#yhdp','http://ticket.lvmama.com/scenic-171376#yhdp','http://ticket.lvmama.com/scenic-159603#yhdp','http://ticket.lvmama.com/scenic-10626118#yhdp','http://ticket.lvmama.com/scenic-100957#yhdp','http://ticket.lvmama.com/scenic-160805#yhdp','http://ticket.lvmama.com/scenic-3667#yhdp','http://ticket.lvmama.com/scenic-158280#yhdp','http://ticket.lvmama.com/scenic-100868#yhdp',
'http://ticket.lvmama.com/scenic-101821#yhdp','http://ticket.lvmama.com/scenic-100390#yhdp','http://ticket.lvmama.com/scenic-102215#yhdp','http://ticket.lvmama.com/scenic-100572#yhdp','http://ticket.lvmama.com/scenic-100640#yhdp','http://ticket.lvmama.com/scenic-100474#yhdp','http://ticket.lvmama.com/scenic-100491#yhdp','http://ticket.lvmama.com/scenic-156091#yhdp','http://ticket.lvmama.com/scenic-102139#yhdp','http://ticket.lvmama.com/scenic-103036#yhdp','http://ticket.lvmama.com/scenic-100455#yhdp',
'http://ticket.lvmama.com/scenic-109669#yhdp','http://ticket.lvmama.com/scenic-109777#yhdp','http://ticket.lvmama.com/scenic-103075#yhdp','http://ticket.lvmama.com/scenic-158694#yhdp','http://ticket.lvmama.com/scenic-100945#yhdp','http://ticket.lvmama.com/scenic-100718#yhdp','http://ticket.lvmama.com/scenic-100956#yhdp','http://ticket.lvmama.com/scenic-108084#yhdp','http://ticket.lvmama.com/scenic-100946#yhdp','http://ticket.lvmama.com/scenic-122400#yhdp','http://ticket.lvmama.com/scenic-120604#yhdp',
'http://ticket.lvmama.com/scenic-100882#yhdp','http://ticket.lvmama.com/scenic-160631#yhdp','http://ticket.lvmama.com/scenic-101478#yhdp','http://ticket.lvmama.com/scenic-100886#yhdp','http://ticket.lvmama.com/scenic-100882#yhdp',
'http://ticket.lvmama.com/scenic-101548#yhdp','http://ticket.lvmama.com/scenic-107516#yhdp','http://ticket.lvmama.com/scenic-171634#yhdp','http://ticket.lvmama.com/scenic-105717#yhdp','http://ticket.lvmama.com/scenic-102965#yhdp','http://ticket.lvmama.com/scenic-100530#yhdp',
'http://ticket.lvmama.com/scenic-160038#yhdp','http://ticket.lvmama.com/scenic-103033#yhdp','http://ticket.lvmama.com/scenic-154369#yhdp','http://ticket.lvmama.com/scenic-101006#yhdp','http://ticket.lvmama.com/scenic-104588#yhdp','http://ticket.lvmama.com/scenic-107987#yhdp','http://ticket.lvmama.com/scenic-101043#yhdp','http://ticket.lvmama.com/scenic-101293#yhdp','http://ticket.lvmama.com/scenic-101028#yhdp','http://ticket.lvmama.com/scenic-10000391#yhdp',
'http://ticket.lvmama.com/scenic-3942#yhdp','http://ticket.lvmama.com/scenic-101000#yhdp','http://ticket.lvmama.com/scenic-104599#yhdp','http://ticket.lvmama.com/scenic-159590#yhdp','http://ticket.lvmama.com/scenic-152650#yhdp','http://ticket.lvmama.com/scenic-160588#yhdp','http://ticket.lvmama.com/scenic-102589#yhdp','http://ticket.lvmama.com/scenic-100969#yhdp','http://ticket.lvmama.com/scenic-456#yhdp','http://ticket.lvmama.com/scenic-101112#yhdp','http://ticket.lvmama.com/scenic-154499#yhdp',
'http://ticket.lvmama.com/scenic-101374#yhdp','http://ticket.lvmama.com/scenic-156466#yhdp','http://ticket.lvmama.com/scenic-101720#yhdp','http://ticket.lvmama.com/scenic-100335#yhdp','http://ticket.lvmama.com/scenic-101159#yhdp',
'http://ticket.lvmama.com/scenic-162215#yhdp','http://ticket.lvmama.com/scenic-101141#yhdp','http://ticket.lvmama.com/scenic-108156#yhdp','http://ticket.lvmama.com/scenic-104777#yhdp','http://ticket.lvmama.com/scenic-102975#yhdp','http://ticket.lvmama.com/scenic-100974#yhdp','http://ticket.lvmama.com/scenic-103027#yhdp','http://ticket.lvmama.com/scenic-101204#yhdp',
'http://ticket.lvmama.com/scenic-101127#yhdp','http://ticket.lvmama.com/scenic-107134#yhdp','http://ticket.lvmama.com/scenic-108497#yhdp',
'http://ticket.lvmama.com/scenic-103189#yhdp','http://ticket.lvmama.com/scenic-160352#yhdp','http://ticket.lvmama.com/scenic-103156#yhdp','http://ticket.lvmama.com/scenic-100753#yhdp','http://ticket.lvmama.com/scenic-344#yhdp','http://ticket.lvmama.com/scenic-100713#yhdp','http://ticket.lvmama.com/scenic-100807#yhdp','http://ticket.lvmama.com/scenic-100754#yhdp,'
'http://ticket.lvmama.com/scenic-108009#yhdp','http://ticket.lvmama.com/scenic-100428#yhdp','http://ticket.lvmama.com/scenic-100561#yhdp','http://ticket.lvmama.com/scenic-173041#yhdp',
'http://ticket.lvmama.com/scenic-11318003#yhdp','http://ticket.lvmama.com/scenic-101867#yhdp','http://ticket.lvmama.com/scenic-3953#yhdp',
'http://ticket.lvmama.com/scenic-101840#yhdp','http://ticket.lvmama.com/scenic-100460#yhdp','http://ticket.lvmama.com/scenic-108362#yhdp','http://ticket.lvmama.com/scenic-100433#yhdp',
'http://ticket.lvmama.com/scenic-109505#yhdp','http://ticket.lvmama.com/scenic-105324#yhdp','http://ticket.lvmama.com/scenic-10689749#yhdp','http://ticket.lvmama.com/scenic-161600#yhdp','http://ticket.lvmama.com/scenic-105313#yhdp','http://ticket.lvmama.com/scenic-160599#yhdp','http://ticket.lvmama.com/scenic-107761#yhdp','http://ticket.lvmama.com/scenic-100306#yhdp','http://ticket.lvmama.com/scenic-101163#yhdp'






]
        
    def start(self):
        for url1 in self.urls:
            self.driver.get(url1)
            # 将界面最大化
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)
            time.sleep(3)
            self.crawlxiecheng()




    def crawlxiecheng(self):
        # 单页循环次数
        loopNum = 0

        ifHandle = False

        #获取总页面数
        pageNum = 2800
        while(pageNum>=1):
            # 循环次数加1
            loopNum = loopNum + 1
            
            target = self.driver.find_element_by_css_selector(
                '#allCmtComment > div.paging.orangestyle')
            y = target.location['y']
            print y
            y = y - 100
            # self.driver.execute_script("arguments[0].scrollIntoView();", target)
            js = "var q=document.documentElement.scrollTop=" + str(y)
            self.driver.execute_script(js)

            time.sleep(3)



            if u"驴友点评" in self.driver.page_source:

                if ifHandle == False:
                    a = self.crawllianjie(self.driver.page_source)
                    #print a
                    if(a ==2):
                        break
                        #continue
                    ifHandle = True

                try:
                    #print (u"下一页" in self.driver.page_source)
                    if u"有用" in self.driver.page_source:
                        #print(u"下一页" in self.driver.page_source)
                        pageNum = pageNum - 1
                       
                        self.driver.find_element_by_xpath("//*[@id='allCmtComment']/div[11]/div/a[@class='nextpage']").click()
                        #mment_ctrip']/div[@class='ttd_pager cf']/div[@class='pager_v1']/a[@class='nextpage']").click()
                        ifHandle = False
                        #print ifHandle
                        loopNum = 0

                        time.sleep(3)
                        print "页数：" + str(pageNum)
                    else:
                        break


                except:

                    pageNum = pageNum + 1




        return False if pageNum > 1 else True

    def crawllianjie(self, page_sourse):
        #print page_sourse
        response = HtmlResponse(url="my HTML string", body=page_sourse, encoding="utf-8")
        #/html/body/div[4]/div/div[2]/div[1]/div/h1
        jingqu = response.xpath('//div[@class="crumbs-link"]/span[@class="crumbs-list"]/a/text()').extract()[0]
        province = response.xpath('//div[@class="crumbs-link"]/a[@class="current"]/text()').extract()[0]
        A = response.xpath("//div[@class='comment-list com-all']/div[@class='comment-li']")
        
        for B in A:
            comment = B.xpath('div[@class="ufeed-content"]/text()').extract()
            comments = []
            for i in comment:
                i = i.strip()
                comments.append(i)
            comment1 = ''.join(comments)

            author = B.xpath('div[@class="com-userinfo"]/p/a[1]/text()').extract()[0]
            time = B.xpath('div[@class="com-userinfo"]/p/em/text()').extract()[0]
            ID = B.xpath('div[@class="com-userinfo"]/a/@id').extract()[0]
            ID = ID.split("_")[2]
            #print ID,user,comment1,time

            if(time < '2016-01-01'):
                return(2)
                continue

            self.listPageInfo.append({"jingqu":jingqu,"province":province, "author": author, "ID": ID,"time":time,
                                      "comment":comment1})
        xiechengService.saveListPageInfo()

        print len(self.listPageInfo)
        self.listPageInfo = []





    def saveListPageInfo(self):
        self.xiechengDao.savehotellink(self.listPageInfo)

    def depose(self):
        self.driver.close()

if __name__=="__main__":
    xiechengService = XiechengDriverService()
    xiechengService.start()

    xiechengService.depose()

