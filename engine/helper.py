import re

from engine.config import ASSISTANT_NAME


def extract_yt_term(vid):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, vid, re.IGNORECASE)
    return match.group(1) if match else None


def remove_words(input_string, words_to_remove):
    # split input string into separate words
    words =input_string.split()

    # remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    result_string = ' '.join(filtered_words)
    return result_string

# # sample usage
# input_string = "make a phone call to appaji"
# words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'call', 'message', 'whatsapp', 'send', 'phone', 'to']
# result = remove_words(input_string, words_to_remove)
# print(result)
