def gcd(m, n):
   r = m % n
   while r != 0:
      m = n
      n = r
      r = m % n
   return n

print ("\n", "gcd (10, 35) = ", gcd(10, 35))

print ("\n", "gcd (-10, -35) = ", gcd(-10, -35))

print ("\n", "gcd (-10, 35) = ", gcd(-10, 35))

print ("\n", "gcd (735, 175) = ", gcd(735, 175))


print ("\n", "gcd (735, 350) = ", gcd(735, 350))
