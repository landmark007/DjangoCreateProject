from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Ho Bro")

def input(request, item_id, name):  # เพิ่มพารามิเตอร์ 'name'
    # if item_id is not None and name:  # ตรวจสอบว่า 'item_id' และ 'name' ไม่ใช่ค่าว่าง
    #return HttpResponse(f"Hi {name}, your id is {item_id}")  # ใช้ f-string เพื่อการจัดรูปแบบข้อความได้สะดวก
    return render(request, 'index.html')
    # else:
    # context_data = {
    #     "item_id": item_id
    # }
    # return render(request, 'index.html', context = context_data)

def table(request):
    return render(request, 'table.html')