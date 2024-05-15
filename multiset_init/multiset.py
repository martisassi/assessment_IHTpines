"""
Class implementing multiset
Created Nov 2, 2020
Updated Feb 7, 2024
by Giulio Iannello
"""
from copy import deepcopy

class MultiSet(object):

    def __init__(self, elems = []):
        """
        choose a representation
        """
        self.elemento = sorted(elems)
        #print(self.elemento)


    def add(self, e):
        """
        add an element to the multiset

        Parameters
        ----------
        e : any hashable type
            element to be added.

        Returns
        -------
        None.

        """

        if type(e) == int or type(e) == float:
            print ('quello che ho inserito è un num')
            self.elemento.append(e)
            self.elemento = sorted(self.elemento, key = int)
        
        elif type(e) == tuple:
            print("TUPLA")
            for elem in e:
                self.elemento.append(elem)
                self.elemento = sorted(self.elemento)
       
            

        print(self.elemento)

    def remove(self, e):
    
        """
        decrease multiplicity of an element if it is > 0

        Parameters
        ----------
        e : any hashable type
            element whose multiplicity must be decreased

        Returns
        -------
        None.
        """
        
        rep = self.elemento.count(e)
                
        if rep > 0:
            self.elemento.remove(e)

        print(self.elemento)

      

    def membership_test(self, e):
        """
        returns True if element e has multiplicity > 1

        Parameters
        ----------
        e : any hashable type
            element to be checked.

        Returns
        -------
        Boolean
            if element e has multiplicity > 1

        """
        rep = self.elemento.count(e)
        
        if rep >= 1:
           return True
        else:
            return False
        

    def union(self, ms):
        '''
        return the multiset which is the union
        of the object with multiset ms

        Parameters
        ----------
        ms : Multiset
            multiset to be joined
        
        Returns
        -------
        new_ms : Multiset
            the union between the object and ms
        '''
        
        self.elemento.extend(ms.elemento)

        new_ms = MultiSet(self.elemento)
        print(f"The union between the two multisets is: {new_ms.elemento}")
        
        return new_ms.elemento
        

    def intersection(self, ms):
        """
        return the multiset which is the itersection
        of the object with multiset ms

        Parameters
        ----------
        ms : Multiset
            multiset to be intersected

        Returns
        -------
        new_ms : Multiset
            the intersection between the object and ms
        """
        pass

    def difference(self,ms):
        """
        return the multiset which is the difference
        of the object with multiset ms

        Parameters
        ----------
        ms : Multiset
            multiset to be subtracted

        Returns
        -------
        new_ms : Multiset
            the difference between the object and ms
        """
        pass


if __name__ == "__main__":
    ms1 = MultiSet([1, 1, 2, 4])        # ms1 = { 1, 1, 2,          4       }
    
    ms1.add(3)                          # ms1 = { 1, 1, 2,    3,    4       }
    ms1.add(3)                          # ms1 = { 1, 1, 2,    3, 3, 4       }
    ms1.add(2)                          # ms1 = { 1, 1, 2, 2, 3, 3, 4       }
    ms1.remove(1)                       # ms1 = { 1,    2, 2, 3, 3, 4       }   
    ms2 = ms1.union(MultiSet([7,5]))    # ms2 = { 1,    2, 2, 3, 3, 4, 4, 5 }
    ms2.remove(2)                       # ms2 = { 1,    2,    3, 3, 4, 4, 5 }
    #ms3 = ms1.intersection(ms2)         # ms3 = { 1,    2,    3, 3, 4       }
    #ms1 = ms1.difference(ms3)                 # ms1 = {       2                   }
    #print(ms1.membership_test(2))       # True
    #print(ms1.membership_test(5))       # False
    
    print('Fine')