import requests
import re, time, random, json

class GraphqlReact:
    def __init__(self, cookies, ua='Mozilla/5.0 (Windows NT 10.0; rv:52.0) Gecko/20100101 AOLShield/52.4.2'):
        self.ses = requests.session()
        self.ses.cookies['cookie'] = cookies
        self.get_headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','dpr':'1.8000000715255737','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':ua,'viewport-width':'980'}
        self.post_headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','dpr':'1.8000000715255737','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':ua,'viewport-width':'980','X-ASBD-ID':'129477'}

    def react(self, post_id):
        src = self.ses.get('https://www.facebook.com/'+ post_id, headers=self.get_headers).text
        #        open('/sdcard/x.htm','w').write(src)
        lsd = re.search(r'\["LSD",\[\],\{"token":"(.*?)"', src).group(1)
        user = re.search(r'"actorID":"(.*?)"', src).group(1)

        var = {
            "input":{
                "attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1697303736286,689359,,",
                "feedback_id":re.findall(r'"feedback_id":"(.*?)"', src)[-1],
                "feedback_reaction_id":'444813342392137',
                "feedback_source":"OBJECT",
                "is_tracking_encrypted":True,
                "tracking":[re.search(r'"encrypted_tracking":"(.*?)"', src).group(1)],
                "session_id":re.search(r'"sessionID":"(.*?)"', src).group(1),
                "actor_id":user,
                "client_mutation_id":"1"
            },
           "useDefaultActor":False,
           "scale":1.5
        }
        
        spin_r = re.search(r'__user=(.*?)&', src).group(1)
        data = {
            'av':user,
            '__user':user,
            '__a':'1',
            '__hs':re.search(r'"haste_session":"(.*?)"', src).group(1),
            'dpr':'1',
            '__ccg':re.search(r'"connectionClass":"(.*?)"', src).group(1),
            '__rev':spin_r,
            '__hsi':re.search(r'"hsi":"(.*?)"', src).group(1),
            '__comet_req':re.search(r'__comet_req=(.*?)&', src).group(1),
            'fb_dtsg':re.search(r'\["DTSGInitialData",\[\],\{"token":"(.*?)"', src).group(1),
            'jazoest':re.search(r'jazoest=(.*?)"', src).group(1),
            'lsd':lsd,
            '__spin_r':spin_r,
            '__spin_b':re.search(r'"__spin_b":"(.*?)"', src).group(1),
            '__spin_t':re.search(r'"__spin_t":(.*?),', src).group(1),
            'fb_api_caller_class':'RelayModern',
            'fb_api_req_friendly_name':'CometUFIFeedbackReactMutation',
            'variables':json.dumps(var),
            'server_timestamps':True,
            'doc_id':'6623712531077310'
        }

        coldown = random.randrange(360, 720)
        post = self.ses.post('https://www.facebook.com/api/graphql/', data=data, headers=self.post_headers).text
        if re.search('"can_viewer_react":(.*?),', post).group(1) == 'true':
            print('Berhasil memberikan reaksi! Post_id: {}, Coldown: {}'.format(post_id, coldown))
        else:
            print('Gagal memberikan reaksi! Post_id: {}, Coldown: {}'.format(post_id, coldown))

        time.sleep(coldown)

    def loop_id(self):
        src = self.ses.get('https://mbasic.facebook.com/', headers=self.get_headers).text
        regex = re.findall(r'shared_from_post_id=(.*?)&', src)
        for post_id in list(set(regex)):
            self.react(post_id)
 
# masukan cookies di variable c
c = 'sb=ZmRgZYGeqJKZAiJeXUubG2cG; datr=ZmRgZXSeoERdhH79_XSHLIDe; dpr=1.8000000715255737; c_user=61553284916731; xs=46%3ATCNCs81E2Og9tQ%3A2%3A1701182002%3A-1%3A-1; m_page_voice=61553284916731; wd=400x714; fr=1FBvR1iDs2D44xhi8.AWXL0xDjrIPV4nciLAXweCx6MT0.BlYSup.cQ.AAA.0.0.BlaBRc.AWXpnR18wac'
GraphqlReact(c).loop_id()
