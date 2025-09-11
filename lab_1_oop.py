import sys
import math

def getCoef(index, mes):
    if len(sys.argv) > index:
        coef_str = sys.argv[index]
    else:
        print(mes)
        coef_str = input()
    return float(coef_str)

def getRoots(a, b, c):
    res = []
    D = b ** 2 - 4 * a * c
    sqD = D ** 0.5
    if D == 0.0:
        root = -b / (2.0 * a)
        if root > 0:
            orgRoot1 = root ** 0.5
            orgRoot2 = - (root ** 0.5)
            res.append(orgRoot1)
            res.append(orgRoot2)
        elif root == 0:
            res.append(root)
    if D > 0:
        root1 = - b - sqD / (2 * a)
        root2 = - b + sqD / (2 * a)
        if root1 > 0:
            orgRoot3 = root1 ** 0.5
            orgRoot4 = - (root1 ** 0.5)
            res.append(orgRoot3)
            res.append(orgRoot4)
        if root2 > 0:
            orgRoot5 = root2 ** 0.5
            orgRoot6 = - (root2 ** 0.5)
            res.append(orgRoot5)
            res.append(orgRoot6)
    return res
    
def main():
    a = getCoef(1, "Ведите коэффициент a:")
    b = getCoef(2, "Ведите коэффициент b:")
    c = getCoef(3, "Ведите коэффициент c:")
    roots = getRoots(a, b, c)
    cntRoots = len(roots)
    if cntRoots == 0:
        print("Корней нет")
    else:
        print(f"{cntRoots} корня:", *roots)
        

if __name__ == "__main__":
    main()