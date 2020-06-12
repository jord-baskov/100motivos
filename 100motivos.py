#/usr/bin/env python
# -*- coding: utf-8 -*-

#BY SR.STORM 


print('OI AMOR DA MINHA VIDA!!ESTE É MEU PRESENTE DO DIA DOS NAMORADOS PRA VOCE!!.\n\nSÃO 100 MOTIVOS PELOS QUAIS EU TE AMO.')
print('❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤')

RESPOSTAS = {
    '1': 'Eu amo o seu sorriso',
    '2': 'Eu amo sua sinceridade',
    '3': 'Eu amo o jeito que você fala comigo',
    '4': 'Eu amo como você planeja o nosso futuro',
    '5': 'Eu amo como você esta em todos os meus planos',
    '6': 'Eu amo como você me dá um motivo para eu te amar mais todos os dias',
    '7': 'Eu amo nossos assuntos',
    '8': 'Eu amo a nossa falta de assunto',
    '9': 'Eu amo como você não precisa de esforço pra me fazer sorrir',
    '10': 'Eu amo como todo mundo gosta de você. Mas eu tenho ciúmes',
    '11': 'Eu amo como você fez eu confiar em você, para estar contigo até hoje',
    '12': 'Eu amo como você faz meu coração bater mais depressa',
    '13': 'Eu amo sua respiração',
    '14': 'Eu amo a sua persistência',
    '15': 'Eu amo todas as partes do seu corpo',
    '16': 'Eu amo as suas manias',
    '17': 'Eu amo quando você me corrige',
    '18': 'Eu amo a sua educação',
    '19': 'Eu amo como você me conhece',
    '20': 'Eu amo as suas perguntas',
    '21': 'Eu amo quando você concorda com minhas ideias loucas',
    '22': 'Eu amo viajar em pensamentos com você',
    '23': 'Eu amo nosso jeito “criança',
    '24': 'Eu amo nosso jeito “maduro”',
    '25': 'Eu amo o nosso jeito ”foda',
    '26': 'Eu amo como aprendi a ser melhor contigo',
    '27': 'Eu amo como você faz tudo ficar bem',
    '28': 'Eu amo dormir pensando em você',
    '29': 'Eu amo acordar pensando em você',
    '30': 'Eu amo sonhar com você',
    '31': 'Eu amo como pensamos até nos detalhes do nosso futuro',
    '32': 'Eu amo como tudo acontece naturalment',
    '33': 'Eu amo ouvir você dizendo “amor”',
    '34': 'Eu amo ouvir você dizendo “amor”',
    '35': 'Eu amo quando eu falo demais, e mesmo assim você me ouve com atenção',
    '36': 'Eu amo você é mais do que eu esperava pra ser "o amor da minha vida"',
    '37': 'Eu amo você ter aparecido no momento em que eu mais precisei',
    '38': 'Eu amo saber que nosso amor é sincero',
    '39': 'Eu amo saber que nosso amor não é frágil',
    '40': 'Eu amo a sua letra',
    '41': 'mesmo antes de descobrir que te amava tanto, eu já sentia necessidade de estar com você.',
    '42': 'Eu amo quando você me ouve',
    '43': 'Eu amo Você traz o meu melhor',
    '44': 'Eu amo como meus planos envolvem você',
    '45': 'Eu amo ouvir a sua voz me chamando',
    '46': 'Eu amo Você vê em mim o que ninguém vê',
    '47': 'Eu amo porque mesmo longe eu sinto você perto',
    '48': 'Eu amo a gente discute nossos problemas',
    '49': 'Eu amo gente nunca briga',
    '50': 'Eu amo porque juntos temos um sonho',
    '51': 'Eu amo como você ama sua família',
    '52': 'Eu amo como você fala de tudo comigo',
    '53': 'Eu amo como você não tem vergonha comigo',
    '54': 'Eu amo como você me repreende às vezes',
    '55': 'Eu amo como você luta pelas coisas que quer',
    '56': 'Eu amo como você não desistiu de mim, mesmo depois de 4 anos',
    '57': 'Eu amo como você me faz mais feliz a cada dia',
    '58': 'Eu amo como você não precisa falar nada pra dizer que ama',
    '59': 'Admito que quero ter mais tempo com você ',
    '60': 'Eu amo como você responde minhas perguntas do seu passado',
    '61': 'Eu amo como penso em você ao escutar uma música',
    '62': 'Eu amo como você é meu pensamento constante',
    '63': 'Eu amo como você sabe que eu te amo',
    '64': 'Eu amo como eu gasto horas pra escrever coisas pra você',
    '65': 'Eu te amo porque você me ensinou como é fácil te amar, mas não me ensinou como te esquecer (tudo bem, eu não preciso dessa lição) ',
    '66': 'Eu te amo porque eu posso contar tudo pra você sempre',
    '67': 'Eu te amo porque eu conto tudo pra você sempre, de qualquer jeito',
    '68': 'Eu amo como a cada dia você me conquista mais e de um jeito novo',
    '69': 'Eu amo você sempre se preocupa comigo',
    '70': 'Eu amo porque vamos ficar ricos juntos (ou não)',
    '71': 'Eu amo quando você discorda de mim, fazendo com que eu reflita sobre as coisa',
    '72': 'Eu amo como você está tendo paciência pra ler tudo isso',
    '73': 'Eu amo como estes motivos são só nossos',
    '74': 'Eu amo como você busca alternativas para o meu crescimento',
    '75': 'Eu amo como você sonha junto comigo',
    '76': 'Eu amo como você vai dar graças a Deus quando estiver acabando de ler isso tudo',
    '77': 'Eu te amo porque sem você sou incompleto',
    '78': 'Eu te amo porque você me faz rir a qualquer hora',
    '79': 'Eu amo como teu amor me faz forte',
    '80': 'Eu te amo porque assim como a Lua sabe que não está só porque tem o Sol eu sei que não estou sozinho porque tenho você',
    '81': 'Eu amo eu te amo mesmo quando me deixa preocupado',
    '82': 'Eu te amo porque se isso não é amor, o que mais pode ser?',
    '83': 'Eu te amo porque só de pensar em te perder por um segundo, eu sei que isso é o fim do mundo',
    '84': 'Eu amo como você sempre me surpreende',
    '85': 'Eu te amo porque eu não vivo sem você um segundo',
    '86': 'Eu amo como eu não consigo te esquecer',
    '87': 'Eu te amo porque amor igual ao teu, eu nunca mais terei, amor que eu nunca vi igual, que eu nunca mais verei',
    '88': 'Eu amo como eu não existo longe de você, e a solidão é meu pior castigo',
    '89': 'Eu amo como sua mãe é simpatica comigo',
    '90': 'Eu amo a forma que voce me incentiva ser melhor',
    '91': 'Eu amo o seu jeitinho quando ta com vergonha',
    '92': 'Eu amo quando voce me pede ajuda(me sinto o cara inteligente)',
    '93': 'Eu amo quando você manda foto zoada',
    '94': 'Eu amo como nossos pensamentos combinam',
    '95': 'Eu amo comonos respeitamos',
    '96': 'Eu amo o seu jeito ansiosa',
    '97': 'Eu te amo de todas as formas possiveis',
    '98': 'Eu amo saber que é com voce que vou passar o restante dos meus dias',
    '99': 'Eu amo o fato de sermos um casal dev',
    '100': 'Eu amo voce de todas as formas que voce puder imaginar.',
}

DEFAULT = 'Huum, não entendi essa resposta :('

while True:
    print("Vamos comecar!! Escolha um numero?")
    print("Essas são suas opções:", list(RESPOSTAS.keys()), '?')
    
    escolha = input("Numero: ")
    
    print(RESPOSTAS.get(escolha, DEFAULT))
    
    confirm = input('Gostaria de ver outro? [S/n] ')
    
    if confirm in ['n', 'N', '']:
        break
    else:
        print()
        
print('Volte quantas vezes quiser'.format(escolha))
    
