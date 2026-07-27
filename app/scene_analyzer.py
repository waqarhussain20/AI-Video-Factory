def analyze_script(script):
    scenes = []

    for sentence in script.split("."):
        sentence = sentence.strip()

        if sentence:
            scenes.append(sentence)

    return scenes