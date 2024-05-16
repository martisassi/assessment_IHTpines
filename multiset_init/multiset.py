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
        self.elemento = sorted(elems)           #the constructor sorts the elements of a list


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

        if type(e) == int or type(e) == float:   #if the element to be add is an int or float, append and sort the element
            self.elemento.append(e)
            self.elemento = sorted(self.elemento, key = int)
        
        elif type(e) == tuple:                   #if the element to be add is a tuple, each individual element in the tuple is appended with a for loop and sorted
            for elem in e:
                self.elemento.append(elem)
                self.elemento = sorted(self.elemento)
        
        print (f'New Multiset after adding the element {e} is: {self.elemento}')


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
        
        rep = self.elemento.count(e)   #rep is the number of times that the element 'e' is present in the object
                
        if rep > 0:
            self.elemento.remove(e)    #if the multiplicity of 'e' is > 0, the multiplicity is decreased 

        print (f'New Multiset after removing the element {e} is: {self.elemento}')


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
        rep = self.elemento.count(e) #rep is the number of times that the element 'e' is present in the object
        
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
        
        ms.elemento.extend(self.elemento)    #The elements of the object are added to the elements of New Multiset (ms)

        new_ms = MultiSet(ms.elemento)       #New Multiset is created 

        print(f"The union between the two Multisets is ms2: {new_ms.elemento}")
        
        return new_ms
        

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

        intersection = []                   #Create an empty list.    
        for i in self.elemento:             #Each element of the object is compared with the elements of the new ms multiset
            for j in ms.elemento: 
                if i == j:                  #if there is a match, that element is inserted into the empty list and removed from the ms multiset.
                    intersection.append(i)
                    ms.elemento.remove(j)
                else:
                    continue
                
        new_ms = MultiSet(intersection)

        print('The intersection between two Multisets is ms3:', new_ms.elemento)
        return new_ms


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

        diff = self.elemento       #Create a copy of the object
        print(diff)
        for j in ms.elemento:      #if each element of new multiset (j) is in diff, it is removed from diff
            if j in diff:
                diff.remove(j)
            
        
        new_ms = MultiSet(diff)

        print(f'The difference between two Multisets is: {new_ms.elemento}')
        return new_ms 


if __name__ == "__main__":
    ms1 = MultiSet([1, 1, 2, 4])        # ms1 = { 1, 1, 2,          4       }
    ms1.add(3)                          # ms1 = { 1, 1, 2,    3,    4       }
    ms1.add(3)                          # ms1 = { 1, 1, 2,    3, 3, 4       }
    ms1.add(2)                          # ms1 = { 1, 1, 2, 2, 3, 3, 4       }
    ms1.remove(1)                       # ms1 = { 1,    2, 2, 3, 3, 4       }   
    ms2 = ms1.union(MultiSet([4,5]))    # ms2 = { 1,    2, 2, 3, 3, 4, 4, 5 }
    ms2.remove(2)                       # ms2 = { 1,    2,    3, 3, 4, 4, 5 
    ms3 = ms1.intersection(ms2)         # ms3 = { 1,    2,    3, 3, 4       }
    ms1 = ms1.difference(ms3)                 # ms1 = {       2                   }
    print(ms1.membership_test(2))       # True
    print(ms1.membership_test(5))       # False
    
    print('Fine')