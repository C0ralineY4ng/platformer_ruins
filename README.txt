README – Projeto Platformer Ruins Python (PgZero)
Descrição do Projeto

Este projeto é um jogo platformer criado em Python usando apenas a biblioteca PgZero, com movimentação de personagem, inimigos com território limitado, e rolagem de tela. O objetivo principal é avaliar o conhecimento em Python, lógica de programação, manipulação de sprites, animações e sons.

O projeto foi desenvolvido de forma autoral, seguindo as regras de PEP8, e respeitando os módulos permitidos: pgzero, math, random e pygame.Rect.

O jogo atualmente contém:

-Menu principal com botões clicáveis (Começar jogo, Música e Sons, Sair) – parcialmente implementado.

-Plano de fundo e chão com rolagem infinita.

-Player com movimentação lateral e pulo.

-Inimigos (ghost e bat) com movimento dentro de limites específicos (território).

-Estrutura básica para score.

O que já foi implementado

-Menu principal

-Estrutura inicial e botões desenhados no menu.

-Clique para iniciar o jogo ou voltar ao menu.

-Player

-Movimentação horizontal (esquerda/direita).

-Pulo com gravidade.

Sprite inicial definido e desenhado na tela.

Inimigos

-Ghosts: movem-se horizontalmente dentro de um território definido.

-Bats: movem-se horizontal e verticalmente dentro de limites.

-Sistema de movimentação aleatória controlada por move_count e vx/vy.

-Rolagem do cenário

-Fundo e chão se movem conforme player se aproxima do limite da tela.

-Tiles do chão desenhados dinamicamente.

O que ainda falta implementar

-Para que o projeto esteja completo e dentro dos requisitos do enunciado, os seguintes pontos precisam ser adicionados:

-Menu completo com botões funcionais

-Alternar música e sons on/off.

-Música e efeitos sonoros

-Música de fundo contínua.

-Sons para pulo, ataques e colisões.

-Sprites e animações

-Player: animação ao se mover (correr) e pular.

-Ghosts: animação de movimento e “morte” ao ser atacado.

-Bats: animação batendo asas.

-Ataque do player

-Definir mecânica: pular sobre ghost para derrotá-lo.

-Colisão entre player e inimigos que cause dano ou morte.

-Score aumenta ao derrotar inimigos.

-Múltiplos inimigos e aleatoriedade

-Gerar inimigos em posições aleatórias dentro de limites do mapa.

-Criar spawn contínuo ou por tempo para aumentar desafio.

Interface do jogo

Painel com score e vidas do player.

Feedback visual de ataques e colisões.

Polimento

Próximos passos sugeridos

-Criar classes:

-class Player(Actor)

-class Enemy(Actor) com subclasses Ghost e Bat para comportamentos diferentes.

Implementar animações:

-Criar listas de sprites para cada estado (idle, run, jump, attack).

-Alternar imagens usando um contador ou timer para animação.

-Implementar ataques e colisões:

-Colisão player-inimigo.

-Aumentar score e remover inimigos derrotados.

-Menu interativo completo:

-Criar funções para ligar/desligar música e efeitos.

-Testes e ajustes finais:

-Testar limites de movimento dos inimigos (território).

-Testar rolagem de fundo com tiles e obstáculos.

-Garantir que não existam bugs de movimento, colisão ou spawn de inimigos.

Observações finais

-O projeto ainda não possui música, sons e animações completas.

-A mecânica de ataque do player e score ainda precisa ser implementada.