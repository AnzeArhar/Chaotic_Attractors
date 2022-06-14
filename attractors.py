import numpy as np

def clifford(X, Y, a=-2.0, b=-2.4, c=1.1, d=-0.9):
    new_X = np.sin(a*Y) + c*np.cos(a*X)
    new_Y = np.sin(b*X) + d*np.cos(b*Y)
    return new_X, new_Y

def peter_de_jong(X, Y, a=0.97, b=-1.899, c=1.381, d=-1.506):
    new_X = np.sin(a*Y) - np.cos(b*X)
    new_Y = np.sin(c*X) - np.cos(d*Y)
    return new_X, new_Y

def tinkerbell(X, Y, a=0.9, b=-0.6013, c=2, d=0.5):
    new_X = X**2 - Y**2 + a*X + b*Y
    new_Y = 2*X*Y + c*X + d*Y
    return new_X, new_Y

def johnnY_svensson(X, Y, a=1.4, b=-1.56, c=1.4, d=-6.56):
    new_X = d*np.sin(a*X) - np.sin(b*Y)
    new_Y = c*np.cos(a*X) + np.cos(b*Y)
    return new_X, new_Y

def gumowski_mira(X, Y, a=-0.192, b=0.982):
    f = lambda t : a*t + 2 * (1-a) * t**2 * (1 + t**2)**(-2)
    new_X = b*Y + f(X)
    new_Y = f(new_X) - X
    return new_X, new_Y

def ssss(X, Y, a=1.468, b=2.407, c=0.194, d=1.438):
    new_X = np.sin(Y*b) + c*np.sin(X*b)
    new_Y = np.sin(X*a) + d*np.sin(Y*a)
    return new_X, new_Y

def quadratic_strange(X, Y, code="CVQKGHQTPHTE"):
    f = lambda c : -1.2 + (ord(code[c])-65)*0.1
    new_X = f(0) + f(1)*X + f(2)*X**2 + f(3)*X*Y + f(4)*Y + f(5)*Y**2
    new_Y = f(6) + f(7)*X + f(8)*X**2 + f(9)*X*Y + f(10)*Y + f(11)*Y**2
    return new_X, new_Y

def cubic_strange(X, Y, code="ISMHQCHPDFKFBKEALIFD"):
    f = lambda c : -1.2 + (ord(code[c])-65)*0.1
    new_X = f(0) + f(1)*X + f(2)*X**2 + f(3)*X**3 + f(4)*X**2*Y + f(5)*X*Y* + f(6)*X*Y**2 + f(7)*Y + f(8)*Y**2 + f(9)*Y**3
    new_Y = f(10) + f(11)*X + f(12)*X**2 + f(13)*X**3 + f(14)*X**2*Y + f(15)*X*Y* + f(16)*X*Y**2 + f(17)*Y + f(18)*Y**2 + f(19)*Y**3
    return new_X, new_Y

def bogdanov(X, Y, eps=0, k=1.2, mu=0):
    new_Y = Y + eps*Y + k*X*(X-1) + mu*X*Y
    new_X = X + new_Y
    return new_X, new_Y

def gingerbreadman(X, Y):
    new_X = 1 - Y + abs(X)
    new_Y = X
    return new_X, new_Y

def duffing(X, Y, a=2.75, b=0.2):
    new_X = Y
    new_Y = -b*X + a*Y - Y**3
    return new_X, new_Y

def henon(X, Y, a=1.4, b=0.3):
    new_X = 1 - a*X**2 + Y
    new_Y = b*X
    return new_X, new_Y

def ikeda(X, Y, u=0.918):
    T = 0.4 - 6/(1 + X**2 + Y**2)
    new_X = 1 + u*(X*np.cos(T) - Y*np.sin(T))
    new_Y = u*(X*np.sin(T) + Y*np.cos(T))
    return new_X, new_Y

def standard(X, Y, K=0.971635):
    new_X = (X + K*np.sin(Y)) % (2*np.pi)
    new_Y = (Y + new_X) % (2*np.pi)
    return new_X, new_Y

def zaslavskii(X, Y, eps=5, nu=0.2, r=2):
    mu = (1-np.exp(-r))/r
    new_X = (X + nu*(1 + mu*Y) + eps*nu*mu*np.cos(2*np.pi*X)) % (1)
    new_Y = np.exp(-r)*(Y + eps*np.cos(2*np.pi*X))
    return new_X, new_Y
