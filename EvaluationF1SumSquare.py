from Evaluation import *

class EvaluationF1SumSquare(Evaluation) :
    
    
    def performance(self,coordonnees):
        performance=0
        for index in range(len(coordonnees)):
            performance=performance+coordonnees[index]**2
        return performance
