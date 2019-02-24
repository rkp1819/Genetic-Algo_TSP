#TSP using GA
import random

global vertices
vertices = [1,2,3,4,5]
global cost_mat
cost_mat = [[0,2,3,4,5],[2,0,4,5,6],[3,4,0,7,8],[4,5,7,0,9],[5,6,8,9,6]]
global pop_size
##pop_size must be enen
pop_size = 100
global MAX_ITR
MAX_ITR = 100
global ELITE
ELITE = list(vertices)
ELITE.append(10**9)



def initialize():
    mat = []
    global pop_size
    global cost_mat
    global vertices
    for i in range(pop_size):
        random.shuffle(vertices)
        mat.append(list(tuple(vertices)))
    return mat

def selection(mat):
##    binary tournament
    global pop_size
    global ELITE
    mat = evaluate_costs(mat)
    mod_mat = []
    for i in range(pop_size):
        u = mat[random.randint(0, pop_size-1)]
        v = mat[random.randint(0, pop_size-1)]
        if(u[-1]>v[-1]):
            mod_mat.append(v)
            if v[-1]<ELITE[-1]:
                ELITE = v
        else:
            mod_mat.append(u)
            if u[-1]<ELITE[-1]:
                ELITE = u
    return mod_mat

def crossover(mat):
    global pop_size
    mod_mat = []
    for i in range(pop_size//2):            
        u = mat[random.randint(0, pop_size-1)]
        v = mat[random.randint(0, pop_size-1)]
        u = ''.join(list(map(str, u[:-1])))
        v = ''.join(list(map(str, v[:-1])))
        cut_index = random.randint(1, pop_size-2)
        u_part2 = []
        v_part2 = []
        for vp in v:
            if vp in list(u[cut_index:]):
                u_part2.append(vp)
        for up in u:
            if up in list(v[cut_index:]):
                v_part2.append(up)
        u = u[:cut_index]+''.join(list(map(str, u_part2)))
        v = v[:cut_index]+''.join(list(map(str, v_part2)))
        mod_mat.append(u)
        mod_mat.append(v)
    for i in range(len(mod_mat)):
        mod_mat[i] = list(map(int, list(mod_mat[i])))
    return mod_mat

def mutation(mat):
    i = random.randrange(len(mat))
    j = random.randrange(len(mat[i]))
    k = random.randrange(len(mat[i]))
    temp = mat[i][j]
    mat[i][j] = mat[i][k]
    mat[i][k] = temp
    return mat

def Terminate(mat):
    terminate = True
    cost = mat[0][-1]
    for row in mat:
        if row[-1] != cost:
            terminate = False
    return terminate

def evaluate_costs(mat):
    cost = 0
    k = 0
    mod_mat = mat
    global cost_mat
    for row in mat:
        for i in range(len(row)-1):
            cost+=cost_mat[ row[i]-1 ][ row[i+1]-1 ]
        mod_mat[k].append(cost)
        k+=1
    return mod_mat

def optimized_solution(mat):
    index = 0
    min_cost = mat[index][-1]
    
    for i in range(len(mat)):
        if mat[i][-1] < min_cost:
            min_cost = mat[i][-1]
            index = i
        
    return index

if __name__ == "__main__":
    for k in range(10):
        mat = initialize()
        i=0
        while(not Terminate(mat) and i<MAX_ITR):
            mat = mutation(crossover(selection(mat)))
            i+=1
        mat = selection(mat)
        print(f'The optimized solution is : {mat[optimized_solution(mat)]}, ELITE : {ELITE}')
