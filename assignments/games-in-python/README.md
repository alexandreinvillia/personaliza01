
# 📘 Assignment: Python Hangman Game

## 🎯 Objective

Desenvolver um jogo da Forca em Python usando manipulação de strings, condicionais e loops. Ao final, o aluno deverá implementar a lógica completa de adivinhação com tentativas limitadas e mensagens claras para o jogador.

## 📝 Tasks

### 🛠️ Build the Hangman Game Loop

#### Description
Implemente um jogo da Forca que escolha uma palavra aleatória de uma lista predefinida e permita que o jogador tente adivinhar letras, uma por vez, até vencer ou perder.

#### Requirements
Completed program should:

- Selecionar uma palavra aleatoriamente de uma lista predefinida.
- Aceitar apenas um palpite de letra por rodada e exibir o progresso atual da palavra no formato `_ _ _`.
- Rastrear e exibir a quantidade de tentativas incorretas restantes a cada rodada.
- Informar ao jogador quando uma letra já tiver sido tentada anteriormente.
- Encerrar o jogo quando a palavra for completamente adivinhada ou quando as tentativas acabarem.
- Exibir uma mensagem final de vitória ou derrota, incluindo a palavra secreta no fim do jogo.

Exemplo de interação esperada:

```text
Palavra: _ _ _ _ _
Tentativas restantes: 6
Digite uma letra: a

Boa tentativa! Palavra: _ a _ a _
Tentativas restantes: 6
```