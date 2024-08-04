import PyPDF2
import re

def search_pdf(file_path, keywords):
    result_sentences = []
    pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"

    try:
        with open(file_path, "rb") as file:
            pdf = PyPDF2.PdfReader(file)
            num_pages = len(pdf.pages)
            index = 0
            for page_num in range(num_pages):
                page = pdf.pages[page_num]
                text = page.extract_text()

                sentences = re.split(pattern, text)
                for sentence in sentences:
                    sentence = sentence.strip()
                    if any(keyword.lower() in sentence.lower() for keyword in keywords):
                        sentence = re.sub(r"\n", " ", sentence)
                        index += 1 
                        result_sentences.append(f"{index}. {sentence}")

    except FileNotFoundError:
        print("File not found.")
        return []

    return result_sentences

# Example usage
file_path = "/Users/mac/Desktop/llm-agent/output.pdf"
keyword = ["Gross Margin"]

results = search_pdf(file_path, keyword)
output_file = "output.txt"
with open(output_file, "w") as f:
    f.truncate(0) 
    merged_sentences = "\n".join(results)
    f.write(merged_sentences)

print(f"Results have been saved to {output_file}.")
