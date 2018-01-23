# -*- coding: utf-8 -*-
import urllib.request

'''
speaker
mijin : 한국어, 여성 음색
jinho : 한국어, 남성 음색
clara : 영어, 여성 음색
matt : 영어, 남성 음색
yuri : 일본어, 여성 음색
shinji : 일본어, 남성 음색
meimei : 중국어, 여성 음색
liangliang : 중국어, 남성 음색
jose : 스페인어, 남성 음색
carmen : 스페인어, 여성 음색

speed
-5 ~ 5 = (1.5 ~ 0.5)
'''

client_id = "api_id"
client_secret = "api_secret"

class Naver_TTS:
    def get_file(message):
        param = "speaker=mijin&speed=0&text=" + str(message);

        request = urllib.request.Request("https://openapi.naver.com/v1/voice/tts.bin")
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=param.encode('utf-8'))
        code = response.getcode()

        if(code == 200):
            response_body = response.read()
            with open("tts.mp3", 'wb') as f:
                f.write(response_body)
        else:
            print("Connection Refused - Code " + code)
