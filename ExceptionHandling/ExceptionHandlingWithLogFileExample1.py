import traceback
import logging as log


class ZeroError(Exception):
    def __init__(self, mesg):
        super().__init__(self)
        self.mesg = mesg

    def __str__(self):
        return self.mesg


log.basicConfig(
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
    filemode='a',
    filename="err.log")
try:
    a = int(input("Enter a num : "))
    b = int(input("Enter another num : "))
    if a == 0 or b == 0:
        raise ZeroError("Values cannot be ZERO....")
    res = a + b

except ZeroError as e1:
    log.warning(e1)
except ValueError as e2:
    log.warning(e2)
    print("values suppose to be INTEGER")
except:
    log.warning("SOME UNKNOWN PROBLEM12")
    traceback.print_exc()
else:
    print("ANS = ", res)
finally:
    log.warning("CLEANUP")
