def convert_to_dashed_string(text: str) -> str:
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    
    # Step 1: Remove unwanted characters
    cleaned_text = ""
    for ch in text:
        if ch in allowed_chars:
            cleaned_text += ch

    # Step 2: Split by spaces and join with dash
    dashed_text = "-".join(cleaned_text.split())

    # Step 3: Convert to lowercase
    return dashed_text.lower()

print(convert_to_dashed_string("Hello, World!"))
print(convert_to_dashed_string("Multiple    Spaces"))
print(convert_to_dashed_string("Python-Programming@2024"))
print(convert_to_dashed_string("47: 113-04-789"))
print(convert_to_dashed_string("Special*&^%Characters"))