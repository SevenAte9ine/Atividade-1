from Aluno import Aluno

class AlunoGraduacao(Aluno):
  def __init__(self,semestre = 2):
    self.semestre = semestre
  def imprimir(self):
    print("Semestre do Aluno: ", self.semestre)