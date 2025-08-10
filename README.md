# 🌍 Offline Document Translator  
*Translate PDF, DOCX, and TXT files quickly and privately — all offline!*

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)

---

## ✨ Features
✅ **Multi-format support** — Works with `.pdf`, `.docx`, `.txt`  
✅ **Offline translations** — Powered by [Argos Translate](https://github.com/argosopentech/argos-translate)  
✅ **Privacy-first** — No data leaves your computer  
✅ **Custom language pairs** — Easily change source and target languages  
✅ **Easy to use** — Simple Python script with clear functions  

---

## 📦 Installation

### 1️⃣ Install Python dependencies
```bash
pip install argostranslate pdfplumber docx2txt
```

### 2️⃣ Install a translation model  
Run the following Python snippet **once** to install the desired language model (example: Russian → English):

```python
import argostranslate.package, argostranslate.translate

# Update package index
argostranslate.package.update_package_index()

# Get available models
available_packages = argostranslate.package.get_available_packages()

# Install Russian → English
package = next(pkg for pkg in available_packages if pkg.from_code == "ru" and pkg.to_code == "en")
argostranslate.package.install_from_path(package.download())
```

You can change `"ru"` and `"en"` to any other supported language codes (e.g., `"fr"` for French, `"es"` for Spanish).

---

## 🛠 Usage

### Basic usage (run from terminal)
```bash
python translator.py
```

### Example inside the script
```python
file_path = "example_ru.pdf"         # Input file path
out_path = "translated_en.txt"       # Output file path

translation = load_model("ru", "en") # Load model
text = extract_text(file_path)       # Extract text
translated = translation.translate(text) # Translate text
save_text(translated, out_path)      # Save result

print(f"✅ Translation saved: {out_path}")
```

---

## 📂 Project Structure
```
translator.py       # Main script
example_ru.pdf      # Example input file
translated_en.txt   # Example translated output
```

---

## 🔍 How It Works

1. **Load Translation Model**  
   The `load_model(from_code, to_code)` function finds the installed language pair model.

2. **Extract Text**  
   The `extract_text(file_path)` function:
   - Uses `pdfplumber` for `.pdf`
   - Uses `docx2txt` for `.docx`
   - Reads directly for `.txt`

3. **Translate**  
   The translation object processes the extracted text **offline**.

4. **Save Output**  
   The `save_text(text, out_path)` function writes the translated text to a `.txt` file.

---

## ⚙ Functions Overview

| Function | Description | Example |
|----------|-------------|---------|
| `load_model(from_code, to_code)` | Loads Argos Translate model for a given language pair. | `load_model("ru", "en")` |
| `extract_text(file_path)` | Extracts text from `.pdf`, `.docx`, `.txt` files. | `extract_text("myfile.pdf")` |
| `save_text(text, out_path)` | Saves text to file. | `save_text("Hello", "out.txt")` |

---

## 🌐 Supported Languages
You can use **any languages available in Argos Translate**. Examples:

| Code | Language   |
|------|-----------|
| `en` | English   |
| `ru` | Russian   |
| `fr` | French    |
| `es` | Spanish   |
| `de` | German    |
| `it` | Italian   |

---

## 📜 License
This project is released under the [MIT License](LICENSE).

---

## 💡 Tips
- For **better translations**, split large documents into smaller chunks.
- For **PDFs with images**, use OCR tools like [pytesseract](https://github.com/madmaze/pytesseract) before translation.
- Works completely **offline** after model installation — safe for sensitive data.

---

## 🚀 Example Workflow
1. Place your file in the script directory.  
2. Run the script:  
   ```bash
   python translator.py
   ```
3. Get your translated `.txt` file in seconds.  
4. Enjoy your **private, offline translation**!  
