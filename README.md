# Language Translation Tool

A simple command-line tool to translate text from one language to another using the Google Cloud Translation API.

## Features
- Translate text between languages
- Uses Google Cloud Translation API (pre-trained model)

## Prerequisites
- Python 3.x
- Google Cloud account with Translation API enabled
- **Service account JSON key for authentication (do NOT include this file in your repository!)**

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a Google Cloud service account and download the JSON key:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the **Cloud Translation API** for your project.
   - Navigate to **IAM & Admin > Service Accounts**.
   - Create a new service account (or use an existing one).
   - Grant it the **Cloud Translation API User** role.
   - Click **Create Key** and download the JSON key file.
   - **Do NOT include this JSON key file in your repository.**
4. Set the environment variable for authentication:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
   ```
   Replace `/path/to/your/service-account-file.json` with the actual path to your downloaded JSON key file.

## Usage
Run the tool:
```bash
python translate.py
```
- Enter the text to translate
- Enter the source language code (e.g., `en` for English)
- Enter the target language code (e.g., `es` for Spanish)

## Language Codes
Refer to [ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for language codes.

## License
Specify your license here. 