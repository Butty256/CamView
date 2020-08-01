import cv2
#import time
#from timeout_decorator import timeout, TimeoutError
#import sys
import math

#@timeout(10)
#def VideoCapture2(num):
#    return cv2.VideoCapture(num)
## end

if __name__ == '__main__':
    #try:
    #    capture = VideoCapture2(0)
    #except TimeoutError:
    #    print("test timed out :(")
    #    sys.exit()
    #else:
    #    print("test finished successfully :)")
    capture = cv2.VideoCapture(1)
    windowname = 'CamView'

    while(True):
        ret, frame = capture.read()

        cv2.namedWindow(windowname, cv2.WINDOW_GUI_EXPANDED | cv2.WINDOW_NORMAL)
        x, y, w, h = cv2.getWindowImageRect(windowname)
        cv2.imshow(windowname, frame)
        gcd = math.gcd(frame.shape[1], frame.shape[0])
        wr = int(frame.shape[1] / gcd)
        hr = int(frame.shape[0] / gcd)
        #print(math.gcd(frame.shape[1], frame.shape[0]))
        if h / frame.shape[0] > w / frame.shape[1]:
            cv2.resizeWindow(windowname, (int(w / wr) * wr, int(w * frame.shape[0] / frame.shape[1] / hr) * hr))
        #end
        else:
            cv2.resizeWindow(windowname, (int(h * frame.shape[1] / frame.shape[0] / wr) * wr, int(h / hr) * hr))
        #end
        if cv2.waitKey(1) & 0xFF == 27:
            break
        # end
    # end

    capture.release()
    cv2.destroyAllWindows()
# end
