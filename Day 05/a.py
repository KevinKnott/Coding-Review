class Solution:
    def findRotation(self, mat, target) -> bool:
        if mat == target:
            return True

        for _ in range(3):
            mat = self.rotate90(mat)

            print(mat)
            if mat == target:
                return True

        return False

    def rotate90(self, mat):
        return [list(r) for r in zip(*mat[::-1])]
