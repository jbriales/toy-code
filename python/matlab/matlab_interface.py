import matlab.engine

eng = matlab.engine.start_matlab()
for i in range(0, 5):
    print(eng.generate_random(10))
