from  cmath import phase
# Enter your code here. Read input from STDIN. Print output to STDOUT
complex_number = input()

border_between_real_and_imag = 1
for i in complex_number[1:]:
    if not i.isnumeric():
        break
    border_between_real_and_imag += 1

    
real_part = int(complex_number[:border_between_real_and_imag])
imagine_part = int(complex_number[border_between_real_and_imag:-1])


print(abs(complex( real_part,imagine_part)))
print(phase(complex( real_part,imagine_part)))
