Longest substring without repeating characters

s = "abcabcbbefgh"

l=0
seen=set()
mx=0

for i in range(len(s)):
	while s[i] in seen:
		seen.remove(s[l])
		l=l+1
	seen.add(s[i])
	
	if i-l+1>mx:
	    mx=i-l+1
