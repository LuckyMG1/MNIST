import numpy as np

def read_images(input_file):
    with open(input_file, 'rb') as fid:
        fid.read(16) # ignore headers
        count = 0
        for i in range(60000): # size of training dataset
            image_matrix = np.zeros((28,28))
            for j in range(28):
                line = ""
                for k in range(28):
                    current_char = int(fid.read(1).hex(), 16) # convert hex2dec
                    image_matrix[j][k] = current_char / 255 # normalize
            yield image_matrix
            count += 1
            print(count)

def init_network(sizes):
    layers = len(sizes)
    weights
    

if __name__ == "__main__":
    read_images("images/train-images-idx3-ubyte/train-images-idx3-ubyte")
