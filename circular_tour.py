# https://practice.geeksforgeeks.org/problems/circular-tour-1587115620/1
def tour(gas, cost):
        #Code here
        length = len(gas)

        def do_dfs(node, visited=[], carry_over=0):
            if node in visited:
                return True
            visited.append(node)
            _next = (node + 1) % length
            carry_over = carry_over + (gas[node] - cost[node])
            if carry_over < 0:
                return False
            return do_dfs(_next, visited, carry_over)
            
        for i in range(length):
            if gas[i] >= cost[i]:
                if i ==6:
                    print("")
                result = do_dfs(i, [], 0)
                if result:
                    return i
        return -1

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
result = tour(gas, cost) 
print(result)