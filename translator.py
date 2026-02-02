import requests
from config import TRANSLATOR_KEY, TRANSLATOR_ENDPOINT, TRANSLATOR_REGION

def translate_text(text, target_lang):
    if not text:
        return ""
    
    path = "/translate?api-version=3.0"
    params = f"&to={target_lang}"
    headers = {
        "Ocp-Apim-Subscription-Key": TRANSLATOR_KEY,
        "Ocp-Apim-Subscription-Region": TRANSLATOR_REGION,
        "Content-Type": "application/json"
    }
    body = [{"text": text}]
    
    try:
        response = requests.post(
            TRANSLATOR_ENDPOINT + path + params,
            headers=headers,
            json=body
        )
        response.raise_for_status()
        result = response.json()
        
        if result and len(result) > 0 and "translations" in result[0]:
            return result[0]["translations"][0]["text"]
        else:
            print(f"Translation API error: {result}")
            return text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text
