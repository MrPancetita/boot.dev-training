# https://www.boot.dev/lessons/1d9bbaf7-f597-497d-aebd-4662097ef2f7

def filter_messages(messages):
    filtered_messages = []
    profanity_counts = []
    profane_word = "dang"
    for message in messages:
        filtered_message = []
        profanity_count = 0
        words = message.split()
        for word in words:
            if word != profane_word:
                filtered_message.append(word)
            else:
                profanity_count += 1
        filtered_messages.append(" ".join(filtered_message))
        profanity_counts.append(profanity_count)
    return filtered_messages, profanity_counts