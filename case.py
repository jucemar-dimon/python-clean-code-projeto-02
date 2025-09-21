class MinhaClasse:
    def __enter__(self):
        print("Entrei aqui!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou no exit!")


with MinhaClasse() as mc:
    print("Entrei no with")
