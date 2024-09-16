# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado

nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
nota3 = float(input('terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
print('tiarndo {} e {}, a media do aluno é {:.1f}'. format(nota1, nota2, nota3, media))
if media >= 7:
    print('aprovado.')
elif media == 5 and media < 7:
    print('recuperação')
elif media < 5:
    print('reprovado')