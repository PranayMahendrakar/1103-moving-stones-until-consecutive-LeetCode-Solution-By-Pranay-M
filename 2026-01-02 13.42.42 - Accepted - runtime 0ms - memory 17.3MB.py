class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        # Sort positions
        x, y, z = sorted([a, b, c])
        
        # Maximum moves: move endpoint stones one at a time
        max_moves = (z - y - 1) + (y - x - 1)
        
        # Minimum moves
        if z - x == 2:  # Already consecutive
            min_moves = 0
        elif y - x <= 2 or z - y <= 2:  # One gap of 1 or 2
            min_moves = 1
        else:
            min_moves = 2
        
        return [min_moves, max_moves]