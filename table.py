'''
Name: Jeffrey Moniz
ID: 3148591
Course: CMPT 200 X04L
assignment: lab 6 - Table
'''

class Table: #use this table to hold the values
    class _Node:
        def __init__(self,key,val,pos_check):
            self._key = key
            self._value = val
            self._pos_check = pos_check
    def __init__(self,size=8):
        self._size = size
        self._table = [None]*self._size
    def __len__(self):
        '''
        purpose: returns the size of the table
        parameters: self
        returns: self._size
        '''
        return self._size
    def add(self,key,value):
        '''
        purpose: this function first checks to see if the table is full or not,
                 once done the function takes the users key and value and adds it 
                 to the table
        parameters: self, key, value
        pre: self._table is unaltered
        post: self._table has changed and added its new node of a key and value
        returns: None
        '''
        self._check_size()
        ind = hash(key)%self._size
        if self._table[ind] == None or self._table[ind]._key == key:
            self._table[ind] = self._Node(key,value,True)
            return
        while self._table[ind] != None and self._table[ind]._key != key:
            ind = (ind+1)%self._size 
        self._table[ind] = self._Node(key,value,True)
        return
    def get(self,key):
        '''
        purpose: this function takes the users key, hashes the key and checks if 
                 the key at that position is equal to the given key, if not traverse
                 the table. Once the program finds the key in the table that equals 
                 to the users key the program will return the value at that position
        parameters: self, key
        returns: either None or self._table[ind]._value
        '''        
        ind = hash(key)%self._size
        if self._table[ind] == None:
            return
        elif self._table[ind]._key == key:
            return self._table[ind]._value
        else:
            save = self._table[ind]._key
            ind = (ind+1)%self._size
            while self._table[ind] != None and self._table[ind]._key != save:
                if self._table[ind]._key == key:
                    return self._table[ind]._value
                else:
                    ind = (ind+1)%self._size
                    continue
            return
    def delete(self,key):
        pass
    def _check_size(self):
        '''
        purpose: this checks to see if the table is full or not, if it is full move
                 to the _create_table function, otherwise return
        parameters: self
        returns: None
        '''        
        size = 0
        for i in self._table:
            if i == None:
                continue
            size += 1
        if size == self._size:
            self._create_table()
        return
    def _create_table(self):
        '''
        purpose: this function creates a new table and places the old elements 
                 on the new table, the new table replaces the new table and the 
                 size is doubled
        parameters: self
        pre: self._table is unaltered
        post: self._table is doubled and the old elements are placed on the new table
        returns: None
        '''        
        self._size = self._size*2
        new_table = Table(self._size)
        for i in self._table:
            new_table.add(i._key,i._value)
        self._table = new_table._table
    def __str__(self):
        '''
        purpose: returns the string representation of the table in the form 'key: value'
        parameters: self
        pre: ret is an empty string
        post: ret has been string concatenated if the table is not empty
        returns: ret
        '''
        ret = ''
        for i in self._table:
            if i == None:
                continue
            print(i._key,i._value)
            ret += f"{i._key}: {i._value}"
            ret += ', '
        return ret
    def __repr__(self):
        '''
        purpose: returns the string representation of the table in the form 'key: value'
        parameters: self
        pre: ret is an empty string
        post: ret has been string concatenated if the table is not empty
        returns: ret
        '''
        ret = ''
        for i in self._table:
            if i == None:
                continue
            print(i._key,i._value)
            ret += f"{i._key}: {i._value}"
            ret += ', '
        return ret
    def keys(self):
        '''
        purpose: creates a set and adds each key in the table to the set
        parameters: self
        pre: s is an empty set
        post: the table has been traversed and the set may have keys in it
        returns: s
        '''        
        s = set()
        for i in self._table:
            if i == None:
                continue
            else:
                s.add(i._key)
        return s
    def load(self):
        '''
        purpose: traverses the table and checks the number of elements in the table
        parameters: self
        pre: size is initialized and set to 0
        post: the table has been traversed and size may be greater than 0
        returns: size
        '''        
        size = 0
        for i in self._table:
            if i == None:
                continue
            else:
                size += 1
        return size
    def __len__(self):
        '''
        purpose: traverses the table and checks the number of elements in the table
        parameters: self
        pre: size is initialized and set to 0
        post: the table has been traversed and size may be greater than 0
        returns: size
        '''        
        size = 0
        for i in self._table:
            if i == None:
                continue
            else:
                size += 1
        return size        