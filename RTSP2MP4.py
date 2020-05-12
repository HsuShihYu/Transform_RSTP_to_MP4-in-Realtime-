import cv2

cap = cv2.VideoCapture('rtsp://admin:cht-123456@59.112.252.178:554/unicast/c1/s0/live')

# 設定擷取影像的尺寸大小
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1944)

# 使用 XVID 編碼
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output0.mp4', fourcc, 20.0, (2592, 1944))

name = "output"

count = 0
number = 0
while(True):
  ret, frame = cap.read()
  count = count + 1
  number = number + 1
  if ret == True:
    # 寫入影格
    out.write(frame)
    cv2.imshow('frame',frame)
    if count == 100:
      out.release()
      new_name = name + str(number/100)
      filename = new_name + ".mp4"
      out = cv2.VideoWriter(filename, fourcc, 20.0, (2592, 1944))
      count = 0
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else:
    break


# 釋放所有資源
cap.release()
out.release()
cv2.destroyAllWindows()

