
N_JOINTS = 12

DEVICE = [
        "can1", "can1", "can1",
        "can1", "can1", "can1",
        "can0", "can0", "can0",
        "can0", "can0", "can0",
        ]

CAN_ID = [
        10, 11, 12,
        7, 8, 9,
        4, 5, 6,
        1, 2, 3,
        ]

MOTOR_TYPE = [
        "RobStride03", "RobStride03", "RobStride03",
        "RobStride03", "RobStride03", "RobStride03",
        "RobStride03", "RobStride03", "RobStride03",
        "RobStride03", "RobStride03", "RobStride03",
        ]

MOTOR_DIR = [
         1, -1, -1,
         1,  1,  1,
        -1, -1, -1,
        -1,  1,  1,
        ]

MOTOR_OFFSET_THRE = [
        None, None, 4,
        None, None, None,
        None, None, 5.0,
        None, 5.0, None,
        ]

MOTOR_OFFSET_ANGLE = [ # These values must be manually adjusted
        -4.1474, 3.2532, -2.8308,
        -1.3524, -4.1952, -8.5498,
        1.9504, 3.5705, -3.7100,
        1.2706, 1.0788, -8.5908,
        ]

JOINT_NAME = [
        'BL_collar_joint', 'BL_hip_joint', 'BL_knee_joint',
        'BR_collar_joint', 'BR_hip_joint', 'BR_knee_joint',
        'FL_collar_joint', 'FL_hip_joint', 'FL_knee_joint',
        'FR_collar_joint', 'FR_hip_joint', 'FR_knee_joint',
        ]

STANDBY_ANGLE = [
         0.169, 1.28, -2.87,
        -0.169, 1.28, -2.87,
         0.169, 1.28, -2.87,
        -0.169, 1.28, -2.87,
        ]

DEFAULT_ANGLE = [
        0.0, 0.7, -1.2, # BL
        0.0, 0.7, -1.2, # BR
        0.0, 0.7, -1.2, # FL
        0.0, 0.7, -1.2, # FR
        ]

KP_GAIN = [
        50.0, 50.0, 50.0,
        50.0, 50.0, 50.0,
        50.0, 50.0, 50.0,
        50.0, 50.0, 50.0,
        ]

KD_GAIN = [
        2.0, 2.0, 2.0,
        2.0, 2.0, 2.0,
        2.0, 2.0, 2.0,
        2.0, 2.0, 2.0,
        ]

ACTION_SCALE = 0.2
ACTION_CLIPPING = 20
CONTROL_DECIMATION = 4
CONTROL_DT = 0.005

CONTROL_HZ = 50

CAN_HZ = 200

SIM_HZ = 200

