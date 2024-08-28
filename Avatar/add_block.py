import cv2


input_path = 'closed.jpg'
output_path = 'closed_block.jpg'


image = cv2.imread(input_path)
#print(image.shape)  # (1789, 1024, 3)
height, width, _ = image.shape


# 創建對話框畫布
overlay = image.copy()
output = image.copy()
dialog_height = 300 # 對話框高度
alpha = 0.5  # 對話框透明度

# 對話框的左上角和右下角座標
top_left = (0, height - dialog_height)
bottom_right = (width, height-100)


# 在圖像上繪製半透明的長方形
cv2.rectangle(overlay, top_left, bottom_right, (255, 255, 255), -1)
cv2.addWeighted(overlay, alpha, output, 1-alpha, 0, output)


cv2.imwrite(output_path, output)