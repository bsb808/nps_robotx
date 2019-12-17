
from tf.transformations import euler_from_quaternion

# Quaternion in order of x, y, z, w
q = (0, 0, 0.501213004674, 0.865323941623)
yaw = euler_from_quaternion(q)[2]
print yaw