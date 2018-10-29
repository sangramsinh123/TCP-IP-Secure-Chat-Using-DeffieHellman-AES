import random

def isPrime(num):
    for i in range(2,int(num/2)+1):
        if(num%i==0):
            return -1
    return num

def generateQ():
    check = 0
    while(check==0):
        q = isPrime(random.randint(1,100))
        if(q!=-1):
            return q

def checkPrimitive(alphaArray):
    check = 0
    j = 1
    for i in alphaArray:
        if(j!=i):
            check = 1
            break
        j += 1
    return check

def findAlpha(q):
    for alpha in range(1,q):
        alphaArray = []
        for j in range(1,q):
            alphaArray.append(pow(alpha,j)%q)
        alphaArray.sort()
        if(checkPrimitive(alphaArray)==0):
            return alpha

def findPublicKey(q,alpha,privateKey):
    return(pow(alpha,privateKey)%q)

def keyGeneration(privateKey,publicKey,q):
    return(pow(publicKey,privateKey)%q)

def keyGeneration_A():
    q = generateQ()
    print("q = " + str(q))
    alpha = findAlpha(q)
    print("Alpha = " + str(alpha))
    privateKey_A = random.randint(1,q-1)
    print("Private Key for A = " + str(privateKey_A))
    publicKey_A = findPublicKey(q,alpha,privateKey_A)
    print("Public Key for A = " + str(publicKey_A))
    #print("Final key = " + str(keyGeneration(privateKey_A,publicKey_B,q)))

    keyArray = [q,alpha,privateKey_A,publicKey_A]
    return keyArray

def keyGeneration_B(q,alpha):
    privateKey_B = random.randint(1,q-1)
    print("Private Key for B = " + str(privateKey_B))
    publicKey_B = findPublicKey(q,alpha,privateKey_B)
    print("Public Key for B = " + str(publicKey_B))

    keyArray = [privateKey_B,publicKey_B]
    return keyArray

def exc(q,privateKeyA,publicKeyB):
    actualKey = str(keyGeneration(privateKeyA,publicKeyB,q))
    print("Final key from A = " + actualKey)
    return actualKey

def exchangeKey():
    q = generateQ()
    print("q = " + str(q))
    alpha = findAlpha(q)
    print("Alpha = " + str(alpha))
    privateKey_A = random.randint(1,q-1)
    privateKey_B = random.randint(1,q-1)
    print("Private Key for A = " + str(privateKey_A))
    print("Private Key for B = " + str(privateKey_B))
    publicKey_A = findPublicKey(q,alpha,privateKey_A)
    publicKey_B = findPublicKey(q,alpha,privateKey_B)
    print("Public Key for A = " + str(publicKey_A))
    print("Public Key for B = " + str(publicKey_B))
    print("Final key from A = " + str(keyGeneration(privateKey_A,publicKey_B,q)))
    print("Final key from B = " + str(keyGeneration(privateKey_B,publicKey_A,q)))

    keyArray = [privateKey_A,publicKey_A]
    return keyArray

def main():
    print "HERE @ MAIN"

main()