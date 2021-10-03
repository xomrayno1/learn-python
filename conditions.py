average = 9.5

if average > 10:
    print("average không chính xác ")
elif average >= 8:
    print("Bạn là học sinh giỏi")
    if average >= 9:
        print("Chúc mừng bạn nhận được học bổng học sinh giỏi")
    else:
        print("Xin lỗi bạn đã bỏ lỡ học bổng học sinh giỏi")
elif average >= 7:
    print("Bạn là học sinh khá")
elif average >= 5:
    print("Bạn là học sinh trung bình")
else:
    print("Bạn học sinh yếu")
print("Điểm của bạn là  ", average)

