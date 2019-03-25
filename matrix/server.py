# server.py
import sys
import matrix

def stream_kiolvasasa(klienstol_adat_byte):
    # MAX_BUFFER_MERET = ekkora lehet a bejovo adat
    #import sys
    input_from_client = klienstol_adat_byte.decode("utf8").rstrip()
    print("Bejovo adat: {} ".format(input_from_client))
    bevitt_adat_feldolgozasa(input_from_client)
    return input_from_client


def bevitt_adat_feldolgozasa(bejovoadat):
    matrix.fugvenyek_kivalasztasa(bejovoadat)


def kliens_szal(conn, ip, port, MAX_BUFFER_MERET=4096):

    while True:
        klienstol_adat_byte = conn.recv(MAX_BUFFER_MERET)
        siz = sys.getsizeof(klienstol_adat_byte)
        if siz >= MAX_BUFFER_MERET:
            print("A bejovo adat nagyobb. mint a megengedett: {}".format(siz))
            # a bejovo adat dekodolasa es a sor vegenek levagasa
        else:
            if not klienstol_adat_byte:
                break
            else:
                stream_kiolvasasa(klienstol_adat_byte)
    print('Csatlakozas vege: ' + ip + ':' + port)


def start_server():

    import socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # A program konnyu inditasara es leallitasara
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket letrehozva')

    try:
        soc.bind(("0.0.0.0", 12345))
        print('Socket bind complete')
    except socket.error as msg:

        print('Hiba: ' + str(sys.exc_info()))
        sys.exit()

    # Start
    soc.listen(10)
    print('A szerver mukodik')
    # Egyszerre tobb kliens csatlakozasara
    from threading import Thread

    # vegtelen ciklus a kliensek csatlakozasara
    while True:
        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        print('Csatlakozva innen: ' + ip + ':' + port)
        try:
            Thread(target=kliens_szal, args=(conn, ip, port)).start()
        except:
            print("Hiba!")
            import traceback
            traceback.print_exc()
    soc.close()


start_server()
