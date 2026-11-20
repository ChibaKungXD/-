VAT_RATE = 0.07
TRAVEL_RATE_PER_KM = 2  # ค่าเดินทางของสินค้า บาทต่อกิโลเมตร

# ขนาด: (ชื่อ, ค่าจัดส่ง, ค่าบรรจุภัณฑ์)
SHIPPING_RATES = {
    "1": ("เล็ก", 40, 10),
    "2": ("กลาง", 80, 20),
    "3": ("ใหญ่", 150, 40),
}

# ระดับความเสียหาย: (ชื่อ, อัตราชดเชย % ของราคาสินค้า)
DAMAGE_LEVELS = {
    "0": ("ไม่เสียหาย", 0.0),
    "1": ("เสียหายเล็กน้อย", 0.20),
    "2": ("เสียหายปานกลาง", 0.50),
    "3": ("พังเสียหายทั้งหมด", 1.00),
}

def input_float(message):
    """รับตัวเลขที่ไม่ติดลบ ถ้ากรอกผิดจะให้กรอกใหม่"""
    while True:
        try:
            value = float(input(message))
            if value >= 0:
                return value
            print("กรุณากรอกค่าที่ไม่ติดลบ")
        except ValueError:
            print("กรุณากรอกเป็นตัวเลข")

def choose(options, prompt):
    """ให้เลือกตัวเลือกจาก dict จนกว่าจะเลือกถูก"""
    choice = input(prompt).strip()
    while choice not in options:
        choice = input(f"กรุณาเลือก {', '.join(options)}: ").strip()
    return options[choice]

price = input_float("กรอกราคาสินค้า (บาท): ")

print("\nเลือกขนาดสินค้า:")
for key, (name, ship_fee, pack_fee) in SHIPPING_RATES.items():
    print(f"  {key}. {name} (จัดส่ง {ship_fee:,.2f} | บรรจุภัณฑ์ {pack_fee:,.2f} บาท)")
size_name, shipping, packaging = choose(SHIPPING_RATES, "เลือกขนาด (1-3): ")

distance = input_float("ระยะทางขนส่ง (กิโลเมตร): ")
travel_fee = distance * TRAVEL_RATE_PER_KM

print("\nสภาพสินค้าเมื่อถึงมือลูกค้า:")
for key, (name, rate) in DAMAGE_LEVELS.items():
    print(f"  {key}. {name} (ชดเชย {rate:.0%} ของราคาสินค้า)")
damage_name, damage_rate = choose(DAMAGE_LEVELS, "เลือกสภาพสินค้า (0-3): ")

vat = price * VAT_RATE
total = price + vat + shipping + packaging + travel_fee
compensation = price * damage_rate
net_total = total - compensation

print("\n===== สรุปรายการชำระเงิน =====")
print(f"ราคาสินค้า: {price:,.2f} บาท")
print(f"ภาษีมูลค่าเพิ่ม 7%: {vat:,.2f} บาท")
print(f"ค่าจัดส่ง (ขนาด{size_name}): {shipping:,.2f} บาท")
print(f"ค่าบรรจุภัณฑ์: {packaging:,.2f} บาท")
print(f"ค่าเดินทางของสินค้า ({distance:,.1f} กม.): {travel_fee:,.2f} บาท")
print(f"ยอดรวมก่อนชดเชย: {total:,.2f} บาท")
if compensation > 0:
    print(f"หัก ค่าชดเชย ({damage_name} {damage_rate:.0%}): -{compensation:,.2f} บาท")
print(f"ยอดชำระสุทธิ: {net_total:,.2f} บาท")