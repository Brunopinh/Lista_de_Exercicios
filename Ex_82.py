# 82. Escreva um programa que remova stopwords de um texto dado.

# Stopwords comuns (exemplo, em português)
stopwords = ["a", "o", "as", "os", "e", "é", "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas", "um", "uma", "uns", "umas", "para", "com", "por", "que", "se", "como", "mas", "mais"]

texto = input("Digite um texto: ")
palavras = texto.lower().split() # Converte para minúsculas e divide em palavras

texto_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]
print(f"Texto sem stopwords: {' '.join(texto_sem_stopwords)}")