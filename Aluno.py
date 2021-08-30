class Aluno:
  def __init__(self,codigo = 143568, nome = "João", matricula = "2009201003009-8"):
    self.codigo = codigo
    self.nome = nome
    self.matricula = matricula
  def imprimir(self):
    print("Código do Aluno: ", self.codigo)
    print("Nome do Aluno: ", self.nome)
    print("Matrícula do Aluno: ", self.matricula)