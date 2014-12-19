import multiprocessing as mp
import rainbow
import readchar
import sys, termios

if __name__ == '__main__':
    print(readchar.main)
    charqueue = mp.Queue()

    # keep stdin around
    fileno = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fileno)
    
    reader = mp.Process(target=readchar.main, args=(charqueue, fileno))
    game = mp.Process(target=rainbow.main, args=(sys.argv, charqueue))
    reader.start()
    game.start()

    # if the game exits, kill the reader
    game.join()
    reader.terminate()
    termios.tcsetattr(fileno, termios.TCSADRAIN, old_settings)
    sys.exit(0)