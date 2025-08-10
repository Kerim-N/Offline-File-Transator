import argostranslate.package, argostranslate.translate  # Argos Translate library for offline translations
import pdfplumber  # Library for extracting text from PDF files
import docx2txt    # Library for extracting text from DOCX (Word) files
import os          # OS module (used for file path handling, though here it's not strictly necessary)

def load_model(from_code="ru", to_code="en"):
    """
    Loads the translation model for the specified language pair.

    Args:
        from_code (str): Source language code (e.g., 'ru' for Russian).
        to_code (str): Target language code (e.g., 'en' for English).

    Returns:
        translation object or None: Translation model object if found, otherwise None.
    """
    installed_languages = argostranslate.translate.get_installed_languages()  # Get all installed translation languages
    from_lang = next(filter(lambda l: l.code == from_code, installed_languages), None)  # Find source language
    to_lang = next(filter(lambda l: l.code == to_code, installed_languages), None)      # Find target language
    return from_lang.get_translation(to_lang) if from_lang and to_lang else None        # Return translation model if both exist

def extract_text(file_path):
    """
    Extracts text from a file (.pdf, .docx, or .txt).

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Extracted text from the file.

    Raises:
        ValueError: If the file format is unsupported.
    """
    if file_path.endswith(".pdf"):  # PDF extraction
        with pdfplumber.open(file_path) as pdf:
            # Extract text from each page and join with line breaks
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    elif file_path.endswith(".docx"):  # DOCX extraction
        return docx2txt.process(file_path)
    elif file_path.endswith(".txt"):   # TXT extraction
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError("Unsupported format")  # Unsupported file type

def save_text(text, out_path):
    """
    Saves text to a file.

    Args:
        text (str): The text to save.
        out_path (str): Path where the file will be saved.
    """
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)

# === Example usage ===
file_path = "example_ru.pdf"         # Path to the input file
out_path = "translated_en.txt"       # Path for the translated file output

# Load the Russian → English translation model
translation = load_model("ru", "en")

# Extract text from the input file
text = extract_text(file_path)

# Translate the extracted text
translated = translation.translate(text)

# Save the translated text to the output file
save_text(translated, out_path)

# Print confirmation message
print(f"✅ Translation saved: {out_path}")
