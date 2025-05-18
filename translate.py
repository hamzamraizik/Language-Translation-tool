import os
from google.cloud import translate_v2 as translate

# List of valid ISO 639-1 codes (partial, for demonstration)
VALID_LANG_CODES = {
    'en', 'es', 'fr', 'de', 'zh', 'ar', 'ru', 'ja', 'ko', 'it', 'pt', 'hi', 'tr', 'nl', 'sv', 'pl', 'fi', 'no', 'da', 'cs', 'el', 'he', 'id', 'ms', 'th', 'vi', 'uk', 'ro', 'hu', 'sk', 'bg', 'hr', 'lt', 'lv', 'et', 'sl', 'sr', 'ca', 'eu', 'gl', 'mt', 'ga', 'is', 'mk', 'sq', 'sw', 'ta', 'te', 'ml', 'bn', 'gu', 'mr', 'pa', 'ur', 'fa', 'af', 'zu', 'xh', 'st', 'tn', 'ts', 'ss', 've', 'nr', 'ny', 'so', 'am', 'om', 'ti', 'rw', 'kg', 'ln', 'lu', 'kj', 'ha', 'yo', 'ig', 'ee', 'tw', 'ff', 'wo', 'ak', 'kr', 'ks', 'ps', 'sd', 'si', 'my', 'km', 'lo', 'mn', 'bo', 'dz', 'ne', 'as', 'or', 'sa', 'bh', 'mai', 'kok', 'doi', 'mni', 'bho', 'sat', 'kha', 'br', 'co', 'cy', 'gd', 'kw', 'la', 'lb', 'li', 'oc', 'rm', 'sc', 'vo', 'wa', 'yi', 'za'
}

def is_valid_lang_code(code):
    return code in VALID_LANG_CODES

def translate_text(text, source_lang, target_lang):
    translate_client = translate.Client()
    result = translate_client.translate(
        text,
        source_language=source_lang,
        target_language=target_lang
    )
    return result['translatedText']

def main():
    print("--- Language Translation Tool (Google Cloud) ---")
    text = input("Enter text to translate: ").strip()
    if not text:
        print("Error: Text cannot be empty.")
        return
    source_lang = input("Enter source language code (e.g., 'en' for English): ").strip().lower()
    if not source_lang or not is_valid_lang_code(source_lang):
        print("Error: Invalid or empty source language code. See ISO 639-1 codes.")
        return
    target_lang = input("Enter target language code (e.g., 'es' for Spanish): ").strip().lower()
    if not target_lang or not is_valid_lang_code(target_lang):
        print("Error: Invalid or empty target language code. See ISO 639-1 codes.")
        return
    try:
        translated = translate_text(text, source_lang, target_lang)
        print(f"\nTranslated text: {translated}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 