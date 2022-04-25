import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()

# ეს ფუნქცია მოპარულია 
def SpiralOrder(A, M, N):
 
 
    top = left = 0
    bottom = M - 1
    right = N - 1
 
    # construct an M × N matrix
    mat = [[0 for x in range(N)] for y in range(M)]
 
    index = 0
 
    while True:
 
        if left > right:
            break
 
        # print top row
        for i in range(left, right + 1):
            mat[top][i] = A[index]
            index +=  1
        top +=  1
 
        if top > bottom:
            break
 
        # print right column
        for i in range(top, bottom + 1):
            mat[i][right] = A[index]
            index +=  1
        right -=  1
 
        if left > right:
            break
 
        # print bottom row
        for i in range(right, left - 1, -1):
            mat[bottom][i] = A[index]
            index +=  1
        bottom -=  1
 
        if top > bottom:
            break
 
        # print left column
        for i in range(bottom, top - 1, -1):
            mat[i][left] = A[index]
            index +=  1
        left +=  1
 


    return mat




# M × N matrix
M = N = Matrix_len =1001

# a list of length M×N
A = [ int(x) for x in range((Matrix_len**2),0,-1)]

matrix = SpiralOrder(A, M, N)  # შემოგვყავს სპირალური მატრიცა





sum = 0

for i in range(Matrix_len): # ვკრიბავთ ყველა დიაგონალურ წევრს მარცხნიდან მარჯვნივ
    sum += (matrix[i][i])

for i in range(Matrix_len):     # ვკრიბავთ ყველა დიაგონალურ წევრს მარჯვნიდან მარვცნივ
    sum += (matrix[i][-i-1])

print(sum - matrix[Matrix_len//2][Matrix_len//2])  # ვკრიბავთ ყველა დიაგონალურ წევრს და ვაკლებთ შუა წევრს რადგან ის ორჯერ შეიკრიბა დიაგონალების კვეთის გამო

end = time.time()  
print(end-start)    # ვპრინტავთ გამოთვალზე დახარჯულ დროს
 