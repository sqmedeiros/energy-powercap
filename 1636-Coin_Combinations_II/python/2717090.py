"""RANK1ZEN; 3966 PEAK; NA; FLEX SUPPORT: Zen, Bap; Battlenet ID -> Knuckles#11791"""
# region ---------------------------------------------------------------------------|
# MNNNNNNNNNNNNNNNNMNho///++//+oooooossssssssssssysssooyyyyyso+//++//shNNNNNNNNNNNNNM
# MNNNNNNNNNNNNNNMNy////////++++oooooooooossssssssoosssssysyyysoossss+/oshNNNNNNNNNNM
# MNNNNNNNNNNNNMNs///////+oooooo++++oooooooooooso+ossssssssssssssssssss++soymMNNNNNNM
# MNNNNNNNNNNNMd/:-//+//shNNmhsoo+++++++++ooooo++oooooooooossssssssssssso+ooosmNNNNNM
# MNNNNNNNNNNMh::://+/+ymMMMMmhsoso+++++++++o+/+ooooooooooooooooooooossso++o+++hMNNNM
# MNNNNNNNNNMy//-:/+/osmMMMMNhssyshNdssoooo++:++++++++++oooooooooooooooooo++-++/sMMNM
# MNNNNNNNNMd:/:///+/ohNMMMNhsohyyNMNNNdhhs+:++++++++++++++++++++ooooooooo/+.o+:/+NNM
# MNNNNNNNMm/:/-///++ooshmmhs+sysdMMMMNdMMd/+++++ooo++++++++++++++++++++++::-++/:/sNM
# MNNNNNNMN/://-+++++++++oo+//yosNMNMNmNMNo/o/oshNmhyoo+++++++++++++++++++/-/+++:/:sM
# MNNNNNMNo://-/+++++:/+++++//++osyhmdhMNs/o/+shMMMMmsooooyo++/+++++++++++://+++://oM
# MNNNNNMs:///:/++++//++-/+/:++++++ooooyo++o-oyNNMMmysooymmso/+shysyyysooo+/++o+/-s+M
# MNNNNMd:///+:/++++-++:`++:/++++//++++++:+-/oyhsmys+oohmyo++:sNMdmMMNNysy+-ohNs+-myM
# MNNNMN::///+-:+++:.+/``++/++++++++++++:+/`+++oo/:/++oyo+oy+odNddMMMMmyyh:-sdMh/odyN
# MNNNNo:///++-:+o/`::```++/+++++++++++//+-.o++:-:/++/+/+ymo/+ossyyhdhssy+.:ohhd/sy+M
# MMNMh-///+++--oo:`/````++-+++++++++++-o/`/+:.:/+++//+hmNo/++++++ooooooo-`/+o++/++-M
# MMMN/:///+++-.o/````-s:+/:++++++++++/++`.:.-/++++/+sdmmo/+++++++++++++: -+++++////M
# MMMh:///++++-`+:```/dN+/::++++++++++++:``.+ooo++ohNMNm++oooooooo+++++o+ :++++/-//oM
# MMd:/-/+++++-`/.``:hmm//./+++++++++o/o..:osoooymmdddmoooooooooooooo+oms.+++++////+M
# MMo// -+++++:`.`` dNddo-.:+++++++++++--/soo:.--::ymh+ssssssssssooo+sNN/++++++++/-dM
# Md/// `/+++o/```` dMddN.-:++++++++++/`/o/+:``-:-`/ooyssssssssssssoodmMo++++++++//NM
# M/:// `-+oooo.``` oMNMM+--/+++++++++/:yd-``.`-+o+hoyyoosyyyyyyys:+o+o++o//+++++/hMM
# m++:/```:oooo/````.dmNNm/-/+++++++//+dhy::ohs:/hysyosyyyyyyyyys:----:-/o/ooo++/-mMM
# s:++//```/oooo-  ``yNmdm:-/++++++////MMNmdhoys+ssssyyyyyysoysss:-.odd/o+/+oo++-+MMM
# s`:++/````:oooo. ```:hNNh-/++++++//:hNNNMMNMdsossyyyyyyss+osdM/o/:yNyoo///ooo/.MMNM
# d `-++/-```:+oo+-`````-+ds/++++++//-mMMMNNhs+syyysysyys+osdMMNyoshdh/+/o:ooo+.+MMNM
# M/` `-/+/-``.:ooo-```````s:++++++++/mNdhsoossssyyhyo/-+hmMMMMNNNNNNo//+.:oo++ oMMNM
# MMo``:..-//-.`-+oo:.`````/+++++++++:ooossyhyyyo+:-:ohNMmMMMMMNmNNNh:/:` :oo/: mMMNM
# MMMh.oMh+``.-:-.-/o+-````mh/+++++++:++++/:--:+syhmMMMMMNMMMMMMMMMo-.//``+oo:`-MMNNM
# MMMMh-omNd+````..`./+/.`hMMs+++++++/dmmmmNMMNNMMMMMMMMMMMMMMMMms:`` :/..+oo: yMNNNM
# MNNNMN/``..``````````.-.+dNy-oooooo/o+s++sNMMNmNMMmmNMMMMMMMmo-   ``-/.-oo+- yMNNNM
# MNNNNMMNdy-``````..``````-+o/+ooooo/++///:`:yMMMMMMMMMMMMds/`/++/````o--o++- MMNNNM
# MMNNMMMMMN:`........-:+oyssoo+ssssss:ooo+/+:`:mMMMMMNho/.````+ooohd+//:+ooo-/MMMMMM
# MMMMMMMMMMs.-...-.-osyyyyysdMhshhhhhossssssdh-.ss+/-.``----.sdhy+mMMMsosssy:sMMMMMM
# endregion ------------------------------------------------------------------------|
# region ---------------------------------------------------------------------------|
from sys import stdin, stdout, setrecursionlimit
from bisect import bisect_left, bisect_right
from math import ceil, floor, log, gcd, sqrt
from collections import Counter, deque
from heapq import heappush, heappop, heapify
from operator import mul
from functools import reduce
def re(): return stdin.readline().rstrip()
def ints(): return map(int, stdin.readline().split())
def test(cases):
    for _ in range(cases): solve()
mod = 1000000007
# endregion
# region ---------------------------------------------------------------------------|
def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


class Dsu:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return 0
        if self.rank[py] > self.rank[px]:
            px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]
        return 1

    def get_size(self, x):
        return self.rank[self.find(x)]
# endregion ------------------------------------------------------------------------|

def solve():
    n, x = ints()
    coins = sorted(ints())
    dp = [0] * (x + 1); dp[0] = 1

    for c in coins:
        for j in range(x + 1):
            if j + c > x: break
            dp[j + c] += dp[j] % mod 

    print(dp[-1] % mod)

    return

test(1)