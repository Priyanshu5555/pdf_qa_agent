import pymupdf

pdf = pymupdf.open("documents/PY.Resume.pdf")

text = ""

for page in pdf:
    text += page.get_text()

pdf.close()

chunk_size = 500

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print("\n--- Chunk", i + 1, "---")
    print(chunk)