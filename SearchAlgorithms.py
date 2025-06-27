nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]
key = 77


print("Linear Search:")
found_linear = False
for i in range(len(nums)):
    if nums[i] == key:
        print("Found at position:", i)
        found_linear = True
        break

if not found_linear:
    print("Not found")


print("\nBinary Search:")
start = 0
end = len(nums) - 1
found = False

while start <= end:
    mid = (start + end) // 2
    if nums[mid] == key:
        print("Found element at pos:", mid)
        found = True
        break
    elif key < nums[mid]:
        end = mid - 1
    else:
        start = mid + 1

if not found:
    print(f"{key} not found in the list")