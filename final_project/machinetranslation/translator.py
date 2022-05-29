"""Translation module"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
#pylint: disable=unsubscriptable-object
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION,authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Calls the instance and translates from english to french
    """
    if english_text is not None:
        translation_response = language_translator.translate(\
                                text=english_text, model_id='en-fr')
        translation = translation_response.get_result()
        return translation['translations'][0]['translation']
    return None

def french_to_english(french_text):
    """
    Calls the instance and translates from french to english
    """
    if french_text is not None:
        translation_response = language_translator.translate(\
                                text=french_text, model_id='fr-en')
        translation = translation_response.get_result()
        return translation['translations'][0]['translation']
    return None
