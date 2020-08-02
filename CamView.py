import cv2
import time
import concurrent.futures as futures
import sys
import math
import numpy

if __name__ == '__main__':
    windowname = 'CamView'
    num = 0
    capture = cv2.VideoCapture(num, cv2.CAP_DSHOW)

    while(True):
        # 画像の読み込み，失敗したらブランク画像
        ret, frame = capture.read()
        if frame is None:
            frame = numpy.zeros((9, 16, 3))
        # end

        # Windowの生成
        cv2.namedWindow(windowname, cv2.WINDOW_NORMAL)

        # Windowと画像のresize，コメントアウト可能
        x, y, w, h = cv2.getWindowImageRect(windowname)
        gcd = math.gcd(frame.shape[1], frame.shape[0])
        wr = int(frame.shape[1] / gcd)
        hr = int(frame.shape[0] / gcd)
        if h / frame.shape[0] > w / frame.shape[1]:
            windowsize = (int(w / wr) * wr, int(w * frame.shape[0] / frame.shape[1] / hr) * hr)
        #end
        else:
            windowsize = (int(h * frame.shape[1] / frame.shape[0] / wr) * wr, int(h / hr) * hr)
        #end
        cv2.resizeWindow(windowname, windowsize)
        frame = cv2.resize(frame, windowsize, cv2.INTER_AREA)

        # 画像の表示
        cv2.imshow(windowname, frame)

        # Escで終了，Spaceでカメラの選択
        key = cv2.waitKey(1)
        if key & 0xFF == 27:
            break
        # end
        elif key & 0xFF== 32:
            capture.release()
            num = (num + 1) % 5
            capture = cv2.VideoCapture(num, cv2.CAP_DSHOW)
        # end
    # end

    # caputureのreleaseとWindowの終了
    capture.release()
    cv2.destroyAllWindows()
# end
