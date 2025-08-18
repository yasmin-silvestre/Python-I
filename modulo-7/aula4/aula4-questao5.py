livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 480],
    ["Ensaio Sobre a Cegueira", "José Saramago", 1995, 352],
    ["Grande Sertão: Veredas", "Guimarães Rosa", 1956, 608],
    ["Orgulho e Preconceito", "Jane Austen", 1813, 279],
    ["Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, 288],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1216]
]

with open("meus_livros.csv", "w", encoding="utf-8") as f:
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        f.write(",".join(map(str, livro)) + "\n")

print("Arquivo meus_livros.csv criado com sucesso!")
