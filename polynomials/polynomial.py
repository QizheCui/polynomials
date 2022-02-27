from numbers import Number

class Polynomial: #don't need (object) as this is python2 requirement
    def __init__(self,coefs):
        """set attribute"""
        self.coefficients = coefs
        #the init return nothing, it just set
        #up the attribute


    def degree(self): #an ordinary method
        
        return len(self.coefficients )-1 
        #so self.degree() return the len -1 


    #why can we directly print p =PolynomiaL((1,2))
    #because python doesn't know what to print out
    #since p is just an object in the class
    def __str__(self):
        coefs = self.coefficients
        terms =[] #a list of term x

        # Degree 0 and 1 terms conventionally have different representation.
        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() > 0 and coefs[1]:
            terms.append(f"{'' if coefs[1]==1 else coefs[1]}x")

        # Remaining terms look like cx^d, though factors of 1 are dropped.
        terms += [f"{'' if c == 1 else c}x^{d}" for d, c in enumerate(coefs[2:], start=2) if c]

        # Sum polynomial terms from high to low exponent.
        return " + ".join(reversed(terms)) or "0"

    def __eq__(self, other):

        return self.coefficients == other.coefficients

    def __add__(self,other): 
        #we can just add the coefficients straight because tuple addition
        #is concatenate, we need to loop over the tuple and add them together
        if isinstance (other, Polynomial):#this only works when self and other are poly
            #first we need to work out the minimal common degree of both
            common = min(self.degree(), other.degree()) +1 #e.g. x^3, y^2 return 2+1=3

            coefs = tuple(a+b for a,b in zip(self.coefficients,other.coefficients))
            #zip will stop when either of them run out
            #now we need to deal with coefs in the longer poly that is not in the other poly
            coefs += self.coefficients[common:] + other.coefficients[common:]
            #now coefs is complete

            return Polynomial(coefs) #return a new object with type class

        elif isinstance(other,Number):
            return Polynomial( (self.coefficients[0]+other,)+
                                self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other  #it is going to call the __add__ method above
        #if 5.__add__(p)  fail python will then try
        # p.__radd__(5) in this case is p+5               

