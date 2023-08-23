import simpy


def my_proc(env):
    yield env.timeout(1)
    return "Monty Python's Flying Circus"


env = simpy.Environment()
proc = env.process(my_proc(env))
env.run(until=proc)


def subfunc(env):
    print(env.active_process)  # will print "p1"


def my_proc(env):
    while True:
        print(env.active_process)  # will print "p1"
        subfunc(env)
        yield env.timeout(1)


env = simpy.Environment()
p1 = env.process(my_proc(env))
env.active_process  # None
env.step()
env.active_process  # None
