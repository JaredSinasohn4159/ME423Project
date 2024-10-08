from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
import utime
import robot_maneuvers as rm

# large motor max speed 1020 deg/s
# medium motor max speed 1500 deg/s

class Joint1:
    def __init__(self, initial_position=0):
        self.initial_position = initial_position
        self.pos = self.initial_position
        self.motor = Motor(Port.A)
        self.motor.track_target(self.pos)
        #self.motor.run_target(speed=1000,target_angle=self.pos,wait=False)
        
    def set_motor_pos(self,pos):
        self.pos=pos
        self.motor.track_target(self.pos)
        #self.motor.run_target(speed=1000,target_angle=self.pos,wait=False)

        
    def is_stalled(self):
        return self.motor.stalled()
        
class Joint2:
    def __init__(self, initial_position=0):
        self.initial_position = initial_position
        self.pos = self.initial_position
        self.motor = Motor(Port.B,positive_direction=Direction.CLOCKWISE)
        self.motor.track_target(self.pos)
        #self.motor.run_target(speed=1000,target_angle=self.pos,wait=False)
        
    def set_motor_pos(self,pos):
        self.pos=pos
        self.motor.track_target(self.pos)
        #self.motor.run_target(speed=1000,target_angle=self.pos,wait=False)

    def is_stalled(self):
        return self.motor.stalled()
    def get_angle(self):
        return self.motor.angle()
    
class Joint3:
    def __init__(self, initial_position=0):
        self.initial_position = initial_position
        self.pos = self.initial_position
        self.motor = Motor(Port.C,gears=[12,36])
        self.motor.track_target(self.pos)
        #self.motor.run_target(speed=500,target_angle=self.pos,wait=False)
        
    def set_motor_pos(self,pos):
        self.pos=pos
        self.motor.track_target(self.pos)
        #self.motor.run_target(speed=500,target_angle=self.pos,wait=False)

    def is_stalled(self):
        return self.motor.stalled()


if __name__ == "__main__":
    tstep = 10
    j1 = Joint1()
    j2 = Joint2()
    j3 = Joint3()
    m1 = rm.Maneuver_1()
    pos1 = m1.get_J1_pos()
    pos2 = m1.get_J2_pos()
    pos3 = m1.get_J3_pos()
    for i in range(len(pos2)):
        j1.set_motor_pos(pos1[i])
        j2.set_motor_pos(-1*(pos2[i]-70))
        j3.set_motor_pos(-1*(pos3[i]-140))
        wait(tstep)
    wait(500)
    m2 = rm.Maneuver_2()
    pos1 = m2.get_J1_pos()
    pos2 = m2.get_J2_pos()
    pos3 = m2.get_J3_pos()
    for i in range(len(pos2)):
        j1.set_motor_pos(pos1[i])
        j2.set_motor_pos(-1*(pos2[i]-70))
        j3.set_motor_pos(-1*(pos3[i]-140))
        wait(tstep)
    wait(500)
    m3 = rm.Maneuver_3()
    pos1 = m3.get_J1_pos()
    pos2 = m3.get_J2_pos()
    pos3 = m3.get_J3_pos()
    for i in range(len(pos2)):
        j1.set_motor_pos(pos1[i])
        j2.set_motor_pos(-1*(pos2[i]-70))
        j3.set_motor_pos(-1*(pos3[i]-140))
        wait(tstep)
    j1.set_motor_pos(0)
    j2.set_motor_pos(0)
    j3.set_motor_pos(0)