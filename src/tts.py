from pathlib import Path

from google.cloud import texttospeech


def generate_audio(text: str, output_file: str) -> None:
    """Generate audio file from text using Google Cloud Text-to-Speech API."""
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="ja-JP",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
    )
    response = client.synthesize_speech(
        input=input_text,
        voice=voice,
        audio_config=audio_config,
    )

    with Path.open(output_file, "wb") as out:
        out.write(response.audio_content)
