## Código por Gabriel Moretti de Souza
## Resolvendo exercício 91 - Projeto Euler

## Função feita para retornar verdadeiro caso o triângulo encontrado tenha um ângulo reto,
##  ou seja, os valores dos seus lados respeitam a fórmula de Bhaskara.
def descobrirTriangulo(disPQ, disPO, disQO):
    return (disPQ+disPO==disQO) or (disQO+disPO==disPQ) or (disPQ+disQO==disPO)

## Declaração de uma variável 'k' para o número desejado de coordenadas máximas,
##  nesse caso, 0 ≤ x1, y1, x2, y2 ≤ 50 .
## Junto com ela, a declaração inicial do número de triângulos retos encontrados no intervalo.
k = 50
triangulosRetos = 0

##Alguns 'for' percorrendo todos os valores possíveis para as coordenadas.
for q_x in range(k+1):
    for q_y in range(k+1):
        for p_x in range(k+1):
            for p_y in range(k+1):
                ## Para saber se os triângulos são retos, primeiro precisamos saber
                ##  o valor de seus lados.
                ## A raiz quadrada da fórmula da distância se cancela com as potências
                ##  da fórmula de Bhaskara.
                distanciaQO = pow(q_x,2) + pow(q_y,2)
                distanciaPQ = pow((q_x - p_x),2) + pow((q_y - p_y),2)
                distanciaPO = pow(p_x,2) + pow(p_y,2)

                ## Primeira condição confere se os valores dos dois lados não entrem em conflito.
                ## Segunda condição confere se o triângulo com essas 3 distâncias é reto.
                ## Caso verdadeiras, foi encontrado um triângulo reto no intervalo.
                if p_y * q_x < q_y * p_x and descobrirTriangulo(distanciaPQ,distanciaPO,distanciaQO):
                    triangulosRetos += 1

## Impressão do resultado.       
print(triangulosRetos)
