
from translation_module import translate_to_english
from code_generation_module import generate_code

def main(input_text, source_language="es"):
    try:
        translated_text = translate_to_english(input_text, source_language)
        code = generate_code(translated_text)
        return code
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
# print(main("Escribe una función en Python que sume dos números."))
