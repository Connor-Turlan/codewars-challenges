def first_non_repeating_letter(string):
    chars = [c for c in string if string.lower().count(c.lower()) <= 1]
    return chars[0] if chars and string else ""