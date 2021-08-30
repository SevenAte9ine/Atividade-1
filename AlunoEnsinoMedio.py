from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):
  def __init__(self, ano = 3):
    self.ano = ano
  def imprimir(self):
    print("Ano do Aluno: ", self.ano)