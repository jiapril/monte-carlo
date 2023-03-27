import pi_calculator

def run_pi(times):
    results={}
    for i in times:
        results[i]=pi_calculator.pi_calculator_np(i)
    print(results)

run_pi([10,100,1000,10000,100000,500000])

