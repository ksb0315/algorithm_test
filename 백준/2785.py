# 희원이는 그의 다락방에서 N개의 체인을 찾았다. 각각의 체인은 몇 개의 고리로 연결되어 있는데, 각각의 고리는 최대 두 개의 인접한 고리를 가질 수 있다. 각각의 고리는 열고 닫을 수 있다. 그래서, 체인을 분리하거나 두 체인을 연결하여 하나의 긴 체인으로 만들 수 있다. 희원이는 가능한 한 적은 고리를 열고 닫아서, 모든 체인을 하나의 긴 체인으로 연결하려고 한다.
# 예를 들어, 희원이가 세 개의 체인을 가지고 있고, 각 체인이 고리 하나로만 이루어져 있다면, 그 중 하나를 열어서 나머지 두 개를 연결하고 닫으면 된다.
# 체인의 개수와 각각의 체인의 길이가 주어지면, 하나의 긴 체인으로 모든 체인을 묶기 위해 희원이가 열고 닫아야할 최소한의 고리 수를 찾아라.

N = int(input())
chains = list(map(int, input().split()))

chains.sort()

chainCount = N
tiedChains = 1

for chain in chains:
    if tiedChains + chain >= chainCount:
        break
    else:
        tiedChains += chain
        chainCount -= 1
print(chainCount-1)