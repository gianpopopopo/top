class FF:

    def __init__(self,flujos,tasa):
        
        self.flujos = flujos
        self.tasa = tasa
        #self.p = int(input("Periodos a futuro: "))
        self.resultadova = []
        self.resultadovf = []
        
    
    def VA(self,tasa, n = 0):
        if n == len(self.flujos):
            return self.resultadova
        else: 
            self.resultadova.append(round(self.flujos[n]/((1+self.tasa)**(n)),2))
            return self.VA(tasa,n+1)
        
    def VF(self, n = 0):
        if n == len(self.flujos):
            None
        else:
            self.resultadovf.append(round(self.resultadova[n]*((1+self.tasa)**(self.p)),2))
            return self.VF(n+1), 
            
        
    def TIR(self, k=0):
        vanes = []
        for i in range(1, len(ff.flujos)):
            vanes.append(self.flujos[i]/(1+k)**i)
        van = self.flujos[0] + sum(vanes)
        if van < 0:
            return round(k,3)
        else:
            return self.TIR(k+0.001) 

        
        
def elija():
    e = input("elija si quiere el VA o VF de los flujos:")
    
    if e == "VA":
        print(ff.resultadova)
    elif e == "VF":
        print(ff.resultadovf)
    else:
        return None
    
ff = FF([-100000, 45000, 45000, 45000],0.1665)
#ff.VA(0.3)
#ff.VF()
print(ff.TIR())

#elija()

        


