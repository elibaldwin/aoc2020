class bot:
  def __init__(self):
    self.accumulator = 0
    self.fmap = dict()
  
  def reset(self):
    self.accumulator = 0
  
  def run(self, instr):
    if instr[0] not in self.fmap:
      self.fmap[instr[0]] = eval(f'self.{instr[0]}')
    return self.fmap[instr[0]](instr[1:])
  
  def acc(self, arg):
    self.accumulator += arg[0]
    return 1
  
  def jmp(self, arg):
    return arg[0]
  
  def nop(self, arg):
    return 1