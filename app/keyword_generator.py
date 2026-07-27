def generate_keywords(scene):
    words = scene.lower().split()

    # Common words remove karo
    stop_words = {
        "the", "is", "a", "an", "and", "of", "to",
        "in", "on", "for", "with", "are", "this"
    }

    keywords = []

    for word in words:
        word = word.strip(".,!?")

        if word not in stop_words:
            keywords.append(word)

    return " ".join(keywords[:4])