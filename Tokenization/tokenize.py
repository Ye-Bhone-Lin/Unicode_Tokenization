import re

def syllable_tokenize(text: str) -> str:
    """
    Tokenizes Unicode Burmese text into syllables.
    
    Args:
        text (str): The input Burmese text.
        
    Returns:
        str: The tokenized text with spaces between syllables.
    """
    pattern = re.compile(r'([က-ဪ]|[^က-၏])(?![ှျ]?[့္်])')
    return pattern.sub(r' \1', text)

text = 'တွေ့ရတာဝမ်းသာပါတယ်'
tokenized_text = syllable_tokenize(text)
print(tokenized_text)
