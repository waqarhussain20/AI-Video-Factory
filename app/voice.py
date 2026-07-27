import subprocess
import os

PIPER_EXE = r"C:\piper\piper.exe"
MODEL = r"C:\piper\models\en_US-amy-medium.onnx"


def generate_voice(text, output_file="temp/voice.wav"):
    os.makedirs("temp", exist_ok=True)

    command = [
        PIPER_EXE,
        "--model",
        MODEL,
        "--output_file",
        output_file,
    ]

    subprocess.run(
        command,
        input=text,
        text=True,
        check=True
    )

    print(f"Voice Saved: {output_file}")

    return output_file