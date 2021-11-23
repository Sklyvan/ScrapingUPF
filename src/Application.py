from Main import RunApplication

if __name__ == "__main__":
    mainLoop = True
    applicationIterator = RunApplication(deleteMode=False)
    while mainLoop:
        try: next(applicationIterator)
        except StopIteration: mainLoop = False
