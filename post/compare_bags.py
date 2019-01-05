import rosbag
import tf

fnames = ['baseline_2019-01-04-14-49-35.bag',
          'upward_force_only_2019-01-04-15-17-26.bag',
          'cylinder_v1_2019-01-04-16-09-47.bag',
          'y_leftright_2019-01-04-17-14-01.bag',
          'x_center_2019-01-04-17-20-32.bag',
          'x_center_n4_2019-01-04-17-23-33.bag',
          'final_pr_2019-01-04-17-32-16.bag']
'''
fnames = ['x_center_2019-01-04-17-20-32.bag',
          'x_center_n4_2019-01-04-17-23-33.bag']
'''


figure(1)
clf()
figure(2)
clf()

for fname in fnames:

    bag = rosbag.Bag(fname)

    tt = []
    x = []
    y = []
    z = []
    r = []
    p = []
    y = []

    for topic, msg, t in bag.read_messages(topics=['/gazebo/model_states']):
        # Assume that the WAMV is the last entry in the array
        pose = msg.pose[-1]

        tt.append(t.to_sec())
        x.append(pose.position.x)
        y.append(pose.position.y)
        z.append(pose.position.z)
        euler = tf.transformations.euler_from_quaternion((pose.orientation.x,
                                                         pose.orientation.y,
                                                         pose.orientation.z,
                                                         pose.orientation.w))
        r.append(euler[0]*180.0/pi)
        p.append(euler[1]*180.0/pi)
        y.append(euler[2]*180.0/pi)

    bag.close()

    figure(1)
    plot(tt,z,label=fname)
    xlabel('Time [s]')
    ylabel('Heave [m]')
    grid(True)
    figure(2)
    subplot(211)
    plot(tt,r)
    ylabel('Roll [deg]')
    grid(True)
    subplot(212)
    plot(tt,p)
    grid(True)
    ylabel('Pitch [deg]')
    xlabel('Time [s]')

figure(1)
legend()
    
    
show()
