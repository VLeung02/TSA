from TSPA_framework import L298N, LDR

motor = L298N(**L298N.STANDARD_PIN_SET)
ldr = LDR(LDR.STANDARD_PIN_SET)

for move in ["low", "forward", "backward", "stop", "this will produce an error"]:
    print(motor.move(move))

