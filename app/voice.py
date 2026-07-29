import subprocess
import os

PIPER_EXE = r"C:\piper\piper.exe"

MODELS = {
    "🇺🇸 English": {
        "Male": r"C:\piper\models\en_US-ryan-medium.onnx",
        "Female": r"C:\piper\models\en_US-amy-medium.onnx",
    },

    "🇵🇰 Urdu": {
        "Male": r"C:\piper\models\ur_PK-fasih-medium.onnx",
        "Female": r"C:\piper\models\ur_PK-fasih-medium.onnx",
    },

    "🇪🇸 Spanish": {
        "Male": r"C:\piper\models\es_ES-sharvard-medium.onnx",
        "Female": r"C:\piper\models\es_ES-sharvard-medium.onnx",
    }
}


def generate_voice(
    text,
    language="🇺🇸 English",
    voice="Male",
    output_file="temp/voice.wav"
):

    os.makedirs("temp", exist_ok=True)

    model = MODELS.get(
        language,
        MODELS["🇺🇸 English"]
    ).get(
        voice,
        MODELS["🇺🇸 English"]["Male"]
    )

    print("\n==============================")
    print("Language :", language)
    print("Voice    :", voice)
    print("Model    :", model)
    print("==============================")

    command = [
        PIPER_EXE,
        "--model",
        model,
        "--output_file",
        output_file
    ]

    subprocess.run(
        command,
        input=text.encode("utf-8"),
        check=True
    )

    print(f"\nVoice Saved: {output_file}")

    return output_file