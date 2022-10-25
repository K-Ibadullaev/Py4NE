def calc_newton(a, err=1e-6):

    """  x_min = x_n - f(x_n)/f'(x_n)
       f(x) = 1 - a/(x^2) -> instance function
       f'(x) = 2a/(x^3) ->
       """
 
    x1 = (1+a)/9.0
    x2 = x1 -(1-a/x1**2)/(2*a/x1**3)
    it =1
       
    while (abs(x2-x1)>=err):
        x1 = x2
        x2 = x1 - (1-a/x1**2)/(2*a/x1**3)
        it +=1
    return x2, it, abs(x2-x1)   
    
def sym_newton(fx, dfx,x0, err=1e-6):

    """  x_min = x_n - f(x_n)/f'(x_n)
       f(x) = 1 - a/(x^2) -> instance function
       f'(x) = 2a/(x^3) ->
       """
 
    x1 = x0
    x2 = x1 -fx(x1)/dfx(x1)
    it =1
       
    while (abs(x2-x1)>=err):
        x1 = x2
        x2 = x1 - fx(x1)/dfx(x1)
        it +=1
    return x2, it, abs(x2-x1)   
    