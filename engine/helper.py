import re


def extract_yt_term(vid):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, vid, re.IGNORECASE)
    return match.group(1) if match else None