

class siso_PID:
  
  def __init__(self, kp, kd, ki):

    """
    A siso PID algorithm with internal anti-windup state
    #TODO inherited differentiation, integration (and anti-windup?) methods
    #TODO test in a simulation with a linear system
    """  
    self.kp = kp
    self.kd = kd
    self.ki = ki

    # integral state and anti-windup
    self.int_state = 0
    self.anti_windup_state = 0
    self.y_prev = None

  def num_int(self, error, dt):
    
    int_state = self.int_state + error*dt
    return int_state

  def num_diff(self, y, dt):
    y_dot = (y - self.y_prev) / dt
    return y_dot
  
  def calculate_u(self, y, y_ref, dt):

    if self.y_prev is not None:
      y_dot = self.num_diff(y, dt)
    else:
      y_dot = 0
      
    
    u = -(y - y_ref) * self.kp + self.int_state * self.ki - (y - y_dot) * self.kd

    self.int_state = self.num_int(-y + y_ref, dt)

    return u
  

  
