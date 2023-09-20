# Interpalyatsion qidiruvni recursive usulda tadbiq qilish

# Agar x (qidirilayotgan element  arr[0..n-1] arrayda bo'lsa
# element indexi qaytariladi aks holda -1 qaytariladi.
import random
def interpolationSearch(arr, lo, hi, x):

	# Array tartiblanganligi sababli, arrayda mavjud element  belgilangan diapazonda bo'lishi kerak
	if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

		# Yagona taqsimotni hisobga olgan holda pozitsiyani tekshirish.
		pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
					(x - arr[lo]))

		# qidirilayotgan element topilgan holatda
		if arr[pos] == x:
			return pos

		# Agar x o'ng tomondagi ostki arrayda bo'lsa 
		if arr[pos] < x:
			return interpolationSearch(arr, pos + 1,
									hi, x)

		# Agar x chap tomondagi ostki arrayda bo'lsa 
		if arr[pos] > x:
			return interpolationSearch(arr, lo,
									pos - 1, x)
	return -1

# Massiv o'lchamini kiritish.
n = int(input("Massiv o'lchamini kiriting: "))

# Qidiruv o'tkaziladigan elementlar to'plami
arr = [random.randint(0,100) for _ in range(n)]
arr = sorted(arr)
print(arr)

# qidiriladigan element
x = int(input("Elementni kiriting: "))
index = interpolationSearch(arr, 0, n - 1, x)

if index != -1:
	print("Qidirilayotgan element indeksi: ", index)
else:
	print("Element topilmadi !")
