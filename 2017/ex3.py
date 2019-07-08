import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identity_function(x):
    return x

def init_network():
    W1 = np.array([]) # 1layer
    W2 = np.array([]) # 2layer
    W3 = np.array([]) # 3layer
    W4 = np.array([]) # 4layer

    # 1layer
    N = [2, 4, 3, 3] # double loop
    M = [4, 3, 3, 2] #
    for i in range(N[0]):
        raw_in = list(map(float,input().split()))
        W1 = np.append(W1,np.array(raw_in))

    # 2layer
    for i in range(N[1]):
        raw_in = list(map(float,input().split()))
        W2 = np.append(W2,np.array(raw_in))

    # 3layer
    for i in range(N[2]):
        raw_in = list(map(float,input().split()))
        W3 = np.append(W3,np.array(raw_in))

    # 4layer
    for i in range(N[3]):
        raw_in = list(map(float,input().split()))
        W4 = np.append(W4,np.array(raw_in))

    network = {} #dictionary
    network['W1'] = np.reshape(W1,(N[0],M[0]))
    network['b1'] = np.array([0,0,0,0])
    network['W2'] = np.reshape(W2,(N[1],M[1]))
    network['b2'] = np.array([0,0,0])
    network['W3'] = np.reshape(W3,(N[2],M[2]))
    network['b3'] = np.array([0,0,0])
    network['W4'] = np.reshape(W4,(N[3],M[3]))
    network['b4'] = np.array([0,0])

    return network

def forward(network,x):
    W1, W2, W3, W4 = network['W1'], network['W2'], network['W3'], network['W4']
    b1, b2, b3, b4 = network['b1'], network['b2'], network['b3'], network['b4']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3
    z3 = sigmoid(a3)

    a4 = np.dot(z3, W4) + b4
    y = identity_function(a4)

    return y

def main():
      
    network = init_network()
    #print("OK!\n")
    inp=int(input()) # n
    for i in range(inp):
        x = list(map(float,input().split()))
        y = forward(network, x)
        print("{} {}".format(y[0], y[1]))

if __name__=="__main__":
    main()