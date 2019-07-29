import time
import sys

detik = 60

menit = 1

for sisa in range(menit * detik,0,-1):
    sys.stdout.write("\r") # "\r" berfungsi mengembalikan kursor ke tempat semula dan overwrite teks sebelumnya

    detik = detik - 1

    if detik <= 0:
        menit = menit - 1
        detik = 60

    if detik <=9:
        sys.stdout.write("[{:2d}:0:{:1d}] Pomodoro runnings".format(menit-1,detik))
    else:
        sys.stdout.write("[{:2d}:{:1d}] Pomodoro runnings".format(menit - 1,detik))

    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\n SELESAI")