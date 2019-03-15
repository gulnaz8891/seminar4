class _BSTIterator :      
  def __init__( self, root ):
   
    self._theKeys = list()
    self._curItem = 0   
    self._bstTraversal( root )     
    self._curItem = 0    
    
  def __iter__( self ):
    return self


  def __next__( self ):
    if self._curItem < len( self._theKeys ) :
      key = self._theKeys[ self._curItem ]
      self._curItem += 1
      return key
    else :
      raise StopIteration
      
    
  def _bstTraversal( self, subtree ):
    if subtree is not None :
      self._bstTraversal( subtree.left )
      self._theKeys.append( subtree.key )
      self._curItem += 1
      self._bstTraversal( subtree.right )       
