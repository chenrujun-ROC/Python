import sys
sys.path[len(sys.path):len(sys.path)]=["modules"]
print(sys.path)     # 印出模組的搜尋路徑
import geometry
result=geometry.distance(1,1,5,5)
print(result)