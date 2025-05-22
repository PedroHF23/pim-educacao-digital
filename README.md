# pim-educacao-digital
Plataforma de Educação Digital para inclusão e segurança da informação.
O sistema que desenvolvemos utiliza a linguagem Python para construir as funcionalidades de controle de usuários e a interação deles com a plataforma de ensino. A escolha por Python se deve à sua facilidade de leitura e escrita, o que ajuda bastante na hora de criar e dar manutenção no código, além de ter várias ferramentas como as bibliotecas que facilitam o trabalho com os dados e os arquivos do computador.
Como o Código é Organizado
O código foi dividido em várias partes menores, chamadas de funções. Cada função tem uma tarefa específica, o que torna o código mais fácil de entender, usar novamente em outros lugares e corrigir eventuais problemas.
O Papel de Cada Função
1.	pega_os_usuarios() (Recupera Dados dos Usuários):
o	Essa função é responsável por ir buscar as informações dos usuários que estão guardadas no sistema.
o	Primeiro, ela verifica se o arquivo onde essas informações ficam armazenadas (arquivo_de_usuarios) existe.
o	Se o arquivo existir, a função abre para leitura, envia o conteúdo para a memória do computador e entrega esses dados como uma lista. Nessa lista, cada usuário é representado por um conjunto de informações (como nome, e-mail, etc.).
o	Caso o arquivo não exista, a função retorna uma lista vazia, indicando que ainda não há nenhum usuário cadastrado.
o	Para saber se o arquivo existe, usamos a função os.path.exists(). E para lidar com possíveis erros ao ler o arquivo JSON como por exemplo, se ele estiver vazio ou com algum problema, usamos o que chamamos de "try-except".
o	O "with open()" é um jeito de garantir que o arquivo será fechado corretamente depois de usá-lo, evitando problemas.
salva_os_usuarios() (Armazena Dados dos Usuários):
•	Essa função serve para guardar as informações dos usuários no arquivo JSON.
•	Ela recebe uma lista com os dados de todos os usuários (a_lista) e abre o arquivo para escrita.
•	Com a função json.dump(), ela pega essa lista e escreve tudo no arquivo, no formato JSON.
•	O "with open()" também é usado aqui para garantir que o arquivo seja fechado corretamente.
cria_novo_usuario() (Cria um Novo Cadastro):
•	Essa função é responsável por cadastrar novos usuários (alunos) no sistema.
•	Ela pede para o usuário digitar seu nome, e-mail e senha, usando a função input().
•	Em seguida, ela usa a função pega_os_usuarios() para obter a lista de usuários que já estão cadastrados.
•	A função verifica se o e-mail que o novo usuário digitou já existe no sistema. Se existir, ela avisa que o e-mail já está cadastrado e não faz nada.
•	Se o e-mail for novo, a função cria um "pacote" de informações (novo_usuario) com os dados do usuário, incluindo a informação de que ele ainda não começou nenhum curso.
•	Para finalizar, ela adiciona esse novo usuário à lista de usuários e usa a função salva_os_usuarios() para guardar tudo no arquivo.
fazer_login() (Realiza o Login):
•	Essa função cuida da parte de "entrar" no sistema.
•	Ela pede para o usuário digitar seu e-mail e senha, usando a função input().
•	Depois, ela usa a função pega_os_usuarios() para pegar a lista de usuários cadastrados.
•	A função verifica se existe algum usuário na lista com o e-mail e a senha que foram digitados.
•	Se encontrar, ela avisa que o login foi feito com sucesso e chama a função area_do_usuario() para mostrar o menu da área do usuário.
•	Se não encontrar, ela avisa que o e-mail ou a senha estão errados.
area_do_usuario() (Área do Usuário):
•	Essa função mostra o menu principal da área do aluno quando ele entra no sistema.
•	Ela permite que o usuário veja a lista de cursos, marque os cursos que já terminou e saia da área do usuário.
•	A função usa um "loop" (while) para mostrar o menu várias vezes, até que o usuário escolha sair.
•	A função input() é usada para saber qual opção o usuário escolheu.
•	A função acessa e troca as informações sobre o progresso do usuário nos cursos, guardadas em um "pacote" chamado progresso. Ela mostra o status dos cursos e atualiza quando o usuário marca um curso como terminado.
•	A função salva_os_usuarios() é chamada para guardar as mudanças no progresso do usuário.
principal() (Função Principal):
•	Essa é a função que começa a rodar o programa.
•	Ela mostra o menu principal da plataforma, com as opções de cadastrar, entrar ou sair.
•	Ela também usa um "loop" para mostrar o menu várias vezes, até que o usuário escolha sair.
•	A função input() é usada para saber qual opção o usuário escolheu.
•	A função chama as outras funções (cria_novo_usuario(), fazer_login()) para fazer o que o usuário escolheu.
•	A parte do código if __name__ == "__main__": serve para garantir que a função principal() só rode quando o programa for iniciado diretamente, e não quando ele for usado como parte de outro programa.
ferramenta usadass
•	Python: A linguagem de programação que escolhemos para construir o sistema.
•	JSON: O formato que usamos para guardar as informações dos usuários em arquivos.
•	Ferramentas do Python (Módulos): 
o	os: Ajuda a gente a mexer com o sistema operacional, tipo checar se um arquivo existe.
o	json: Ajuda a gente a trabalhar com as informações no formato JSON.
Como a gente pensou no sistema
•	Escolhemos o formato JSON porque ele é simples e fácil de usar para guardar as informações.
•	Dividimos o código em funções para deixar o sistema mais organizado e fácil de dar manutenção.
•	Usamos as ferramentas do Python para guardar e mexer com as informações dos usuários de um jeito eficiente.

