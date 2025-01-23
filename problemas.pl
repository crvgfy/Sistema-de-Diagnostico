
% Base de Conhecimento: Problemas e Soluções
problema("Computador não liga", 
    "Verifique se o cabo de alimentação está conectado corretamente.").
problema("Internet lenta", 
    "Reinicie o modem e o roteador. Verifique se outros dispositivos estão consumindo muita largura de banda.").
problema("Tela azul", 
    "Pode ser causado por erro de hardware ou software. Tente reiniciar em modo seguro e atualizar os drivers.").
problema("Teclado não funciona", 
    "Verifique a conexão do teclado e certifique-se de que não há sujeira nos conectores.").
problema("Erro de driver", 
    "Abra o Gerenciador de Dispositivos e atualize o driver do dispositivo com erro.").

% Regra: Encontrar a solução para um problema dado
solucao(Problema, Solucao) :-
    problema(Problema, Solucao).
