# if __name__ == "__main__":
#     x=int(input())
#     y=int(input())
#     z=int(input())
#     n=int(input())
#     combination = [[x1,y1,z1] for x1 in range(x+1) for y1 in range(y+1) for z1 in range(z+1)]
#     ans = list(filter(lambda x:sum(x)!=n, combination))
#     print(ans)



# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))

#     maior = max(arr)
#     qnt = arr.count(maior)
    
#     for i in range(qnt):
#         arr.remove(maior)
        
#     print(max(arr))



# if __name__ == '__main__':
#     nums=[]
#     N = int(input())
    
#     for _ in range(N):
#         split_list=input().split()
#         if split_list[0] == 'print':
#             print(nums)
            
#         elif split_list[0] in ['sort','pop','reverse']:
#             eval(f"nums.{split_list[0]}()")
            
#         elif split_list[0] == 'insert':
#             nums.insert(int(split_list[1]),int(split_list[2]))
            
#         elif split_list[0] in ['remove','append']:
#             eval(f"nums.{split_list[0]}({split_list[1]})")



# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     t=tuple(integer_list)
#     print(hash(t))


n=int(input())
s=set(map(int, input().split()))
N = int(input())

for _ in range(N):
    cmd=input().split()
    if(len(cmd)==1):
        s.pop()
    else:
        cmd="s."+cmd[0]+"("+cmd[1]+")"
        eval(cmd)
        
print(sum(list(s)))