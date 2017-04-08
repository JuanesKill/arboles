class Nodo():
    def __init__ (self, valor, hijos=[]):
        self.valor=valor
        self.hijos=hijos
        
def mostrar(Nodo):
    print Nodo.valor
    [mostrar(x) for x in Nodo.hijos]


def validar(Nodo, palabra):
    if Nodo.valor == palabra:
        return mostrar(Nodo)
    else:
        return [validar(x,palabra) for x in Nodo.hijos]

n=Nodo('',[Nodo('c',[Nodo('ca',[Nodo('cal',[Nodo('calado',[])])
                                 ,Nodo('cas',[Nodo('casa',[Nodo('car',[]),Nodo('carro',[Nodo('carrazo',[])])])])])
                ,Nodo('ce',[Nodo('cer',[Nodo('cero',[Nodo('ceros',[Nodo('cerro',[Nodo('cerros',[])])])])]),
                                  Nodo('cej',[Nodo('ceja',[Nodo('cejas',[])])])])
                ,Nodo('ci',[Nodo('cia',[Nodo('cian',[])]),
                                  Nodo('civ',[Nodo('civil',[Nodo('civiles',[Nodo('civiliza',[]),Nodo('civilizacion',[Nodo('civilizado',[])])])])]),
                                  Nodo('cir',[Nodo('circo',[Nodo('circos',[]),Nodo('circa',[])]),Nodo('circunferencia',[Nodo('circunscrito',[])])])])
                ,Nodo('co',[Nodo('col',[Nodo('coles',[Nodo('colera',[]),Nodo('colores',[])])]),
                                  Nodo('cot',[Nodo('cota',[Nodo('cotas',[])]),
                                                    Nodo('cora',[Nodo('corazon',[]),Nodo('corazones',[])])])])
                ,Nodo('cu',[Nodo('culo',[Nodo('culos',[Nodo('culadas',[])])]),
                                  Nodo('cue',[Nodo('cueva',[Nodo('cuevas',[]),Nodo('cuevana',[])]),
                                                    Nodo('cuen',[Nodo('cuento',[])])])])])
                ,Nodo('s',[Nodo('sa',[Nodo('sal',[Nodo('sales',[])])
                                 ,Nodo('sau',[Nodo('sauna',[Nodo('saunas',[]),Nodo('sauce',[Nodo('sauces',[])])])])])
                ,Nodo('se',[Nodo('ser',[Nodo('serio',[Nodo('seria',[Nodo('serra',[Nodo('serral',[])])])])]),
                                  Nodo('set',[Nodo('seta',[Nodo('setos',[])])])])
                ,Nodo('si',[Nodo('sir',[Nodo('siro',[])]),
                                  Nodo('sil',[Nodo('sili',[Nodo('silicio',[Nodo('silicios',[]),Nodo('silantro',[Nodo('silla',[])])])])]),
                                  Nodo('sic',[Nodo('sico',[Nodo('sicar',[]),Nodo('sicode',[])]),Nodo('sicodelia',[Nodo('sicodelico',[])])])])
                ,Nodo('so',[Nodo('sor',[Nodo('soro',[Nodo('sorte',[]),Nodo('sorteo',[])])]),
                                  Nodo('sos',[Nodo('sose',[Nodo('sosiego',[])]),
                                                    Nodo('sol',[Nodo('soles',[]),Nodo('solecito',[])])])])
                ,Nodo('su',[Nodo('sus',[Nodo('susu',[])]),
                                  Nodo('sur',[Nodo('surco',[Nodo('surca',[]),Nodo('surcos',[])]),
                                                    Nodo('suci',[Nodo('sucia',[])])])])])])
                

cadena = raw_input("Digite una palabra:")
validar(n,cadena)

