# 載入內建的 sys 模組蹦取得資訊
import sys
print(sys.platform)
print(sys.maxsize)

# 建立 geometry 模組, 載入使用
import sys
sys.path.append("modules")
import geometry
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,2,5,6)
print(result)

# 調整搜尋模組的路徑
import sys
sys.path.append("modules")
print(sys.path)     # 印出模組的搜尋路徑
import geometry
result=geometry.distance(1,1,5,5)
print(result)