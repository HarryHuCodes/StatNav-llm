import PyPDF2
import re

def search_pdf(file_path, keyword):
    result_sentences = []
    pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"

    try:
        with open(file_path, "rb") as file:
            pdf = PyPDF2.PdfReader(file)
            num_pages = len(pdf.pages)

            for page_num in range(num_pages):
                page = pdf.pages[page_num]
                text = page.extract_text()

                sentences = re.split(pattern, text)
                relevant_sentences = [sentence.strip() for sentence in sentences if keyword.lower() in sentence.lower()]

                for i, sentence in enumerate(relevant_sentences, start=1):
                    sentence = re.sub(r"\n", " ", sentence) 
                    result_sentences.append(f"{i}. {sentence}")

    except FileNotFoundError:
        print("File not found.")
        return []

    return result_sentences

# Example usage
file_path = "297.pdf"
keyword = "international"

results = search_pdf(file_path, keyword)
output_file = "output.txt"
with open(output_file, "w") as f:
    f.truncate(0)  # Clear the file
    merged_sentences = "\n".join(results)
    f.write(merged_sentences)

print(f"Results have been saved to {output_file}.")
