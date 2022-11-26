import os
import matplotlib.pyplot as plt
BG_ = 0             # begingetal
F0_ = F1_ = True    # vlag


def f_error(v_):                        # error messages, v_ = FN_ = foutnummer als getal
    if v_ == 0: print("  Het programma wordt gestopt!\n")
    if v_ == 1: print("  >! Fout: kies het juiste getal !<\n")
    if v_ == 2: print("  >! Fout: verkeerde invoer !<\n")


def f_invoer():                         # controle van invoer en stoppen programma; g_ = BG_ = begingetal
    global BG_
    print("  ----------\n")
    while F1_ is True:
        try:
            print("  (0= stop)")
            g_ = int(input(">>> geef een geheel getal > 1: "))
            if g_ == 0:
                f_error(0)
                quit()                                          # stop het programma
            BG_ = g_
            break                                               # stap uit de lus
        except ValueError:
            f_error(2)


def f_algoritme(g_):								    # Collatz conjecture, g_ = BG_
    i_ = 0  											# de teller voor aantal iteraties
    m_ = g_  											# de maximale waarde
    b_ = g_  											# geheugen voor de invoer
    w_ = [g_]  											# lijst voor de waarden

    while g_ != 1:                          # zolang het resultaat niet 1 is .....
        if (g_ % 2) == 0:                   # mod 2 test, wanneer geen rest (=0) dan is het even
            g_ = int(g_ / 2)                # regel algoritme: bij even delen door 2
            i_ += 1                         # teller voor aantal iteraties
        else:                               # en anders (getal_ % 2) == 1 dus oneven
            g_ = int(3 * g_ + 1)            # regel algoritme: bij oneven dan 3x + 1
            i_ += 1                         # teller voor aantal iteraties
        if g_ > m_:                         # hier wordt bijgehouden wat de maximale waarde is
            m_ = g_                         # nieuwe max
        w_.append(g_)                       # getal aan lijst toevoegen

    return b_, i_, m_, w_                   # output !!!


def f_mon(b_, i_, m_, w_):                  # results on screen; b_, i_, m_, w_ = begin_, iteratie_, maximaal_, waarden_
    print("  beginwaarde      : ", b_)
    print("  aantal iteraties : ", i_)
    print("  maximale waarde  : ", m_)
    print("  waarden:")
    print(" ", w_)
    print("  ----------\n")


def f_csv(b_, i_, m_, w_, n_):                 # results to csv file
    pad_ = "/Collatz/csv"                      # b_, i_, m_, w_, n_ = begin_, iteratie_, maximaal_, waarden_, naamcsv_
    f_ = os.path.exists(pad_)                  # f_ variabele of map bestaat
    if not f_:
        os.makedirs(pad_)
        print("  nieuwe map: " + pad_)

    with open(pad_ + "/" + n_, 'w') as f:
        f.write("beginwaarde      : " + str(b_) + "\n")
        f.write("aantal iteraties : " + str(i_) + "\n")
        f.write("maximale waarde  : " + str(m_) + "\n")
        for i_ in w_:                                               # i_ = teller
            f.write(str(i_) + "\n")
    print("  waarden opgeslagen als " + n_ + " in de map " + pad_)


def f_plot(t_, w_, n_):								    # plotting results, t_, w_, n_ = titel_, waarden_, naam_
    pad_ = "/Collatz/png"  	                            # de map
    f_ = os.path.exists(pad_)                           # f_ variabele of map bestaat
    if not f_:
        os.makedirs(pad_)
        print("nieuwe map: " + pad_)
    plt.suptitle(t_)
    plt.xlabel('itteraties')
    plt.ylabel('waarden')
    plt.plot(w_)
    plt.savefig(pad_ + "/" + n_)
    plt.close()  										# wanneer weggelaten dan meerdere grafieken in de afbeelding
    print("  grafiek opgeslagen als " + n_ + " in de map " + pad_)


while F0_ is True:                      # programma afloop
    keuze_ = 0
    try:
        f_invoer()
        print("  ----------\n")
        begin_, iteratie_, maximaal_, waarden_ = f_algoritme(BG_)  # resultaten van algoritme
        f_mon(begin_, iteratie_, maximaal_, waarden_)
        keuze_ = int(input("  (0= stop, 1= opslaan, 2= opnieuw)\n>>> keuze: "))

        if keuze_ < 0 or keuze_ > 3:
            raise ValueError
        elif keuze_ == 0:
            f_error(0)
            quit()
        elif keuze_ == 1:
            naamcsv_ = "Collatz_" + str(begin_) + ".csv"
            f_csv(begin_, iteratie_, maximaal_, waarden_, naamcsv_)
            titel_ = "startgetal " + str(begin_)
            naampng_ = "Collatz_" + str(begin_) + ".png"
            f_plot(titel_, waarden_, naampng_)
        elif keuze_ == 2:
            begin_ = iteratie_ = maximaal_ = waarden_ = 0
            raise ValueError

    except TypeError:
        f_error(1)
    except ValueError:
        if keuze_ != 2: f_error(2)
