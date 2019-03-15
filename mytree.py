from bstiter import _BSTIterator



class BST:

  def __init__( self ):
  
    self._root = None
    self._size = 0
      
  def __len__( self ):
   
    return self._size

  def print( self ):
    if self._root != None:
      self._root.print()

  def __contains__( self, key ):
 
    return self._bstSearch( self._root, key ) is not None

  def _bstFindMin( self, subtree ):
   
    pass
  
  def _bstFindMax( self, subtree ):
   
    pass

  def add( self, key, value ):
   
    node = self._bstSearch( self._root, key )    
    
    if node is not None :
      node.value = value
      return False
   
    else :
      self._root = self._bstInsert( self._root, key, value )
      self._size += 1
      return True
     
  def remove( self, key ):
    
    assert key in self, "Invalid key to remove."
    self._root = self._bstRemove( self._root, key )
    self._size -= 1

  def findMin( self ):
  
    return self._bstFindMin( self._root )

  def findMax( self ):
    
    return self._bstFindMax( self._root )

  def __iter__( self ):
   
    return _BSTIterator( self._root )
     
  def _bstInsert( self, subtree, key, value ):
   
    if subtree is None :   
      subtree = _BSTNode( key, value )
    elif key < subtree.key :
      subtree.left = self._bstInsert( subtree.left, key, value )
    elif key > subtree.key :
      subtree.right = self._bstInsert( subtree.right, key, value )
    return subtree

  def _bstSearch( self, subtree, target ):        
   
    if subtree is None :         
      return None
    elif target < subtree.key : 
      return self._bstSearch( subtree.left, target )
    elif target > subtree.key : 
      return self._bstSearch( subtree.right,target )       
    else :                      
      return subtree                                
  
  def _bstRemove( self, subtree, target ):
    
    if subtree is None :  
      return subtree
    elif target < subtree.key :  
      subtree.left = self._bstRemove( subtree.left, target )
      return subtree
    elif target > subtree.key :  
      subtree.right = self._bstRemove( subtree.right, target )
      return subtree      
    else :     
      return self._bstDeleteNode( subtree )
        
  def _bstDeleteNode( self, node ):
    

    if node.left is None and node.right is None : 
        return None
    elif node.left is None or node.right is None :  
      if node.left is not None :
        return node.left
      else :
        return node.right
    else : 
      successor = self._bstFindMin( node.right )
      node.key = successor.key
      node.value = successor.value
      node.right = self._bstRemove( node.right, successor.key )
      return node


class _BSTNode :                       
  def __init__( self, key, value ):
    self.key = key
    self.value = value
    self.left = None
    self.right = None

  def __str__( self ):
    return str( self.value )


