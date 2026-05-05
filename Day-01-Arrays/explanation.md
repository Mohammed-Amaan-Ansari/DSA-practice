# 💡 Explanation - Two Sum

## 🚀 Approach:
We use a **hash map (dictionary)** to store numbers we have already seen.

### Steps:
1. Iterate through the array.
2. For each element, calculate the complement:
   complement = target - current number
3. Check if the complement exists in the hash map:
   - If yes → we found the solution.
   - If no → store the current number in the map.
 
## 🧠 Key Insight:
Instead of checking all pairs (O(n²)), we store visited numbers and check in constant time.
 
## ⏱ Time Complexity:
O(n) — We traverse the array once.

## 💾 Space Complexity:
O(n) — For storing elements in the hash map.
 
## ❌ Brute Force Approach:
Check all pairs → O(n²) → Not efficient.
 
## ✅ Optimized Approach:
Using hash map → O(n)

 
## 📌 Summary:
- Use dictionary for fast lookup
- Always check complement BEFORE inserting