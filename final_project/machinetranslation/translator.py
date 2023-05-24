import os
from ibm_watson import LanguageTranslatorV3 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

lt.set_service_url(url)

def engtofr(engt):
    frt = lt.translate(text= engt, model_id='en-fr').get_result()
    translation=frt['translations'][0]['translation']
    print(translation)
    return translation

def frtoeng(frt):
    engt = lt.translate(text= frt, model_id='fr-en').get_result()
    translation=engt['translations'][0]['translation']
    print(translation)
    return translation