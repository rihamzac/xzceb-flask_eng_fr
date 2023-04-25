# translate text from english to french

import ibm_watson
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def english_to_french(english_text):
     # Use the Language Translator instance to translate the input English text to French
    authenticator = IAMAuthenticator('jusvyVKgVQ7TY2ROb3uMz63MYu9naVeLHW-pDV_RHH1X')
    translator = ibm_watson.LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
    translator.set_service_url(
'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/afe709de-df9d-4f26-ad2c-9765d0b8e1ca'
)
    translation = translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
     # Use the Language Translator instance to translate the input French text to English
    authenticator = IAMAuthenticator('jusvyVKgVQ7TY2ROb3uMz63MYu9naVeLHW-pDV_RHH1X')
    translator = ibm_watson.LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
    translator.set_service_url(
    'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/afe709de-df9d-4f26-ad2c-9765d0b8e1ca'
    )
    translation = translator.translate(
        text= 'bonjour',
        source='fr',
        target='en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
