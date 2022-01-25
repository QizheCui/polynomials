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
