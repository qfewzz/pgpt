import json
from pathlib import Path
from llama_index.readers.file.docs import (  # type: ignore
    DocxReader,
    HWPReader,
    PDFReader,
)

output_text_file = open('_output_text.txt', 'w', encoding='utf-8')
output_chars_file = open('_output_chars.txt', 'w', encoding='utf-8')
chars = dict()

file_path = r"""C:\_projects\_RAG_test\Ae.pdf"""
documents = PDFReader().load_data(Path(file_path))
for document in documents:
    # document.text = document.text.replace('ة', 'ه').replace('ي', 'ی').replace('ء', ' ')
    output_text_file.write(document.text)
    for char in document.text:
        count = chars.get(char, 0)
        chars[char] = count + 1

num_pages = len(pdf.pages)

for page in range(num_pages):
                    # Extract the text from the page
                    page_text = pdf.pages[page].extract_text()
                    page_label = pdf.page_labels[page]

                    metadata = {"page_label": page_label, "file_name": file.name}
                    if extra_info is not None:
                        metadata.update(extra_info)

                    docs.append(Document(text=page_text, metadata=metadata))


chars_sorted = list(map(lambda a : f'{a[0]}\n{a[1]}',sorted(chars.items(), key=lambda a: a[0])))
output_chars_file.write('\n----------------------------\n'.join(chars_sorted))

output_text_file.close()
output_chars_file.close()
