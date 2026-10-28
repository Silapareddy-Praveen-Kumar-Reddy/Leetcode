class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[r // 3 * 3 + c // 3].add(ch)

        def solve():
            if not empties:
                return True

            best = 0
            best_opts = None
            for i, (r, c) in enumerate(empties):
                used = rows[r] | cols[c] | boxes[r // 3 * 3 + c // 3]
                opts = [d for d in "123456789" if d not in used]
                if best_opts is None or len(opts) < len(best_opts):
                    best, best_opts = i, opts
                    if len(opts) <= 1:
                        break

            if not best_opts:
                return False

            r, c = empties.pop(best)
            b = r // 3 * 3 + c // 3
            for d in best_opts:
                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)
                if solve():
                    return True
                rows[r].remove(d)
                cols[c].remove(d)
                boxes[b].remove(d)

            board[r][c] = '.'
            empties.insert(best, (r, c))
            return False

        solve()