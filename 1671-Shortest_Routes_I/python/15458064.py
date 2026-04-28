import heapq

def dijkstra_repulesi_utak(utak_adj_list, kezdopont):
    tavolsagok = [float('inf')]*(n+1) #nullás index nem használása
    szulok = [None]*(n+1)
    csucsok_prioritasi_sora = []
    #csúcsok eltárolása prioritási sorban legrövidebb úthosszak szerint
    #for csucs in utak_adj_list.keys():
    #    heapq.heappush(csucsok_prioritasi_sora, (min(utak_adj_list[csucs]), csucs))
    heapq.heappush(csucsok_prioritasi_sora, (0, kezdopont))
    tavolsagok[kezdopont]=0
    while csucsok_prioritasi_sora:
        #visszaalakítás egyszerű csúcsra útvonal nélkül
        jelenlegi_suly, jelenlegi_csucs=heapq.heappop(csucsok_prioritasi_sora)
        #heap-ről kivett csúcs ellenőrzése, hogy valid értéket tárol-e, optimalizálás szempontjából
        if jelenlegi_suly != tavolsagok[jelenlegi_csucs]:
            continue
        #az utak a lista ami az út tuple-üket tárolja (első: súly, második: csúcs)
        for utak in utak_adj_list[jelenlegi_csucs]:
            #itt a jelenlegi csúcs a kiindulocsucs
            #az összes szomszédja amin iterálunk végpontok
            #az alábbi kommentben a kezdopont nem a dijkstra kezdopontja, csupán egy közelítés kezdőpontja
            """
                if tavolsagok[kezdopont] > tavolsagok[kezdopont] + kozvetlen_tav(graf, kezdopont, vegpont):
                    tavolsagok[vegpont] = tavolsagok[kezdopont] + kozvetlen_tav(graf, kezdopont, vegpont)
                    szulok[vegpont] = kezdopont
            """
            vegpont_sulya, vegpont = utak
            if tavolsagok[vegpont] > tavolsagok[jelenlegi_csucs] + vegpont_sulya:
                tavolsagok[vegpont] = tavolsagok[jelenlegi_csucs] + vegpont_sulya
                szulok[vegpont] = jelenlegi_csucs
                heapq.heappush(csucsok_prioritasi_sora, (tavolsagok[vegpont], vegpont))
    print(' '.join(f'{x}' for x in tavolsagok[1:]))




n, m = map(int, input().split())

graph = {}
#minden csúcs inicializálása út listával, mert lehet hogy nincs hozzá útvonal
for i in range(n+1):
    graph[i] = []

for _ in range(m):
    utak = input().split(" ")
    #adjacency list használata a gráf reprezentációjához ahol az utak tuple értékek
    #a tuple értékek első értéke a súly, a második érték a csúcs
    #a python két tuple összehasonlításánál először az első értéket nézi
    graph[int(utak[0])].append((int(utak[2]), int(utak[1])))
#bemeneti utak szomszédsági listájának tesztelése
#print(graph)
dijkstra_repulesi_utak(graph, 1)