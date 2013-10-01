import scipy
import scipy.integrate
import pylab as plt

beta = 0.003
gamma = 0.1

def SIR_model(X, t=0):         
        
	y = scipy.array([- beta*X[0]*X[1]
                          ,  beta*X[0]*X[1] - gamma*X[1]
                          , gamma*X[1] ])
	return y

if __name__ == "__main__":

        t = scipy.linspace(0, 60, num = 100)                         

        X0 = scipy.array([225, 1,0])
        X = scipy.integrate.odeint(SIR_model,X0,t)
        print(X)
        
        plt.plot(range(0, 100), X[:,0], 'o', color = "green")
        plt.plot(range(0, 100), X[:,1], 'x', color = "red")
        plt.plot(range(0, 100), X[:,2], '*', color = "blue")
        plt.show()
