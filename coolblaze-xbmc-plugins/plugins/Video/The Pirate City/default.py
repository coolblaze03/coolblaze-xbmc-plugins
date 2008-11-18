import urllib,urllib2,re,xbmcplugin,xbmcgui,socket,xbmc,base64
			

def CATS():
        addDir('1) Featured Movies','http://www.thepiratecity.org/',5,'')
        addDir('2) All Movies','http://www.thepiratecity.org/search.htm',1,'')
        addDir('3) Action','http://www.thepiratecity.org/search.htm?cat=29&type=',1,'')
        addDir('4) Drama ','http://www.thepiratecity.org/search.htm?cat=33&type=',1,'')
        addDir('5) Family','http://www.thepiratecity.org/search.htm?cat=31&type=',1,'')
        addDir('6) Horror','http://www.thepiratecity.org/search.htm?cat=34&type=',1,'')
        addDir('7) Comedy','http://www.thepiratecity.org/search.htm?cat=32&type=',1,'')
        addDir('8) Sci-fi','http://www.thepiratecity.org/search.htm?cat=36&type=',1,'')
        addDir('9) Others','http://www.thepiratecity.org/search.htm?cat=37&type=',1,'')
		

def INDEX(data):
                #req = urllib2.Request(data)
                #req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
                #lemon = urllib2.urlopen(req);response=lemon.read();lemon.close()
                #url=re.compile('<a class="anc"  href="(.+?)\"').findall(response)
                #name=re.compile('_(.+?).htm').findall(str(url))
                #for n in range(0,len(url)):
                #        addDir(name[n],'http://www.thepiratecity.org/'+url[n],2,'')
        req = urllib2.Request(data)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
        lemon = urllib2.urlopen(req);response=lemon.read();lemon.close()
        url=re.compile('<a class="anc"  href="(.+?)\"').findall(response)
        nameclean=re.compile('_(.+?).htm').findall(str(url))
        #Tidy names
        code=re.sub('_',' ',str(nameclean))
        code2=re.sub('  ',' - ',code)
        code3=re.sub('&#039;','',code2)
        code4=re.sub('&amp;','&',code3)
        code5=re.sub('&eacute;','e',code4)
        name=re.compile("'(.+?)'").findall(code5)
        #small ammendment - Voinage.
        for n in range(0,len(url)):
                addDir(name[n],'http://www.thepiratecity.org/'+url[n],2,"")

def INDEXF(data):
                req = urllib2.Request(data)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
                lemon = urllib2.urlopen(req);response=lemon.read();lemon.close()
                url=re.compile('<a class="loginText"  onMouseover.+?href="(.+?)\">').findall(response)
                name=re.compile('_(.+?).htm').findall(str(url))
                for n in range(0,len(url)):
                        addDir(name[n],'http://www.thepiratecity.org/'+url[n],2,'')
						
def ExtractMediaUrl(data):
        if len(data) > 0:
        			videoPath = ""
        			storeMessage = ""
        			alphabet = "abcdefghijklmnopqrstuvwxyz"
        			randomAlpha = ""
        			randomNumber = 0
        			storeMessage = data
        			switchOverDecoded = ""
        			keyPosition = 0
        			i = 0
        			j = 0
        			
        			while i < 26:
        				if data[0] == alphabet[i]:
        					keyPosition = i
        				i = i + 1
        				
        			i = 0
        			
        			while i < 26: 
        				randomAlpha = randomAlpha + alphabet[keyPosition]
        				keyPosition = keyPosition + 1
        				if keyPosition == 26: 
        					keyPosition = 0
        				i = i + 1
        			
        			i = 0
        			
        			while i < len(storeMessage):
        				if (storeMessage[i] > "`" and storeMessage[i] < "{"): 
        					j = 0
        					while j < 26:
        						if (storeMessage[i] == randomAlpha[j]):
        							switchOverDecoded = switchOverDecoded + alphabet[j]
        						j = j + 1
        				else: 
        					switchOverDecoded = switchOverDecoded + storeMessage[i]
        				i = i + 1
        				
        			storeMessage = switchOverDecoded[1:]
        			randomAlpha = ""
        			switchOverDecoded = ""
        			videoPath = storeMessage
        			
        			return videoPath
        			
        else:
            return ""
			
						

def VIDEO(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
        lemon = urllib2.urlopen(req);response=lemon.read();lemon.close()
        vpageurl=re.compile('<iframe scrolling="no" frameborder="0" src="(.+?)\"').findall(response)
        req = urllib2.Request('http://www.thepiratecity.org/'+vpageurl[0])
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
        lemon = urllib2.urlopen(req);response=lemon.read();lemon.close()
        match=re.compile('\r\nflashvars="myURL=(.+?)"').findall(response)
        link=ExtractMediaUrl(match[0])
        addLink(name+' - Flv',link,'')


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
              
params=get_params()
url=None
name=None
mode=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
#print "Mode: "+ str(mode)
#print "URL: "+str(url)
#print "Name: "+str(name)
if mode==None or url==None or len(url)<1:
        #print "CATEGORY INDEX : "
        CATS()
elif mode==1:
        INDEX(url)
elif mode==2:
        VIDEO(url,name)
elif mode==5:
        INDEXF(url)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
