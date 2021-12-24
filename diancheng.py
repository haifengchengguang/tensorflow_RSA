import tensorflow as tf
import time
time_start=time.time()
mat1 = tf.random.uniform([8192, 8192], minval=1, maxval=65536, dtype=tf.int64)
mat2 = tf.random.uniform([8192, 8192], minval=1, maxval=65536,dtype=tf.int64)
#result=tf.pow(mat1,mat2)
eRSA=65537
result_temp=tf.pow(mat1,mat2)
result=tf.math.floormod(result_temp,eRSA)
print(mat1)
print(mat2)
print(result)
time_end=time.time()
print('time cost',time_end-time_start,'s')
