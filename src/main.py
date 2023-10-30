import threading
from itpracujpl.itpracujpl_main import gather_data as itpracuj_gather_data
from nofluffjobs.nofluffjobs_main import gather_data as nofluff_gather_data
from plindeedcom.plindeedcom_main import gather_data as plindeed_gather_data

t1 = threading.Thread(target=itpracuj_gather_data)
t2 = threading.Thread(target=nofluff_gather_data)
t3 = threading.Thread(target=plindeed_gather_data)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Done!")