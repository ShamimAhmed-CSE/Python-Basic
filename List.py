
sub=["os","java","python"]
print(sub)

print(sub[1])
print(sub[1:])

print(sub[-1])

print("os" in sub)
print("s" in sub)

sub +["in","out"]
print(sub)

print(sub +["in","out"])

print(sub *3)

print(len(sub))

sub.append("in_Now")
print(sub)

sub.insert(2,"possition")
print(sub)

sub.remove("in_Now")
print(sub)

ls=[20,50,4,8,90]

ls.sort()
print(ls)
ls.reverse()
print(ls)
print(max(ls))
print(min(ls))
ls2=ls.copy()
ls.pop()
print(ls)
print(ls2)

