def validate_text(text):
    if not isinstance(text, str):
        raise TypeError("Text property should be of text type.")
    if not text.strip():
        raise ValueError("Text property should not be empty.")
