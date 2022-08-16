def generate_hashtag(s):
    tag = ''.join([word.capitalize() for word in s.split(' ')])
    return '#' + tag if tag and len(tag) < 140 else False